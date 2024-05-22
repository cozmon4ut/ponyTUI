import requests
import json
from random import randint
from math import ceil
# TODO
    # cython? requests are slow
    # modularize, we need speed opts
    
    # all of these params, query settings,


API_ENDPOINT = "https://derpibooru.org/api/v1/json/search/images"


"""Load parameters"""
def loadData():
    with open('params.json') as f: params = json.load(f)
    return params


"""Do the initial API call to get total images"""
def initAPI(params):
    with open('params.json') as f: params = json.load(f)
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    return data['total']

"""Get count of pages for the search to randomly select"""
def getPageCount(data, params):
    image_num = data 
    page_count = ceil(image_num / params['per_page'])
    page_count = randint(0, page_count)
    params['page'] = page_count
     


# Get random pony image
def getPonies(params):
    
    # As far as I can tell, two requests have to be made
    # 1 for the page count, 1 for the actual search on 
    # a random page. Speed optimizations should be looked
    # into for this, since the two API calls depend on 
    # each other, which slows down obtaining the img.
    response = requests.get(API_ENDPOINT, params=params) 
    data = response.json()
    
    if response.status_code == 200:
        if data['images']:
            rand_i = randint(0, min(15, len(data['images'])) - 1)
            rand_image = data['images'][rand_i]
            img = rand_image['representations']['full']
            
            extension = "." + img.split('.')[-1]
            return rand_image, img, extension

def savePostInfo(post_info):
    with open('post_info.json', 'w') as f:
        json.dump(post_info, f, indent=4)


# get all data
def fetch():
    params = loadData()
    data = initAPI(params)
    getPageCount(data, params)
    rand_image, img, extension = getPonies(params)
    
    if rand_image:
        post_info = {
            'id': rand_image['id'],
            'uploader': rand_image['uploader'],
            'source': rand_image['source_urls'],
            'tags': rand_image['tags'],
            'description': rand_image['description'],
            'url': rand_image['representations']['full'] 
        }
        savePostInfo(post_info)
        return img, extension, post_info
    
    return None, None, None
