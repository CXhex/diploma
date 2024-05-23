from models.main import Model
from views.main import View


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        
        self.view.frames['main'].options.set_entry_number_of_elements_text_var(self.model.settings.get_number_of_elements())
        self.view.frames['main'].options.set_optionmenu_list(self.model.settings.get_list_of_work_types(), self.model.settings.get_type_of_works())
        self.view.frames['main'].options.set_check_var_obliquity(self.model.settings.get_obliquity())
        
        self.view.frames['main'].cross_sections.set_check_var_cross_sections(self.model.settings.get_cross_sections())
        self.view.frames['main'].cross_sections.set_ctgs(self.model.settings.get_indicators_of_subgrade_slope())
        
        self.view.frames['main'].table.set_table_headers(self.model.table_data.get_table_headers())
        self.view.frames['main'].table.set_table_data(self.model.table_data.get_table_data())
        self.view.frames['main'].table.frame_info.info_display()
        
        if self.model.settings.get_type_of_works() == "залізниць":
            self.view.frames['main'].options.display_number_of_tracks()
            self.view.frames['main'].options.set_number_of_tracks(self.model.settings.get_number_of_tracks(), self.model.settings.get_track())
        elif self.model.settings.get_type_of_works() == "автомобільних доріг":
            self.view.frames['main'].options.hide_number_of_tracks()
        
        self.view.frames['main'].options.menu_number_of_tracks.configure(command=self.set_number_of_tracks)
        self.view.frames['main'].options.optionmenu.configure(command=self.change_type_of_works)
        self.view.frames['main'].options.set_width_main_field(self.model.settings.get_width_main_field())
        
        self.view.frames['main'].options.entry_number_of_elements.bind("<Return>", command=self.set_number_of_elements)
        self.view.frames['main'].options.set_number_of_elements_button.configure(command=self.set_number_of_elements)
        self.view.frames['main'].options.checkbox_obliquity.configure(command=self.set_obliquity)
        
        self.view.frames['main'].table.buttons_frame.button_calculate.configure(command=self.calculate)
        self.view.frames['main'].table.buttons_frame.button_copy.configure(command=self.copy)
        
        self.view.frames['main'].cross_sections.checkbox_cross_sections.configure(command=self.set_check_var_cross_sections)
        
        
    def change_type_of_works(self, event=None):
        self.view.frames['main'].focus()
        self.model.settings.set_type_of_works(self.view.frames['main'].options.get_optionmenu_value())
        
        if self.model.settings.get_type_of_works() == "залізниць":
            self.view.frames['main'].options.display_number_of_tracks()
            self.view.frames['main'].options.set_number_of_tracks(self.model.settings.get_number_of_tracks(), self.model.settings.get_track())
        elif self.model.settings.get_type_of_works() == "автомобільних доріг":
            self.view.frames['main'].options.hide_number_of_tracks()
    
    def set_number_of_elements(self, event=None):
        if len(self.view.frames['main'].options.get_entry_number_of_elements()):
            number_of_elements = int(self.view.frames['main'].options.get_entry_number_of_elements())
            self.model.settings.set_number_of_elements(number_of_elements)
            self.model.table_data.update_table_data(self.model.settings.get_number_of_elements())
            self.view.frames['main'].table.set_table_data(self.model.table_data.get_table_data())
            self.view.frames['main'].focus()
        else:
            self.view.frames['main'].show_error("Введіть кількість елементів!")
            
    def set_check_var_cross_sections(self):
        self.view.frames['main'].focus()
        check = self.view.frames['main'].cross_sections.get_check_var_cross_sections()
        if check:
            self.model.settings.set_indicators_of_subgrade_slope()
            self.view.frames['main'].cross_sections.set_ctgs(self.model.settings.get_indicators_of_subgrade_slope())
            self.view.frames['main'].cross_sections.disable_editing()
        else:
            self.view.frames['main'].cross_sections.enable_editing()
            
    def set_obliquity(self):
        self.view.frames['main'].focus()
        check = self.view.frames['main'].options.get_check_var_obliquity()
        self.model.table_data.headers_update(check)
        self.view.frames['main'].table.set_table_headers(self.model.table_data.get_table_headers())
        self.view.frames['main'].table.set_table_data(self.model.table_data.get_table_data())
        
    #кількість колій
    def set_number_of_tracks(self, event=None):
        self.view.frames['main'].focus()
        self.model.settings.set_track(self.view.frames['main'].options.get_track())
        
    def calculate(self):
        self.view.frames['main'].focus()
        
        table_data = self.view.frames['main'].table.get_table_data()
        if isinstance(table_data, ValueError):
            table_data =str(table_data)
            if len(table_data) > 60:
                table_data = table_data[:60] + "...'"
            self.view.frames['main'].show_error(f"Перевірте введені дані!\n{table_data}")
            return None
        self.model.table_data.set_table_data()
        self.model.table_data.autofill_table_data()
        
        indicators_of_subgrade_slope = self.view.frames['main'].cross_sections.get_ctgs()
        if indicators_of_subgrade_slope is None:
            self.view.frames['main'].show_error("Введіть показники укосів!")
            return None
        
        self.model.settings.set_indicators_of_subgrade_slope(indicators_of_subgrade_slope)
        
        main_field = self.view.frames['main'].options.get_width_main_field()
        if main_field is None:
            self.view.frames['main'].show_error("Введіть ширину основного поля!")
            return None
        
        self.model.settings.set_width_main_field(main_field)
        self.model.set_calculate()
        self.model.calculate.calculate()
        self.model.table_data.set_table_info(self.model.calculate.calculate_info())
        self.view.frames['main'].table.frame_info.set_table_info(self.model.table_data.get_table_info())
        self.view.frames['main'].table.frame_info.info_display()
        self.view.frames['main'].table.set_table_data(self.model.table_data.get_table_data())
    
    def copy(self):
        self.model.copy_table(self.view.frames['main'].table.frame_info.get_table_info())

    def start(self) -> None:
        self.view.start_mainloop()
