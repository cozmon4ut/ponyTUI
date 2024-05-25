"""This file handles displaying the image"""
import requests
import booru_api
import webbrowser
import subprocess
import os
import platform
     
def getImg():
    # Grab the image
    img, extension, post_info = booru_api.fetch()
    if not img:
        raise ValueError("Image fetch failed from API.") 

    r = requests.get(img)
    if r.status_code == 200:
        filename = "pony" + extension
        with open(filename, "wb") as f:
            f.write(r.content)
    
    return post_info

def openInBrowser(link):
    webbrowser.open(link, new=0, autoraise=True)

def openVideo(file_path):
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":
            subprocess.Popen(['open', file_path]) 
        else:
            subprocess.Popen(['xdg-open', file_path])
    except Exception as e:
        print(f"Error: {e}") 