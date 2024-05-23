from customtkinter import CTkFrame, CTkButton
from components.options import Options
from components.additional_options import AdditionalOptions
from components.table import Table
from CTkMessagebox import CTkMessagebox


class MainView(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.options = Options(master=self)
        self.options.grid(row=0, column=0, sticky="nws", padx=10, pady=10)

        self.cross_sections = AdditionalOptions(master=self)
        self.cross_sections.grid(row=0, column=1, sticky="nwe", padx=(0, 10), pady=10)

        self.button_reset = CTkButton(self, text="Скинути налаштування", width=110)
        self.button_reset.grid(row = 0, column = 1, sticky="wes", padx=(0, 10), pady=(0, 10))
        
        self.table = Table(master=self)
        self.table.grid(row=1, column=0, columnspan=2, sticky="nwse", padx=10, pady=(0, 10))

    def show_error(self, message: str):
        CTkMessagebox(title="Помилка", message=message, icon="cancel", justify="center")
    
    def ask_question(self, message: str):
        msg = CTkMessagebox(title="Впевнені?", message=message,
                            icon="question", option_2="Так", option_1="Ні")
        response = msg.get()
        
        if response == "Так":
            return True
        else:
            return False
        