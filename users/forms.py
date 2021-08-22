from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
#class UserRegisterForm va hérité de "UserCreationForm"
class UserRegisterForm(UserCreationForm):
#add the fields 
     email = forms.EmailField()
     #with the class meta we will specify the model that wewill work with because mahma sar howa chya3ml creation te3 new user
     class Meta:
         model = User
         fields = (['username','email','password1','password2'])
