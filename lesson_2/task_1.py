class Vehicle:

    def __init__(self, make, model, year,  color, type = 'Vehicle'):

        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.type = type

    def get_describe(self):
        describe = f'{self.make} {self.model} {self.year} the color is {self.color}'
        return describe


    def get_type(self):
        return self.type



class Car(Vehicle):
    

    def __init__(self, make, model, year,  color, type = 'Passenger car'):
        super().__init__(make, model, year,  color, type)


    def get_type(self):
        return self.type


class Truck(Vehicle):


    def __init__(self, make, model, year,  color, type = 'Truck'):
        super().__init__(make, model, year,  color, type)


    def get_type(self):
        return self.type


my_car = Vehicle('honda', 'civic', '2007', 'blue')
print(my_car.get_describe())
print(my_car.get_type())

my_new_car = Car('reno', 'megan', 2011, 'white')
print(my_new_car.get_describe())
print(my_new_car.get_type())

my_truck = Truck('ZIL', '130', '1968', 'green')
print(my_truck.get_describe())
print(my_truck.get_type())