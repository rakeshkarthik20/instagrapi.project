from instagrapi  import Client 
from instagrapi.types import Usertag 
import config 
cl = Client()
cl.login(config.username,config.password)
user = cl.user_info_by_username("rakesh_karthik20")
media = cl.clip_upload (
path ="",
caption = "rakesh picture",
usertags = [Usertag(user = user, x = 0.5,y=0.5)],
extra_data = {
"custom_accessibility_caption" : "alt text example ",
"like_and_view_counts_disabled" : False,
" disable_comments" : False })