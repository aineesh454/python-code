
class CarBluePrint:

    def __init__(self, Brand, Model, Year):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year

    def displayDetails(self):
        return f"This car is {self.Brand} in this model {self.Model} of the year {self.Year} ."




h1 = CarBluePrint("BMW", 2, 2024)
print(h1.displayDetails())