from .calculate_train import CalculateTrain


class Calculate():
    def __init__(self, type_of_works: str, b: float, track: str, ctgs: list, data: list):
        self.type_of_works = type_of_works
        self.ctgs = ctgs
        self.data = data
        self.b = b
        self.number_of_tracks = None
        self.set_number_of_tracks(track)

    def set_number_of_tracks(self, number_of_tracks: str):
        if number_of_tracks == "одна":
            self.number_of_tracks = 1
        elif number_of_tracks == "дві":
            self.number_of_tracks = 2
    
    def calculate(self):
        if self.type_of_works == "залізниць":
            for row in self.data:
                c = CalculateTrain(row, self.b, self.ctgs, self.number_of_tracks)
                res = c.calculate()
                row[-2] = res[0]
                row[-1] = res[1]
        elif self.type_of_works == "автомобільних доріг":
            pass

    def calculate_info(self) -> dict: 
        embankment_volume    = 0.0 # Об'єм насипу V
        excavation_volume    = 0.0 # Об'єм виїмки V
        profile_volume       = 0.0 # Профільна кубатура V
        total_length         = 0.0 # Загальна довжина L
        per_kilometer_volume = 0.0 # Покілометровий об'єм
        
        for row in self.data:
            total_length      += row[2]
            embankment_volume += row[-2]
            excavation_volume += row[-1]
        
        profile_volume = excavation_volume + embankment_volume
        if (profile_volume > 0):
            per_kilometer_volume = profile_volume * 1000 / total_length
            
        table_info = {
            "embankment_volume" : format_number(round(embankment_volume, 2)),  # Об'єм насипу V
            "excavation_volume" : format_number(round(excavation_volume, 2)),  # Об'єм виїмки V
            "profile_volume"    : format_number(round(profile_volume, 2)),     # Профільна кубатура V
            "total_length"      : format_number(round(total_length, 2)),       # Загальна довжина L
            "per_kilometer_volume" : format_number(round(per_kilometer_volume, 2)) # Покілометровий об'єм
        }   
        return table_info

def format_number(number):
    return str(number) if len(str(number)) <= 10 else "{:.2g}".format(number)
