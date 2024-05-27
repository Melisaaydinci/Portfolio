from django.shortcuts import render,redirect
from music.models import Music
from user.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from user.form import LoginForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import json
from django.http import JsonResponse
import pandas as pd
from listening.models import MusicListening
from django.db.models import Q

def home_page(request):
    musics = Music.objects.all()[:18]
    if request.user.is_authenticated:
        user= CustomUser.objects.get(username= request.user.username)
        favorite_musics = user.favorites.all().values_list('id', flat=True)
    else:
        favorite_musics = []
    context={
        'musics':musics,
        'favorite_musics':favorite_musics,
    }
    return render(request,'index.html',context)

def music_page(request,music_id):
    only_music = Music.objects.get(id=music_id)
    video_id='8DQxBdHyGVg'
    if request.user.is_authenticated:
        user= CustomUser.objects.get(username= request.user.username)
        favorite_musics = user.favorites.all().values_list('id', flat=True)
        #Favorites.objects.filter(user=request.user).values_list('camp__slug', flat=True)
    else:
        favorite_musics = []
    print(only_music)
    context={
        'only_music':only_music,
        'video_id':video_id,
        'favorite_musics':favorite_musics
    }
    return render(request,'music_play.html',context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Başarılı giriş yapıldıktan sonra yönlendirme yapılabilir
                return redirect('home_page')
            else:
                form.add_error(None, "Kullanıcı adı veya şifre hatalı.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
 
def signup_page(request):   
    if request.method == 'POST':
        print("posta giriyorum")
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user özellikleri",user)
            auth_login(request, user)
            # Başarılı kayıt yapıldıktan sonra yönlendirme yapılabilir veya başka bir işlem gerçekleştirilebilir
            return redirect('home_page')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})
    

@login_required
def logout_page(request):
    logout(request)
    return redirect('home_page')


@login_required
def favorite_page(request):
    user= CustomUser.objects.get(username= request.user.username)
    favorite_musics = user.favorites.all()
    context={
        'favorite_musics':favorite_musics,
    }
    return render(request,'favorites.html',context=context)

@login_required
def profile_page(request):
    user= CustomUser.objects.get(username= request.user.username)
    context={
        'user':user,
    }
    return render(request,'profile.html',context=context)

@login_required
def add_or_remove_favorite(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body) 
        music_slug= data.get('music_slug')
        music = Music.objects.get(id=music_slug)
        user= CustomUser.objects.get(username= request.user.username)
        if music in user.favorites.all():
            user.favorites.remove(music)
            music.decrement_favorite_count()
            return JsonResponse({'status': 'removed'})
        else:
            user.favorites.add(music)
            music.increment_favorite_count()
            return JsonResponse({'status': 'added'})
    return JsonResponse({'status': 'error'})

def search_music(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        musics = Music.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))[:10]
        data = [{'id': music.id, 'text': music.title} for music in musics]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)

