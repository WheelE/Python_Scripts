import os
from dotenv import load_dotenv
import re
import psutil


if "chome.exe" in (p.name() for p in psutil.process_iter()):
          os.system("taskkill /im chrome.exe /f")
        

load_dotenv()

user_profile = os.getenv("USERPROFILE")
cache_path = user_profile +"\\AppData\Local\\Google\\Chrome\\User Data\\Default"
searchString = "Cookies"
for folder, subfolders, files in os.walk(cache_path):
    if folder != cache_path:
        for file in files:
            if re.search('Cook.',file):
                print("Cookies found at " + file)
                
                if os.path.isfile(file):
                     os.remove(file)
                else:
                       print("No Cookies Found")
            if re.search('Cach.+',folder):
                print("Cache folders found " + folder)
                for name in os.listdir(folder):
                     file = folder + "\\" + name
                if os.path.isfile(file):
                        os.remove(file)
