class Car:
    def __init__(self, make, model, year, odometr=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = odometr
        self.fuel = fuel
    def drive(self, path):
        self.path = path
        if self.path <= self.fuel * 10:
            self.__add_distance()
            self.__substract_fuel()
            print('Let’s drive!')            
        else:
            print('Need more fuel, please, fill more!')

    def __add_distance(self):
        self.odometr += self.path

    def __substract_fuel(self):
        self.fuel = self.fuel - self.path/10

bugatti = Car('bugatti', 'veyron', 2005)
bugatti.drive(700)
print(bugatti.odometr)
print(bugatti.fuel)