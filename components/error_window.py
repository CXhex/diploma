from customtkinter import CTkToplevel, CTkLabel
from .center_window import center_window

class ErrorWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        center_window(self, width=500, height=100)
        self.resizable(width=False, height=False)
        if kwargs["text"] is not None:
            self.label = CTkLabel(self, text=kwargs["text"])
        else:
            self.label = CTkLabel(self, text="Помилка")
        self.label.pack(padx=20, pady=20)
        