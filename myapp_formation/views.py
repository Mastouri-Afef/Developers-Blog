from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from .models import Post, Comment
from .forms import *
from django.views.generic import ListView
from .forms import CommentForm #then add adiv in post_form.html
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

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
    #about pagination 
    paginate_by = 5

#class to see posts per user when i click to him  
class UserPostListView(ListView):

    model = Post
    template_name = 'user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
#get_query_set will limit our posts on that page to that specific user
    def get_queryset(self):
    #we wanna take the user that we took it from the url #(filter to take values from a certain user and then display it )
        user = get_object_or_404(User, username=self.kwargs.get('username'))#we want to get this object from that user model and the user that we will get is equal to username, and this username we will get it throw url and if this objet doesn't exit in database return 404,-->import user
        #return our quesrry
        return Post.objects.filter(author=user).order_by('-date_posted')
    #after that create a path url in the urlpatterns(in urls.py) then create the template("user-posts.html", in the template we will copy from home.html but we will just add a head to speccify that this is the user page)
class PostDetailView(DetailView):
#the model set to "Post"
    model = Post
    template_name = 'post_detail.html'
    #the go and register path('post/<int:pk>', PostDetailView.as_view(), name='post-detail')
#---> after that go to urls and import this class
#create a view for individual posts

    count_hit = True

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
        return  render(request, 'post_detail.html')
    def get_context_data(self, **kwargs):

        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({

            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })


        return context
    
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
