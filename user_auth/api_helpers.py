from requests_oauthlib import OAuth1Session
from django.conf import settings

endpoint = 'https://api.twitter.com/1.1/'
def get_user_profile(access_token,access_secret,user_id):
    api_key = settings.SOCIAL_AUTH_TWITTER_KEY
    api_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
    api = OAuth1Session(api_key, api_secret, access_token, access_secret)
    res = api.get("%s/users/show.json?user_id=%s" % (endpoint, user_id))
    return res.json()

def get_my_avatar_url_from_user_auth(user_auth):
    avatar_url = get_user_profile(user_auth.access_token['oauth_token'],
                     user_auth.access_token['oauth_token_secret'],
                     user_auth.uid)['profile_image_url']
    return avatar_url
