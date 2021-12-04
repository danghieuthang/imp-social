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