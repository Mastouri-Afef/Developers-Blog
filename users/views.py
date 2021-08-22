from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#inherits from forms form eli 3malneha importiha ba3d badel esm class (simple lowel"UserCreationForm -->"UserRegisterForm")
from .forms import UserRegisterForm
# Create your views here.
def register(request):
#if we get a post request then it instanciate a user creation form with that post data but with other request just instancite empty form
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        #if data is submitted 
        if form.is_valid():
            form.save()#will hashh password and make everyting secure and register this user w haka tnajem tal9ah kyyf temchi page admin
            username = form.cleaned_data.get('username')
            #flashmessage to show that we have recieve valide data
            messages.success(request, f'Yourn account has been created , you are now able to log in')#uiliser "Accounted created for {username}" si bech t7eb t7ot esm mo3ayen lel username 
            return redirect('login')
    else:
        form=UserRegisterForm()    
    return render(request,'register.html',{'form': form})
    
@login_required    
def profile(request):
    return render(request, 'profile.html')
    
