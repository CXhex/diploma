from customtkinter import CTk
from components.center_window import center_window

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
