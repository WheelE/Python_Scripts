import os
from dotenv import load_dotenv
load_dotenv()

user_profile = os.getenv("USERPROFILE")
cache_path = user_profile +'\\AppData\Local\\Google\\Chrome\\User Data\\Default'
searchString = "Cookies"
for folder, subfolders, files in os.walk(cache_path):
    if folder != cache_path:
        for file in files:
            if file == searchString:
                print("File found at " + os.path.join(folder, file))

 