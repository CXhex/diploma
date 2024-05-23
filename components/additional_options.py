from customtkinter import CTkFrame, CTkLabel, StringVar, CTkEntry, CTkCheckBox
from re import fullmatch

class AdditionalOptions(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = CTkLabel(master=self, text="Налаштування укосів", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=(10, 0))
        
        #Використання типових поперечників
        self.label_cross_sections = CTkLabel(self, text="Використовувати типові показники укосів", fg_color="transparent")
        self.label_cross_sections.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.checkbox_cross_sections = CTkCheckBox(self, text="", onvalue="1", offvalue="0", border_width=2)
        self.checkbox_cross_sections.grid(row=1, column=0, sticky="e", padx=(0,60), pady=10)
        
        #показники укосу земляного полотна
        self.lable_slope_index_until_6 = CTkLabel(master=self, text="Показник укосу земляного полотна при висоті насипу до 6 м")
        self.lable_slope_index_until_6.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")
        
        self.entry_slope_index_until_6 = CTkEntry(master=self, width=50, justify="center", fg_color="transparent", border_color='gray')
        self.entry_slope_index_until_6.grid(row=2, column=1, pady=(0, 10), padx=(0, 10))
        
        self.lable_slope_index_from_6_to_12 = CTkLabel(master=self, text="Показник укосу земляного полотна при висоті насипу від  6 до 12 м")
        self.lable_slope_index_from_6_to_12.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="w")
        
        self.entry_slope_index_from_6_to_12 = CTkEntry(master=self, width=50, justify="center", fg_color="transparent", border_color='gray')
        self.entry_slope_index_from_6_to_12.grid(row=3, column=1, pady=(0, 10), padx=(0, 10))
        
        self.lable_slope_index_from_12_to_18 = CTkLabel(master=self, text="Показник укосу земляного полотна при висоті насипу від  12 до 18 м")
        self.lable_slope_index_from_12_to_18.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="w")
        
        self.entry_slope_index_from_12_to_18 = CTkEntry(master=self, width=50, justify="center", fg_color="transparent", border_color='gray')
        self.entry_slope_index_from_12_to_18.grid(row=4, column=1, pady=(0, 10), padx=(0, 10))
        
        self.entry_list = [self.entry_slope_index_until_6, self.entry_slope_index_from_6_to_12, self.entry_slope_index_from_12_to_18]

        vcmd = (self.register(self.validate), '%P')
        
        for entry in self.entry_list:
            entry.configure(validate='key', validatecommand=vcmd)
        
    def validate(self, value):
        pattern = r'\d{,3}\.?\d{,2}'
        if fullmatch(pattern, value) is None:
            return False
        return True
        
    def enable_editing(self):
        for entry in self.entry_list:
            entry.configure(state="normal")
            
    def disable_editing(self):
        for entry in self.entry_list:
            entry.configure(state="disable")
        
    def set_ctgs(self, ctgs: list):
        self.ctgs = ctgs
        self.StringVar_ctgs = [StringVar(self, ctg) for ctg in self.ctgs]
        
        for ctg, entry in zip(self.StringVar_ctgs, self.entry_list):
            entry.configure(textvariable=ctg)

    def get_ctgs(self) -> list|None:
        str_list = [s.get() for s in self.StringVar_ctgs]
        if "" in str_list:
            return None
        return [float(s) for s in str_list]
    
    def set_check_var_cross_sections(self, check_var_cross_sections: bool):
        self.check_var_cross_sections = StringVar(value=check_var_cross_sections)
        self.checkbox_cross_sections.configure(variable=self.check_var_cross_sections)
        if check_var_cross_sections:
            self.disable_editing()
        else:
            self.enable_editing()

    def get_check_var_cross_sections(self) -> bool:
        return bool(int(self.checkbox_cross_sections.get()))
    