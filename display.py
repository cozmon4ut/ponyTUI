"""This file handles displaying the image"""
import requests
import booru_api
     
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

 