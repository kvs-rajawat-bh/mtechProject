import datetime

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse

from .forms import RegisterForm, LoginForm, PostForm
from .models import UserInfo, Post
import simplejson as json


# Create your views here.

def index(request):
    return render(request, 'Instagram/index.html', {'request': request})


def user_profile(request, id):
    user = UserInfo.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            obj = Post()
            obj.pub_date = datetime.datetime.now()
            obj.user = user
            obj.image = form.cleaned_data['image']
            obj.description = form.cleaned_data['description']
            tags_generated = ["mountain", "hills", "hill station"]
            obj.tags = json.dumps(tags_generated)
            obj.save()
            form = PostForm()
            return render(request, 'Instagram/user_profile.html', {'user': user, 'post_form': form})
    elif request.method == 'GET':
        query_text = request.GET.get('q')
        if query_text is not None:
            query_text.split()
            query = []
            for word in query_text:
                query.append(word)
            if query is not None:
                query_posts = []
                post = Post.objects.all()
                tag_list = []
                for a_post in post:
                    jd = json.decoder.JSONDecoder()
                    tag_list = jd.decode(a_post.tags)
                    for w in tag_list:
                        print(w)
                        for i in range(len(query)):
                            print(query[i])
                            if query[i] in w or w in query[i]:
                                print("matched")
                                if a_post not in query_posts:
                                    query_posts.append(a_post)
                                    break
                if len(query_posts) == 0:
                    message = "No matching tag is found"
                    form = PostForm()
                    return render(request, 'Instagram/user_profile.html',
                                  {'user': user, 'post_form': form, 'message': message})
                else:
                    form = PostForm()
                    return render(request, 'Instagram/user_profile.html',
                                  {'user': user, 'post_form': form, 'query_posts': query_posts,
                                   'query_posts_count': len(query_posts)})
    form = PostForm
    return render(request, 'Instagram/user_profile.html', {'user': user, 'post_form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserInfo.objects.get(username=username, password=password)
                user.is_active = True
                user.save()
                return HttpResponseRedirect(reverse('user_profile', args=[user.id]))
            except:
                form = LoginForm()
                message = "User doesn't exist"
                return render(request, 'Instagram/login.html', {'form': form, 'message': message})
    form = LoginForm()
    return render(request, 'Instagram/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            obj = UserInfo()
            obj.name = form.cleaned_data['name']
            obj.username = form.cleaned_data['username']
            obj.password = form.cleaned_data['password']
            obj.save()
            form = LoginForm()
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'Instagram/register.html', {'form': form})


def post(request, id, post_id):
    user = UserInfo.objects.get(id=id)
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        tags = request.POST.getlist('checks[]')
        return render(request, 'Instagram/post.html', {'post': post, 'user': user, 'tags': tags})
    else:
        jsonDec = json.decoder.JSONDecoder()
        tags = jsonDec.decode(post.tags)
    return render(request, 'Instagram/post.html', {'post': post, 'user': user, 'tags': tags})


def user_tags(request, id, post_id):
    user = UserInfo.objects.get(id=id)
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        tag_text = request.POST.get('user_tags')
        tag_s = []
        words = tag_text.split()
        for w in words:
            tag_s.append(w)
        jsonDec = json.decoder.JSONDecoder()
        for x in jsonDec.decode(post.tags):
            tag_s.append(x)
        post.tags = json.dumps(tag_s)
        post.save()
        return HttpResponseRedirect(reverse('post', args=[user.id, post.id]))


def like(request, id, post_id):
    user = UserInfo.objects.get(id=id)
    post = Post.objects.get(id=post_id)
    post.likes = post.likes + 1
    post.save()
    return HttpResponseRedirect(reverse('post', args=[user.id, post.id]))


def post_user_profile(request, id, post_user_id):
    post_user = UserInfo.objects.get(id=post_user_id)
    user = UserInfo.objects.get(id=id)
    return render(request, 'Instagram/post_user_profile.html', {'user': user, 'post_user': post_user})
