from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .session_helpers import *
import json

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
        'avatar_url': request.session['avatar_url'],
    }
    return render(request, 'talk-page.html', render_params)
def room(request):
    before_action(request)
    if "talk_id" in request.GET:
        talk_id = request.GET.get("talk_id")
    else:
        talk_id = "default"
    room = enter_room(request.session['uid'], talk_id, "twitter")
    while room.is_wait:
        room = Room.objects.filter(id=room.id)[0]
        time.sleep(3)
    if room.user1_uid != request.session['uid']:
        pair_user_profile = get_user_profile(request.session['access_token'],request.session['access_secret'],room.user1_uid)
    else:
        pair_user_profile = get_user_profile(request.session['access_token'],request.session['access_secret'],room.user2_uid)
    pair_avatar_url = pair_user_profile['profile_image_url'].replace("_normal","")#大きいサイズに変換するために_normalを消す
    pair_user_name = pair_user_profile['name']
    pair_screen_name = pair_user_profile['screen_name']
    data = {'room_password': room.password, 'pair_avatar_url': pair_avatar_url, 'pair_user_name': pair_user_name, 'pair_screen_name': pair_screen_name}
    json_str = json.dumps(data, ensure_ascii=False)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8')
    return response
