from TikTokApi import TikTokApi
class TiktokService:
    def __init__(self, *args, **kwargs):
        self.api  = TikTokApi.get_instance()    
    def verify_user(self, username: str, hash_tag: str)-> dict:
        if "www." in username:
            username = username.split("@")[-1]
        user = self.api.get_user(username=username)
        if user and hash_tag in user["seoProps"]["metaParams"]["description"]:
                return user["userInfo"]
        return None
    
    
