from customtkinter import CTkFrame, CTkButton

class Buttons(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.button_copy = CTkButton(self, text="Скопіювати", width=110)
        self.button_copy.grid(row = 0, column = 1, pady=(0, 10))
        
        self.button_calculate = CTkButton(self, text="Розрахувати", width=110)
        self.button_calculate.grid(row = 1, column = 1, pady=(0, 10))
        
       
        