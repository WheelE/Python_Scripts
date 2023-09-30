import os
from dotenv import load_dotenv
import re

load_dotenv()

user_profile = os.getenv("USERPROFILE")
cache_path = user_profile +'\\AppData\Local\\Google\\Chrome\\User Data\\Default'
searchString = "Cookies"
for folder, subfolders, files in os.walk(cache_path):
    if folder != cache_path:
        for file in files:
            if re.search('Cook.+',file):
                os.remove(file)
                print("Cookies Cleared")
            else:
                print("No Cookies Found")
        
        if re.search('Cach.+',folder):
            print("Cache folders found " + folder)
            """
            for name in os.listdir(folder):
                file = folder + name
                if os.path.isfile(file):
                    os.remove(file)
                    """
