from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#class UserRegisterForm va hérité de "UserCreationForm"
class UserRegisterForm(UserCreationForm):
#add the fields 
     email = forms.EmailField()
     #with the class meta we will specify the model that we will work with
     class Meta:
         model = User
         fields = (['username','email','password1','password2'])
         
#create a model form allow us to create a form that we will work with a specific database model 

class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()
     #with the class meta we will specify the model that wewill work with 
     class Meta:
         model = User
         fields = ['username','email']  
                    
class ProfileUpdateForm(forms.ModelForm):        
     email = forms.EmailField()
     #with the class meta we will specify the model that wewill work with 
     class Meta:
         model = Profile
         fields = ['image']   
#-->after adding those classes , go to views and added some code to to add these forms to our profile view         
#1-import it them on views then instanciate on the methods
