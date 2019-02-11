def get_user_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    url = response.get('profile_image_url', '').replace('_normal', '')
    print(url)
