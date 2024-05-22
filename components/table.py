from customtkinter import CTkFrame
from tksheet import Sheet

from .table_information import TableInformation
from .buttons import Buttons


class Table(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Таблиця елементів
        self.sheet = Sheet(self,
                           header_height="2",
                           align="center",
                           show_dropdown_borders=0,
                           height=280,
                           width=990,
                           show_x_scrollbar=False,
                           empty_vertical=0,
                           empty_horizontal=0,
                           auto_resize_columns=True)

        self.sheet.enable_bindings()
        self.sheet.grid(row=0, column=0, columnspan=4,
                        sticky="we", padx=10, pady=10)

        self.frame_info = TableInformation(master=self, fg_color="transparent")
        self.frame_info.grid(row=1, column=0, columnspan=3,
                             sticky="w", padx=(10, 0), pady=(0, 0))

        self.buttons_frame = Buttons(master=self, fg_color="transparent")
        self.buttons_frame.grid(row=1, column=3, sticky="e", padx=(0, 10))

    def set_table_headers(self, headers: list):
        self.sheet.set_header_data(headers)
        
    def get_table_headers(self):
        return self.sheet.headers()
    
    def set_table_data(self, data: list):
        self.sheet.set_sheet_data(data)
        self.sheet.redraw()
        
    def get_table_data(self):
        data = self.sheet.get_sheet_data()
        data = [[float(c) for c in r]for r in data]
        return data
        