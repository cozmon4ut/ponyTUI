
from textual import on
from textual.app import App, ComposeResult, RenderResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Static
from textual.containers import Container
from rich_pixels import Pixels
from rich.text import Text
import PIL
import display
import json
import os
import threading

# TODO
    # Modularize this into more files, codebase is getting rather large
    # Backend
        # try going for API interaction optimizations

    # Frontend
        # favorites? a bit overly ambitious
        # baked-in textual hyperlinks instead of
        # relying on kitty
    
    # Opts to look into
        # https://textual.textualize.io/guide/workers/





"""Search term parameter editing screen"""


#class Settings(Screen)




class EditParams(Screen):
    
    # Load parameters
    def compose(self) -> ComposeResult:  
        with open('params.json') as f:
            params = json.load(f)
        
        yield Header()
        yield Footer()
     
        yield Input(placeholder=f"current search: {params['q']}", type="text")
    
    # Add title, subtitle on start 
    def on_mount(self) -> None: 
            self.title = "Edit Parameters"
            self.sub_title = "Press Enter for no edit"
    
    # Accept input for edits 
    @on(Input.Submitted) 
    def accept_edit(self) -> None:
        input = self.query_one(Input)
        query = input.value
        
        if query == "":
            self.app.pop_screen()
        else:
            
            with open('params.json') as f:
                params = json.load(f)
        
            params['q'] = query
            
            with open('params.json', 'w') as f:
                json.dump(params, f, indent=4)    
             
            self.app.pop_screen()


class ShowPony(Container):
    DEFAULT_CSS = """ 
    ShowPony {
        height: 1fr;
        width: 1fr;
        border: solid purple; 
    }
    """ 
    def on_mount(self) -> None:
        self.auto_refresh = 1 / 1


    
    
    def render_image(self, filename) -> Pixels:
        widget_width = self.size.width 
        widget_height = self.size.height * 2
         
        
        
        
        with PIL.Image.open(filename) as img:
            img = img.resize((widget_width, widget_height), PIL.Image.Resampling.LANCZOS)
            img.save(filename)
        
        return Pixels.from_image_path(filename)
    
    
    
    def render(self) -> RenderResult:
        if not any(filename.startswith("pony") for filename in os.listdir(".")):
            return Text("")        
        else:
            for file in os.listdir("."): 
                filename = os.path.basename(file) 
                if filename.startswith("pony"): # add UnidentifiedImageError handling 
                    return self.render_image(filename)

class PostInfo(Static):
    
    def __init__(self, post_info=None, **kwargs):
        super().__init__(**kwargs)
        self.post_info = post_info
    
    def on_mount(self) -> None:
        self.auto_refresh = 1 / 1
    
    def render(self) -> RenderResult:
        if self.post_info:
            post_info = (
                f"Uploader: {self.post_info.get('uploader', 'N/A')}\n\n"
                f"Source: {', '.join(self.post_info.get('source', 'N/A'))}\n\n"
                f"Tags: {', '.join(self.post_info.get('tags', []))}\n\n"
                f"Description: {self.post_info.get('description', 'N/A')}\n\n"
                f"""{self.post_info.get('url', 'N/A')}\n"""
            )
            return Text(post_info)
        return Text("")

class ponyTUI(App):

    CSS_PATH = "tui.tcss"
    
    BINDINGS = [("d", "toggle_dark", "dark mode"), 
                ("space", "pony_me", "pony"), 
                ("c", "clear_screen", "clear"),
                ("e", "edit_params", "edit search"),
                ("p", "open_image", "open")]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ShowPony()
        yield PostInfo(classes="box") 
    
    def on_mount(self) -> None:
        self.title = "Pony TUI"
        self.sub_title = "PONIES!"     
        
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
    
    def action_pony_me(self) -> None:
        for file in os.listdir("."):
            filename = os.path.basename(file)
            if file.startswith("pony"):
                os.remove(filename)
                
        display_box = self.query_one(ShowPony)
        info_box = self.query_one(PostInfo)
        display_box.loading = True

        def get_image() -> None:
            try:
                post_info = display.getImg()
                display_box.render()  # Ensure the display box is rendered
                info_box.post_info = post_info
            
            except Exception as e:
                print(f"Error fetching image: {e}")  # Log any errors for debugging
            
            finally:
                display_box.loading = False

        t1 = threading.Thread(target=get_image)
        t1.start()
    
    def action_open_image(self) -> None:
        with open("post_info.json", 'r') as f:
            data = json.load(f)
            url = data.get('url')
            display.openInBrowser(url)
             
    def action_clear_screen(self) -> None:
        for file in os.listdir("."):
            filename = os.path.basename(file)
            if file.startswith("pony"):
                os.remove(filename)
        
        post_info = self.query_one(PostInfo)
        post_info.post_info = None

    def action_edit_params(self) -> None:
        self.push_screen(EditParams())

