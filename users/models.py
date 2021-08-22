from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    #we will create one2one relationship with the existing User model (because a user can have one profile and the opposite)
    #delete a user donc na7iwhom min database te3na zeda
    #here we can add any fields that we want 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_pics is the directory where the ipages where uploaded to 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    # we will ay here how we want to print it 
    def __str__(self):
        return str(self.user)+"Profile"
   
   #after that code we should do migrations "python manage.py makemigrations" and "python manage.py migrate"  and install pillow  , the register this model "profile" in the admin file of our step
        

