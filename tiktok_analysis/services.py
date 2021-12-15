from TikTokApi import TikTokApi
from enum import Enum
import random
import string
verify = "verify_755352e33a1c44835827311a4e2b43f3"
class TiktokError(Enum):
    HASH_TAG_NOT_CORRECT = 1
    USERNAME_NOT_CORRECT = 2


class TiktokService:
    def __init__(self, *args, **kwargs):
        did="".join(random.choice(string.digits) for num in range(19))
        self.api = TikTokApi.get_instance(custom_verifyFp=verify,did=did)

    def verify_user(self, username: str, hash_tag: str) -> dict:
        if "www." in username:
            username = username.split("@")[-1]
        try:
            user = self.api.get_user(username=username)
            if user and hash_tag in user["seoProps"]["metaParams"]["description"]:
                return user["userInfo"]
        except: 
            return None
        return None

    def get_user(self, username: str) -> dict:
        if "www." in username:
            username = username.split("@")[-1]
        try:
            user = self.api.get_user(username=username)
            if user:
                return user["userInfo"]
        except: 
            return None
        return None
    def get_list_post(self, username: str) -> dict:
        if "www." in username:
            username = username.split("@")[-1]
        try:
            user = self.api.get_user(username=username)
            if user:
                return user["items"]
        except: 
            return None
        return None

    def get_summary_post(self, url: str, hashtags: str, username=str):
        data = self.api.get_tiktok_by_url(url=url)
        if data:
            # get description of post
            post_description = data["itemInfo"]["itemStruct"]["desc"]
            # check that this post containt all hashtags
            # for hash_tag in hashtags.split("#"):
            #     hash_tag = hash_tag.replace(" ", "")
            #     if hash_tag not in post_description:
            #         return TiktokError.HASH_TAG_NOT_CORRECT
            
            post_author_nickname = data["itemInfo"]["itemStruct"]["author"]["uniqueId"]
            # if username and post_author_nickname.lower() != username.lower():
            #     return TiktokError.USERNAME_NOT_CORRECT
            return data["itemInfo"]["itemStruct"]["stats"]
        return 
