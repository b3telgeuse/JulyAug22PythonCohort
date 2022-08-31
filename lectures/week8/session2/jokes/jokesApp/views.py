from django.shortcuts import render, redirect
from django.contrib import messages
from jokesApp.models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')

def login(request):
    emailUser = User.objects.filter(email = request.POST['email'])
    if emailUser:
        userLogin = emailUser[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'That Username or Email is not in our system, please register for an account')
    return redirect('/')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    # will only render the current user's jokes
    jokes = Joke.objects.filter(user_id=user)
    context = {
        'user': user,
        'jokes': jokes
    }
    return render(request, 'dashboard.html', context)

def jokAPI(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'jokeAPI.html', context)

def createJoke(request):
    Joke.objects.create(
        question = request.POST['question'],
        punchline = request.POST['punchline'],
        user = User.objects.get(id=request.session['user_id'])
    )
    messages.error(request, "Joke added to database")
    return redirect('/dashboard/')

def allUsers(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    users = User.objects.all().values()
    context = {
        'user': user,
        'users': users
    }
    return render(request, 'user.html', context)

def otherUser(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    jokes = Joke.objects.filter(user_id=user_id)
    context = {
        'user': user,
        'jokes': jokes
    }
    # Allows us to use the same html page to render other user's jokes based off the link
    return render(request, 'dashboard.html', context)