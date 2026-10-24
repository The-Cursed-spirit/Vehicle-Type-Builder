class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print("Brand : ", self.brand)
        print("Brand : ", self.model)

class  Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def show_info(self):
        super().show_info()
        print("Number of doors : ", self.doors)

# Create a Car object
car = Car("Toyota", "Camry", 4)

# Display info
car.show_info()

# Check inheritance
print("Is Car a subclass of Vehicle ?", issubclass(Car, Vehicle))