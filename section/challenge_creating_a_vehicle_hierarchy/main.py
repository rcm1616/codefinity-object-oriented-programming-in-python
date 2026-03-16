class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed}"

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()}, Doors: {self.doors}"

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

    def get_info(self):
        return f"{super().get_info()}, Type: {self.type}"

v = Vehicle('generic', 50)
c = Car('toyota', 120, 4)
b = Bike('giant', 30, 'mountain')

print(v.get_info())
print(c.get_info())
print(b.get_info())