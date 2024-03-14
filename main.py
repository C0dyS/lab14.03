class Stadion:
    def __init__(self,name,date,country,city,seats):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.seats = seats

    def display(self):
        print(f'stadion {self.name} was built in {self.date} '
              f'in {self.country} in a city {self.city}')
    def change_name(self,new_name):
        self.name = new_name
    def change_dat(self,new_date):
        self.date = new_date
    def change_country(self,new_country):
        self.country = new_country
    def change_city(self,new_city):
        self.city = new_city
    def change_seat(self,new_amount):
        self.seats = new_amount

    def __str__(self):
        return f'Stadium: {self.name}, Date: {self.date}, Country: {self.country}, City: {self.city}, Seats: {self.seats}'

    def __lt__(self, other):
        return self.seats < other.seats

    def __le__(self, other):
        return self.seats <= other.seats

    def __eq__(self, other):
        return self.seats == other.seats

    def __ne__(self, other):
        return self.seats != other.seats

    def __gt__(self, other):
        return self.seats > other.seats

    def __ge__(self, other):
        return self.seats >= other.seats
