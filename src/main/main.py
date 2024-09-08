import tui
from params import firstRun
from os import path 


def main():
    app =  tui.ponyTUI()
    if path.isfile('params.json'):
        app.run()
    
    else:
        firstRun()
        app.run()

if __name__ == "__main__":
    main()

