from typing import TypedDict

from .root import Root
from .main_frame import MainView
from CTkMessagebox import CTkMessagebox


class Frames(TypedDict):
    main: MainView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}
        self._add_frame(MainView, "main")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def start_mainloop(self) -> None:
        self.root.mainloop()

    def show_error(self, message: str):
        CTkMessagebox(title="Помилка", message=message, icon="cancel", justify="center", sound=True)
    
    def ask_question(self, message: str):
        msg = CTkMessagebox(title="Впевнені?", message=message,
                            icon="question", option_2="Так", option_1="Ні")
        response = msg.get()
        
        if response == "Так":
            return True
        else:
            return False
        