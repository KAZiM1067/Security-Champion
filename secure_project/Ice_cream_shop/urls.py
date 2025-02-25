from django.urls import path
from .views import home, about, feedback, login_view, signup_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='signup'), name='logout'),    
]
