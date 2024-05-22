from customtkinter import CTkFrame, CTkLabel


class TableInformation(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.table_info = ["Об'єм насипу Vн = __ тис.м.куб.", "Об'єм виїмки Vв = __ тис.м.куб.",
                           "Профільна кубатура V = __ тис.м.куб.", "Покілометровий об'єм - __ тис.м.куб./км.",
                           "Загальна довжина L = __ м."]

    def set_table_info(self, info: dict):
        self.table_info = [f"Об'єм насипу Vн = {info['embankment_volume']} тис.м.куб.", f"Об'єм виїмки Vв = {info['excavation_volume']} тис.м.куб.",
                           f"Профільна кубатура V = {info['profile_volume']} тис.м.куб.", f"Покілометровий об'єм - {info['per_kilometer_volume']} тис.м.куб./км.",
                           f"Загальна довжина L = {info['total_length']} м."]

    def get_table_info(self) -> list:
        return self.table_info

    def info_display(self):
        r = c = 0
       
        for child in self.winfo_children():
            child.destroy()
       
        for info in self.table_info:
            self.label = CTkLabel(master=self, text=info)
            self.label.grid(row=r, column=c, sticky="w", padx=(0,10), pady=(0,10))
            
            if c == 2:
                c = 0
                r += 1
            else:
                c += 1
