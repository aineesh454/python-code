class GrandPa:
    def __init__(self, name, car, money):
        self.name = name
        self.car = car
        self.money = money

    def displayAssets(self):
        return f" {self.name} has  {self.money } and also has a  {self.car} car"

class grandSon(GrandPa):
    pass

gpl = GrandPa(name="John", car="BMW", money=100000)
print(gpl.displayAssets())