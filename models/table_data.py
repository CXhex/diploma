class TableData:
    def __init__(self, table_size: int):
        self.headers = ["Відмітка на початку\nМ.", "Відмітка в кінці\nМ.", "Довжина\nМ.",
                       "Розширення\nМ.", "ОБ'ЄМ\nНАСИПУ", "ОБ'ЄМ\nВИЇМКИ"]
        self.table_size = None
        self.set_table_size(table_size)
        self.table_data = None
        self.set_table_data()
        self.table_info = {}
        
    def set_table_size(self, table_size: int):
        self.table_size = table_size
        
    def get_table_size(self) -> int:
        return self.table_size
        
    def set_table_data(self, data: list = None):
        if data is None:
            self.table_data = [[0.0 for c in range(len(self.headers))] for r in range(self.table_size)]
        else:
            self.table_data = data
        
    def update_table_data(self, table_size: int):
        old_size = self.get_table_size()
        
        if table_size > old_size:
            table_data = self.get_table_data() + [[0.0 for c in range(len(self.get_table_headers()))] for r in range(old_size, table_size)]
            self.set_table_data(table_data)
        elif table_size < old_size:
            table_data = self.get_table_data()[:table_size]
            self.set_table_data(table_data)
            
        self.set_table_size(table_size)
        
    def get_table_data(self) -> list:
        return self.table_data
    
    def autofill_table_data(self):
        table_data = self.get_table_data()
        
        for i in reversed(range(self.get_table_size() - 1)):
            table_data[i][1] = table_data[i + 1][0]
            
        self.set_table_data(table_data)
    
    def set_table_headers(self, headers: list):
        self.headers = headers
        
    def get_table_headers(self) -> list:
        return self.headers
    
    def headers_update(self, check: bool):
        if check:
            self.headers.insert(4, "Косогірність")
            
            new_data = self.get_table_data()
            for d in new_data:
                d.insert(4, 0.0)

            self.set_table_data(new_data)
        else:
            self.headers.remove("Косогірність")
            new_data = self.get_table_data()
            for d in new_data:
                del d[4]

            self.set_table_data(new_data)
    
    def set_table_info(self, info: dict):
        self.table_info = info
        
    def get_table_info(self) -> dict:
        return self.table_info
    