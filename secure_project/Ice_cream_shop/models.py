from django.db import models
from django.contrib.auth.models import User

class IceCream(models.Model):
    flavor = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.flavor
    
class Feedback(models.Model):
    author = models.CharField(max_length=100)
    comment = models.TextField(max_length=160)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.rating} Stars"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'