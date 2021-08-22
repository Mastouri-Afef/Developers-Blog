#we want to have a post save after creating the profile when a user is created , the user here wuill become the sender of a signal and also we want to have a receiver to get this signal w bebi3a lazemno niportiw Profile ml ".models"
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#we want a user profile to be created for each new user 
@receiver(post_save, sender=User)#this say when a user was saved ,send this signal and this signal should be recieved by "reciever" that should be "create_profile" 

def create_profile(sender, instance, created, **kwargs):
#if the user was created , the created a profile object
    if created:
        #here we want to create a user equal to instance , then we want to run a function everytoime a user is created that is create a reciever that will should be a decorator "@receiver" take as argument "post_save" is the signal that we want and the sender
        Profile.objects.create(user=instance)

#save profile everytime the user object save
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
#instance ya3ni bih user
    instance.profile.save()
    
#then we should import this "signals.py" in apps.py    
