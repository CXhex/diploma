from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu, CTkCheckBox, CTkEntry, CTkButton, StringVar
from re import fullmatch


class Options(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = CTkLabel(master=self, text="Основні налаштування", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, sticky="n", pady=(10, 0))
        
        #Розрахунок об'єму земляних робіт
        self.label_formula_choice = CTkLabel(self, text="Розрахунок об'єму земляних робіт", fg_color="transparent")
        self.label_formula_choice.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.optionmenu = CTkOptionMenu(self, width=170)
        self.optionmenu.grid(row=1, column=1, sticky="w", padx=(0, 10))

        #Враховувати косогорність місцевості
        self.label_obliquity = CTkLabel(self, text="Враховувати косогорність місцевості", fg_color="transparent")
        self.label_obliquity.grid(row=3, column=0, padx=10, pady=(0,10), sticky="w")
        self.checkbox_obliquity = CTkCheckBox(self, text="", onvalue="1", offvalue="0", border_width=2)
        self.checkbox_obliquity.grid(row=3, column=1, sticky="w", pady=(0, 10))
        
        #Кількість елементів
        self.label_obliquity = CTkLabel(self, text="Кількість елементів", fg_color="transparent")
        self.label_obliquity.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")
        self.entry_number_of_elements_text_var = StringVar()
        self.entry_number_of_elements = CTkEntry(self, width=50, justify="center", fg_color="transparent", border_color='gray', textvariable=self.entry_number_of_elements_text_var)

        validate_number = (self.register(self.validate_number_of_elements),'%P')
        self.entry_number_of_elements.configure(validate='key', validatecommand=validate_number)
        
        self.entry_number_of_elements.grid(row=2, column=1, sticky="w", pady=(0, 10))
        
        self.set_number_of_elements_button = CTkButton(self, text="встановити", width=110)
        self.set_number_of_elements_button.grid(row=2, column=1, sticky="e", padx=(0, 10), pady=(0, 10))

        #ширина основної площадки земляного полотна
        self.lable_width_main_field = CTkLabel(self, text="Ширина основної площадки земляного полотна", fg_color="transparent")
        self.lable_width_main_field.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="w")
        
        self.entry_width_main_field_text_var = StringVar()
        self.entry_width_main_field = CTkEntry(self, width=50, justify="center", fg_color="transparent", border_color='gray', textvariable=self.entry_width_main_field_text_var)
        self.entry_width_main_field.grid(row=4, column=1, sticky="w", pady=(0, 10))
        validate_width = (self.register(self.validate_width), '%P')
        self.entry_width_main_field.configure(validate='key', validatecommand=validate_width)
        
        #Кількість колій
        self.label_number_of_tracks = CTkLabel(self, text="Кількість колій", fg_color="transparent")
        self.label_number_of_tracks.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")
        self.menu_number_of_tracks = CTkOptionMenu(self, width=170)
        self.menu_number_of_tracks.grid(row=5, column=1, sticky="w", padx=(0, 10), pady=(0, 10))
        
    def validate_number_of_elements(self, value):
        pattern = r'\d{,3}'
        if fullmatch(pattern, value) is None:
            return False
        return True
    
    def validate_width(self, value):
        pattern = r'\d{,3}\.?\d{,2}'
        if fullmatch(pattern, value) is None:
            return False
        return True
    
    def set_width_main_field(self, width_main_field: str):
        self.entry_width_main_field_text_var.set(width_main_field)
        
    def get_width_main_field(self) -> str:
        try:
            return float(self.entry_width_main_field_text_var.get())
        except ValueError:
            return None
    
    def set_entry_number_of_elements_text_var(self, number_of_elements: str):
        self.entry_number_of_elements_text_var.set(number_of_elements)

    def get_entry_number_of_elements(self) -> str:
        return self.entry_number_of_elements_text_var.get()

    def set_optionmenu_list(self, optionmenu: list, selected_option: str):
        self.optionmenu.configure(values=optionmenu)
        self.optionmenu.set(selected_option)
        
    def get_optionmenu_value(self) -> str:
        return self.optionmenu.get()
    
    #кількість колій  
    def set_number_of_tracks(self, number_of_tracks: list, selected_number_of_tracks: str):
        number_of_tracks = [str(i) for i in number_of_tracks]
        self.menu_number_of_tracks.configure(values=number_of_tracks)
        self.menu_number_of_tracks.set(selected_number_of_tracks)
        
    def get_track(self) -> str:
        return self.menu_number_of_tracks.get()
        
    def display_number_of_tracks(self):
        self.label_number_of_tracks.configure(text="Кількість колій")
        self.menu_number_of_tracks.grid()

    def hide_number_of_tracks(self):
        self.label_number_of_tracks.configure(text="")
        self.menu_number_of_tracks.grid_remove()

    def set_check_var_obliquity(self, check_var_obliquity: bool):
        self.check_var_obliquity = StringVar(value=check_var_obliquity)
        self.checkbox_obliquity.configure(variable=self.check_var_obliquity)
    
    def get_check_var_obliquity(self) -> bool:
        return bool(int(self.check_var_obliquity.get()))
    