class GrandPa:
    def __init__(self, name, car, money):
        self.name = name
        self.car = car
        self.money = money

    def displayAssets(self):
        return f" {self.name} has  {self.money } and also has a  {self.car} car"

class grandSon(GrandPa):
    def __init__(self, name, car, money, laptop):
        GrandPa.__init__(self, name, car, money)
        self.laptop = laptop

    def displayDetails(self):
        return f"{GrandPa.displayAssets(self)} and has a {self.laptop} laptop."

gs1 = grandSon(name="Mike", car="Audi", money=250000, laptop="MacBook Pro")
print(gs1.displayDetails())    