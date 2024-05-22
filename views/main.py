from typing import TypedDict

from .root import Root
from .main_frame import MainView


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
