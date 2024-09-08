# ponyTUI
Ponies in the terminal.
![image](https://github.com/cozmon4ut/ponyTUI/assets/121418834/31552469-27c3-45d2-8e79-7ba0f0b921d5)

# Info
This is a TUI program which uses the derpibooru API, [Textual](https://textual.textualize.io/), [requests](https://requests.readthedocs.io/en/latest/), [Rich](https://rich.readthedocs.io/en/stable/style.html), [Rich Pixels](https://github.com/darrenburns/rich-pixels), and [Pillow](https://pillow.readthedocs.io/en/stable/) to display pictures of characters from My Little Pony in a terminal; Additionally, it displays information about the post of which it originated from on derpibooru. By default, the character selected is random, but the user can edit the search parameters.

# Compatibility
Currently, this program is based around Linux. It is tested and working on Windows using the Windows Terminal, but has not been tested on Mac.
# Hotkey/Command Usage
**D** - Toggles dark mode. <br />
**Space** - Downloads a pony to display. <br />
**C** - Clears the screen. <br />
**E** - Opens a menu to edit the search term. <br />
**P** - Opens the link to the image in your default web browser. <br />
**R** - Open webm in your default media player. <br /> 

# Script Installation (Most Linux Distros)
A bash script is included which builds the package automatically:

```
chmod +x install.sh
./install.sh
```
<br />

**This installs the script system-wide with pip, which can rarely lead to issues.**

# Manual Installation

Clone the repo:

```
git clone https://github.com/cozmon4ut/ponyTUI
```
<br />

Go into the source directory and create a virtual environment: 

```
python -m venv venv
```

Install the required dependencies:

```
pip install textual rich rich_pixels Pillow requests build
```

Go back to the root directory and build the program: 

```
cd ..
python -m build
```

If you'd like to contain the program to a venv, install it normally:

```
pip install dist/ponytui-0.1-py3-none-any.wh1
```

If you'd like to run it system-wide, deactivate the virtual environment and install it as a super user:

```
deactivate
sudo pip install dist/ponytui-0.1-py3-none-any.wh1 --break-system-packages
```





# Roadmap
I am currently a full-time student who's only been programming for about 2 years, and will not be holding myself terribly accountable to flesh out this hobby project. However, these are additions planned: </br >


- [ ] 1. More robust error handling
   - This program is currently prone to crashes due to being in its infancy. </br>
- [x] 2. Package the program 
- [ ] 3. Kitty term + (when released,) native Textual image support 
- [ ] 4. Favorites, more menus to adjust settings
- [ ] 5. API optimizations
- [ ] 6. Support for posting to derpibooru
