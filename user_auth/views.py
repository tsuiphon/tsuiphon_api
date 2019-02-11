from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth


@login_required
def top_page(request):
    user_auth = UserSocialAuth.objects.get(user_id=request.user.id)
    print('access_token:%s' % user_auth.access_token['oauth_token'])
    print('access_token_secret:%s' % user_auth.access_token['oauth_token_secret'])
    return render(request, 'create-talk-room-page.html', {'user_name': user_auth.user.username})
@login_required
def talk_page(request):
    user_auth = UserSocialAuth.objects.get(user_id=request.user.id)
    return render(request, 'talk-page.html', {'user_name': user_auth.user.username})
