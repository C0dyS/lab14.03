
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return print('engine STARTED')

    def __eq__(self, other):
        return self.year == other.year
    def __le__(self,other):
        return self.year <= other.year
    def __it__(self,other):
        return self.year < other.year
    def __ne__(self,other):
        return self.year != other.year
    def __ge__(self,other):
        return self.year >= other.year
