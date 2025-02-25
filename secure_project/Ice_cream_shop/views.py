from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'Ice_cream_shop/home.html')

@login_required
def about(request):
    return render(request, 'Ice_cream_shop/about.html')

@login_required
def feedback(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')  # Fetch all feedbacks in descending order

    if request.method == "POST":
        author = request.POST.get("author")
        comment = request.POST.get("comment")
        rating = request.POST.get("rating")
        captcha = request.POST.get("captcha")

        # CAPTCHA Validation (5+5 should be 10)
        if captcha != "10":
            messages.error(request, "Incorrect CAPTCHA answer! Please try again.")
            return redirect("feedback")

        # Save feedback to database
        Feedback.objects.create(author=author, comment=comment, rating=int(rating))

        messages.success(request, "Your feedback has been submitted successfully!")
        return redirect("feedback")

    return render(request, "Ice_cream_shop/feedback.html", {"feedbacks": feedbacks})
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'Ice_cream_shop/login.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after successful sign-up
            messages.success(request, "You have successfully signed up!")
            return redirect('login')  # Redirect to the home page or another page
    else:
        form = SignUpForm()

    return render(request, 'Ice_cream_shop/signup.html', {'form': form})