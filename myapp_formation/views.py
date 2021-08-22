from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from .models import Post
from django.views.generic import ListView
#to create a detail view so impot it
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
def home(request):
       context = { 
            'posts': Post.objects.all()#il faut imports Post ml models à travers from .models import Post
       }
       return render(request, 'home.html', context)
       
#PostListView inherit from ListView

class PostListView(ListView):
#we need to create a variable "model" to tell ListView what model to query in order to create the list, in our case is all of our posts
    model = Post
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    #set the variable within our list views that is posts
    context_object_name = 'posts'
    #to mkae the oldest one in the top we need to change the order our query is making to the database
    ordering = ['-date_posted']

class PostDetailView(DetailView):
#the model set to "Post"
    model = Post
    template_name = 'post_detail.html'
    #the go and register path('post/<int:pk>', PostDetailView.as_view(), name='post-detail')
#---> after that go to urls and import this class
#create a view for individual posts

class PostCreateView(LoginRequiredMixin, CreateView):
#when we added LoginRequiredMixi and try to go to url(post/new) redirect me to login form 
        template_name = 'post_form.html'
        model = Post
        fields = ['title','content']#the fields that we want 
        #here we need to overide the form valid method to make the current logged in(the author) post the post blog or it will show error
        def form_valid(self, form):
        #set the authoer on the form
        #this is trying to say that the form trying to submit(post eli t7eb ta3mlelha submit ba3d ma3amart fields), it trys said to you before trying that take the instance and set the author equal to the current logged in user(self.request.user)
            form.instance.author = self.request.user
            #here we can validate the form by this instruction(return super().form_valid(form),the form is running in our parent class
            return super().form_valid(form)
        
        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'post_form.html'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
    #get the exact post that we are currently updateing, use the method of update_view called object to get the post
        post = self.get_object()
        #if the current user(request.user) is equal to post author
        if self.request.user == post.author:
        #then allow them to update the post
            return True
        #otherwise return false ken moch howa

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'post_confirm_delete.html'
    model = Post
    #success_url where to redirect when the deletion works ('/': is the home page) 
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        
        return False
                                
def about(request):
       return render(request, 'about.html', {'title': 'About'})
