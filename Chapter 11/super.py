class Car:
    name = "Toyota"
    brand = "Corolla"

    def __init__(self):
        print(f"The name of the car is {self.name} and its brand is {self.brand}")

class SuperCar(Car):
    def __init__(self, variation):
        super().__init__()  # Correct usage of super()
        self.variation = variation

    def info(self):
        print(f"The name of the car is {self.name}, its brand is {self.brand}, and its variation is {self.variation}")

# Creating instances
# my_car = Car()
# print(my_car)  # This will still print the object reference

# Creating an instance of SuperCar
tesla = SuperCar("automatic")
tesla.info()
