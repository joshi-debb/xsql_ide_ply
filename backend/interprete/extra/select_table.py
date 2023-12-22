
class Record:
    def __init__(self):
        self.recods = []

class Select_table:
    def __init__(self):
        self.fields = []
        self.records:Record = []
        
    def serializar(self):
        json = {
            'fields': self.fields,
            'records': []
        }
        
        aux = []
        
        for record in self.records:
            aux.append(record.recods)
        
        json['records'] = aux

        return json