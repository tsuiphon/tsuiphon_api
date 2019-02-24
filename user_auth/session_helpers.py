from .api_helpers import *
from social_django.models import UserSocialAuth

def before_action(request):
    user_auth = UserSocialAuth.objects.get(user_id=request.user.id)
    if not 'user_name' in request.session.keys():
        request.session["user_name"] = user_auth.user.username
    if not 'avatar_url' in request.session.keys():
        request.session["avatar_url"] = get_user_avatar_url_from_user_auth(user_auth)