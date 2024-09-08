import json

def makeParams(key=None):
    try:
        if key:
            params = {
                'key': key,
                'q': "*,safe,-animated,-video",
                'per_page': 15
            }
                            
        if not key:
            params = {
                'key': "NA",
                'q': "*,safe,-animated,-video",
                'per_page': 15
            }
            
        with open("params.json", 'w') as f:
            json.dump(params, f, indent=4)
            print("Created parameters JSON file..")
        
        empty_data = {}
        with open("post_info.json", 'w') as f:
            json.dump(empty_data, f)
            print("\nCreated an empty json file to store post information...")
    
    except Exception as e:
        print(f"Something went wrong with writing json: \n{e}") 
    
   

 
def firstRun():
    print("Welcome to PonyTUI!")
    print("\nIf you have a derpibooru account and you'd like to, you can enter your user API key.")
    
    while True:
        try:
            confirmation = input("\nWould you like to use an API key? This required to make adult searches.\n(y/n) \n> ")
            
            if confirmation == "yes" or confirmation == "y":
                API_KEY = str(input("\nPlease enter the key now. ")) 
                
                print("\nCreating a best-effort parameter config with API key...", end="")
                
                makeParams(key=API_KEY)
                print("✅", end="")
                
                break
              
            elif confirmation == "no" or confirmation == "n":
                print("Creating a best-effort parameter configuration...")
                makeParams()
                print("Done! ✅")
                break
        
            else:
                print("\nYou've chosen an invalid option. Please try again.")
                continue
        
        except ValueError:
            print("\nYou have entered some wrong value. Please try again.")
            continue 
     