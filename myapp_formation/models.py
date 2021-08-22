from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
        #create a get absolute method to make the django know how to find the location to a specific post , we need the reverse function
        #redirect will redirect you to a specific road but "reverse" will return the default url to that road as a string  and as we just want to return the url as a string (post that we fiill it)
        
    def get_absolute_url(self):
   #post-detail need a specific parameter is called pk ,that wyh we will use kwargs
        return reverse('post-detail', kwargs={'pk': self.pk})     
        
    
    
