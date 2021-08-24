from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm #inherits from forms form 

def register(request):
#if we get a post request then it instanciate a user creation form with that post data but with other request just instancite empty form
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        #if data is submitted 
        if form.is_valid():
            form.save()#will hash password and register this user et comme çà tu peux le voir si tu visite page admin
            username = form.cleaned_data.get('username')
            #flashmessage to show that we have recieve valide data
            messages.success(request, f'Your account has been created , you are now able to log in')#uiliser "Accounted created for {username}" si tu veux juste username 
            return redirect('login')
    else:
        form=UserRegisterForm()    
    return render(request,'register.html',{'form': form})
    
@login_required    
def profile(request):
#this condition will be run when we submit our form and possibly passing new data,we want to pass in the post data into our forms 
#this condition will be run when we sumit our form and we posibly we want to pass new data
    if request.method == 'POST':
    #instanciate for user update form and profile update form
        u_form = UserUpdateForm(request.POST, instance=request.user)#instance=request.user to find the data of the current logged in, "request.POST" (to pass in the post data)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)#here the profile will have the current image filled in, about"request.FILES" it's about getting field data with the request(image which the user try to upload)
        if u_form.is_valid() and p_form.is_valid():
        #here if the form is valid we gonna save the data
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)#instance=request.user to find the data of the current logged in
        p_form = ProfileUpdateForm(instance=request.user.profile)#here the profile will have the current image filled in            
    #pass those instanciates to our template---> create a context which is a dictionnary and the keys are the variables that we're going to access within our template 
    context = {
        'u_form': u_form,
        'p_form': p_form
          }
    #pass this context in our template(third arg in return render)
    return render(request, 'profile.html', context)
#---->then open the profile template and print out these forms(it looks like the register.html(copy the block "form" and paste in profile.htl, add the u_form et p_form in profile.html)
    
