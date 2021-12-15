from facebook_scraper import get_profile, get_posts
import os
from django.conf import settings
def getInformationOfPost(url: str):
    cookie = os.path.join(settings.BASE_DIR, 'cookie.txt')
    posts = get_posts(post_urls=[url], cookies=cookie)
    post = next(posts)
    if post:
        return post
    return None

def getInformationOfUser(username: str):
    cookie = os.path.join(settings.BASE_DIR, 'cookie.txt')
    user = get_profile(account= username, cookies=cookie)
    if user:
        return user
    return None
