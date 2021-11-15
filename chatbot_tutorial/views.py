
import random
import datetime

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

from .models import BotPost
from django.contrib.auth.models import User
from .models import BotPost
from django.db.models import Count, query




@login_required(login_url='login')
def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message, user):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    current_time = datetime.datetime.now()
    if user.is_authenticated:
        BotPost.objects.create(user_id = user, title = message['text'], date_added = current_time)

    return result_message


def login_view(request):
    if request.user.is_authenticated:
        return redirect('chat')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            messages.error(request, "Incorrect username and / or password.")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_request(request):
    logout(request)
    return redirect("login")

def user_list(request):
    
    details = User.objects.values('username').annotate(num_of_calls=Count('user_id'))
    context = {
        'details' : details
    }
    return render(request, 'user_list.html', context)