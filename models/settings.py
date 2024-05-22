class Settings:
    def __init__(self) -> None:
        self.number_of_elements = 15
        self.list_of_work_types = ["залізниць", "автомобільних доріг"]
        self.type_of_works = self.list_of_work_types[0]
        self.number_of_tracks = ["одна", "дві"]
        self.track = self.number_of_tracks[0]
        self.cross_sections = True
        self.obliquity = False
        self.indicators_of_subgrade_slope = [1.5, 1.75, 2]
        self.width_main_field = 7

    def set_width_main_field(self, width_main_field: int):
        self.width_main_field = width_main_field
        
    def get_width_main_field(self) -> int:
        return self.width_main_field

    def set_number_of_elements(self, number_of_elements: int):
        self.number_of_elements = number_of_elements

    def get_number_of_elements(self) -> int:
        return self.number_of_elements
    
    def set_list_of_work_types(self, list_of_work_types: list):
        self.list_of_work_types = list_of_work_types
        
    def get_list_of_work_types(self) -> list:
        return self.list_of_work_types
    
    def set_type_of_works(self, type_of_works: str):
        self.type_of_works = type_of_works
        
    def get_type_of_works(self) -> str:
        return self.type_of_works
    
    def set_track(self, track: str):
        self.track = track
        
    def get_track(self) -> str:
        return self.track
    
    def get_number_of_tracks(self) -> list:
        return self.number_of_tracks
    
    def set_cross_sections(self, cross_sections: bool):
        self.cross_sections = cross_sections
        
    def get_cross_sections(self) -> bool:
        return self.cross_sections
    
    def set_obliquity(self, obliquity: bool):
        self.obliquity = obliquity
        
    def get_obliquity(self) -> bool:
        return self.obliquity
    
    def set_indicators_of_subgrade_slope(self, indicators_of_subgrade_slope: list = [1.5, 1.75, 2]):
        self.indicators_of_subgrade_slope = indicators_of_subgrade_slope
        
    def get_indicators_of_subgrade_slope(self) -> list:
        return self.indicators_of_subgrade_slope
    