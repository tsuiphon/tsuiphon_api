from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .session_helpers import *

@login_required
def top_page(request):
    before_action(request)
    render_params = {
        'user_name': request.session['user_name'],
        'avatar_url': request.session['avatar_url']
    }
    return render(request, 'create-talk-room-page.html', render_params)
@login_required
def talk_page(request):
    before_action(request)
    render_params = {
        'user_name': request.session['user_name'],
        'avatar_url': request.session['avatar_url']
    }
    return render(request, 'talk-page.html', render_params)
def room(request):# TODO:あとで外す
    room_key = "r4)bUzzaqUz&s2Ys1sAlmY"
    return render(request, 'room.html', {'room_key': room_key})
