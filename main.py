import tui
from setup import firstRun
from os import path 


if __name__ == "__main__":
    app =  tui.ponyTUI()
    if path.isfile('params.json'):
        app.run()
    
    else:
        firstRun()
        app.run()
