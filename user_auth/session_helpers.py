from .api_helpers import *
from social_django.models import UserSocialAuth
from .models import *
import time
import random
import hashlib

def before_action(request):
    user_auth = UserSocialAuth.objects.get(user_id=request.user.id)
    if not 'user_name' in request.session.keys():
        request.session["user_name"] = user_auth.user.username
    if not 'uid' in request.session.keys():
        request.session["uid"] = user_auth.uid
    if not 'avatar_url' in request.session.keys():
        request.session["avatar_url"] = get_my_avatar_url_from_user_auth(user_auth)
    if not 'access_token' in request.session.keys():
        request.session["access_token"] = user_auth.access_token['oauth_token']
    if not 'acess_secret' in request.session.keys():
        request.session["access_secret"] = user_auth.access_token['oauth_token_secret']


def enter_room(user_id, talk_id, provider):
    now = int(time.time())
    wait_rooms = Room.objects.filter(talk_id__exact=talk_id, is_wait=True)
    while wait_rooms:
        booking_room = random.choice(wait_rooms)
        booking_room.is_wait = False
        booking_room.user2_uid=user_id
        booking_room.user2_provider=provider
        booking_room.updated_at = now
        booking_room.save()
        booked_rooms = Room.objects.filter(id=booking_room.id,
                                           talk_id__exact=talk_id,
                                           user2_uid=user_id,
                                           user2_provider=provider)# 念の為確認する
        if booked_rooms:
            room = booked_rooms[0]
            break
        wait_rooms = Room.objects.filter(talk_id__exact=talk_id, is_wait=True)
    else:
        h = hashlib.sha256()
        h.update(user_id.encode("utf-8"))
        h.update(str(now).encode("utf-8"))
        h.update(str(random.randint(0,1000000000000000000000000)).encode("utf-8"))
        room_password = str(h.hexdigest())
        room = Room(
            password=room_password,
            talk_id=talk_id,
            user1_uid=user_id,
            user1_provider=provider,
            created_at=now,
            updated_at=now
        )
        room.save()
    return room
