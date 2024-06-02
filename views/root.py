from customtkinter import CTk
from components.center_window import center_window

import sys, os
def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Root(CTk):
    def __init__(self):
        super().__init__()

        self.width = 1030
        self.height = 645
        center_window(self, self.width, self.height)
        self.resizable(width=False, height=False)
        self.title("Розрахунок об'ємів земляних робіт")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.iconbitmap(resource(os.path.join("components", "icon.ico")))
