from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts': posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Your account has been created.')
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return HttpResponseRedirect('/dashboard/')
                else:
                    messages.error(request, 'Invalid credentials. Please try again.')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()  # Save the form data to the database
                messages.success(request, 'Post added successfully!')
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request, 'Error adding post. Please check the form and try again.')
        else:
            form = PostForm()
        return render(request, "blog/addpost.html", {'form': form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post updated successfully!')
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request, 'Error updating post. Please check the form and try again.')
        else:
            form = PostForm(instance=post)
        return render(request, "blog/addpost.html", {'form': form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            post = Post.objects.get(pk=id)
            post.delete()
            messages.success(request, 'Post deleted successfully!')
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/login/')
