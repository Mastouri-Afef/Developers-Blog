from django.db import models
from PIL import Image
# Create your models here.

from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.conf import settings
class Profile(models.Model):
    #we will create one2one relationship with the existing User model (because a user can have one profile and the opposite)
    #delete a user so we will delete them from our database
    #here we can add any fields that we want 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_pics is the directory where the ipages where uploaded to 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # we will say here how we want to print it 
    def __str__(self):
        return str(self.user)+"Profile"
   
   #after that code we should do migrations "python manage.py makemigrations" and "python manage.py migrate"  and install pillow  , the register this model "profile" in the admin file of our step
        
    def save(self, *args, **kwargs):
        #the method that would be run after the model will be saved(this method exit in the parent cllass we can run it using super() to saved an instance of the profile )
        
        super(Profile, self).save(*args, **kwargs)
        #no we will grab the image after saving it and resize it--> so import pillow library
        #open the image for the profile instance that we are saving
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
        #if this condition true so we will try to resize it
            output_size = (300, 300)
            #to resize it an save it
            img.thumbnail(output_size)
            #save it to the same path
            img.save(self.image.path)
            
        
        
        
        
        
        
