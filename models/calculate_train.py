class CalculateTrain():
    def __init__(self, list: list, b: float, m: list, track: int):
        self.b  = b + list[3]    #b  - ширина основної площадки земляного полотна, м
        self.h1 = list[0]        #H1 – робоча відмітка на початку ділянки, м;
        self.h2 = list[1]        #H2 – робоча відмітка в кінці ділянки, м;
        self.l  = list[2]        #l  – довжина ділянки, м;
        
        if len(list) == 7:
            self.n = list[4]     #n  – показник укосу косогору;
        else:
            self.n = None
            
        self.m = m
        self.track = track
             
    #Розрахунок нижньої основи трапеції
    @staticmethod
    def calculate_bottom_side(b: float, h: float, ctg: float) -> float:
        a = b + h * (ctg * 2)
        return a

    #Розрахунок площі трапеції
    @staticmethod
    def calculate_area_trapezoid(a: float, b: float, h: float) -> float:
        area = (a + b) / 2 * h
        return area

    #Розрахунок об'єму трапеції
    @staticmethod
    def calculate_volume_trapezoid(start_area: float, end_area: float, l: float) -> float:
        volume = (start_area + end_area) / 2 * l
        return volume

    #Розрахунок сумми площ трапецій
    def calculate_sum_areas_trapezoids(self, height: float) -> float:
        i = 0
        sum_area = 0
        b = self.b
        while True:
            #Розрахунок виїмки
            if height < 0:
                h = abs(height)
                b += 2.2 * 2 
                a = self.calculate_bottom_side(b, h, self.m[0])
                sum_area += self.calculate_area_trapezoid(a, b, h)
                break
            #Розрахунок насипу
            elif height > 6:
                h = 6

                a = self.calculate_bottom_side(b, h, self.m[i])
                sum_area += self.calculate_area_trapezoid(a, b, h)
                
                height -= 6
                if i < len(self.m) - 1:
                    i += 1
                b = a
            else:
                h = height
                a = self.calculate_bottom_side(b, h, self.m[i])
                sum_area += self.calculate_area_trapezoid(a, b, h)
                break
                
        return sum_area

    #Розрахунок додаткового об’єму за рахунок зливної призми для насипу
    def calculate_additional_volume_drain_prism(self, l: float) -> float:
        #для 1-колійної ділянки
        if self.track == 1:
            area = (2.3 + self.b) / 2 * 0.15
        #для 2-колійної ділянки
        elif self.track == 2:
            area = self.b / 2 * 0.2
        
        volume = area * l
        return volume
          
    #Розрахунок додаткового об’єму за рахунок уположення укосів земляного полотна
    def calculate_additional_volume_placement_of_slopes(self, h1: float, h2: float, l: float) -> float:
        h0 = abs(h1 - h2)
        volume = 0
        
        if 6 < h0 <= 12:
            volume = abs((self.m[1] - self.m[0]) * pow((h0 - 6), 2)) * l
        elif 12 < h0 <= 18:
            volume = abs(((self.m[1] - self.m[0]) * pow((h0 - 6), 2)) + ((self.m[2] - self.m[1]) * pow((h0 - 12), 2))) * l
            
        return volume
        
    #Розрахунок додаткового об’єму за рахунок влаштування кюветів
    def calculate_volume_cuvettes(self, l: float) -> float:
        area = self.calculate_area_trapezoid(2.2, 0.4, 0.6)
        v = 2 * area * l
        return v
    
    #Додатковий об’єм для насипу
    def calculate_additional_volume_for_nas(self, h1: float, h2: float, l: float) -> float:
        v_zp = self.calculate_additional_volume_drain_prism(l=l)
        v_yk = self.calculate_additional_volume_placement_of_slopes(h1=h1, h2=h2, l=l)
        v = v_zp + v_yk
        return v
        
    #Додатковий об’єм для виїмки
    def calculate_additional_volume_for_viem(self, l: float) -> float:
        v_zp = self.calculate_additional_volume_drain_prism(l=l)
        v_cuv = self.calculate_volume_cuvettes(l)
        v = v_cuv - v_zp
        return v
    
    #Додатковий об’єм за рахунок косогірності місцевості для насипу 
    def calculate_additional_volume_for_nas_for_placement(self, l: float) -> float:
        _max = max(self.h1, self.h2)
        if _max <= 6:
            m = self.m[0]
        elif _max > 6 and _max <= 12:
            m = self.m[1]
        else:
            m = self.m[2]
     
        k = pow(m, 2) / (pow(self.n, 2) - pow(m, 2))
        h = (self.h1 + self.h2) / 2
        f = self.calculate_sum_areas_trapezoids(height=h)
        d = self.b
        v = k * l * (f + (pow(d, 2) / (4 * m)))
        
        return v
    
    #Додатковий об’єм за рахунок косогірності місцевості для виїмки
    def calculate_additional_volume_for_viem_for_placement(self, l: float) -> float:
        m = self.m[0]
        k = pow(m, 2) / (pow(self.n, 2) - pow(m, 2))
        h = (self.h1 + self.h2) / 2
        f = self.calculate_sum_areas_trapezoids(height=h)
        d = self.b + 4.4
        v = k * l * (f + (pow(d, 2) / (4 * m)))
        
        return v

    #розрахунок об’єму
    def calculate_volume_by_sum_trapezoids(self, h1: float, h2: float, l: float) -> float:
        f1 = self.calculate_sum_areas_trapezoids(height=h1)
        f2 = self.calculate_sum_areas_trapezoids(height=h2)
        v  = self.calculate_volume_trapezoid(f1, f2, l)
        
        return v
        
    #розрахунок насипу
    def calculate_nas(self, h1: float, h2: float, l: float) -> float:
        v = self.calculate_volume_by_sum_trapezoids(h1=h1, h2=h2, l=l)
        v_add = self.calculate_additional_volume_for_nas(h1=h1, h2=h2, l=l)
        v_nas = v + v_add
        
        if (self.n is not None) and (self.n != 0.0):
            v_add_placement = self.calculate_additional_volume_for_nas_for_placement(l)
            v_nas += v_add_placement
        
        return round(v_nas / 1000, 2)
    
    #розрахунок виїмки
    def calculate_viem(self, h1: float, h2: float, l: float) -> float:
        v = self.calculate_volume_by_sum_trapezoids(h1, h2, l)
        v_add = self.calculate_additional_volume_for_viem(l)
        v_viem = v + v_add
        
        if (self.n is not None) and (self.n != 0.0):
            v_add_placement = self.calculate_additional_volume_for_viem_for_placement(l)
            v_viem += v_add_placement
            
        return round(v_viem / 1000, 2)
        
    #розрахунок точки переходу
    def calculate_transition_point(self) -> float:
        point = ((-1 * self.h1) * self.l) / (self.h2 - self.h1)
        
        return point
        
    def calculate(self) -> list[float]:
        v_nas = 0.0
        v_viem = 0.0
        
        if self.h1 >= 0 and self.h2 >= 0:
            v_nas = self.calculate_nas(self.h1, self.h2, self.l)
        elif self.h1 <= 0 and self.h2 <= 0:
            v_viem = self.calculate_viem(self.h1, self.h2, self.l)
        else:
            transition_point = self.calculate_transition_point()
            if self.h1 > self.h2:
                v_nas = self.calculate_nas(self.h1, 0, transition_point)
                v_viem = self.calculate_viem(self.h2, 0, self.l - transition_point)
            else:
                v_nas = self.calculate_nas(self.h2, 0, self.l - transition_point)
                v_viem = self.calculate_viem(self.h1, 0, transition_point)

        return [v_nas, v_viem]
    