class ProductBlueprint:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def displayDetails(self):
        return f"Product: {self.name} | Category: {self.category} | Original Price: ${self.price:.2f}"

    def calculateDiscount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        discounted_price = self.price - discount_amount
        return discounted_price


laptop = ProductBlueprint(name="Gaming Laptop", price=1200.00, category="Electronics")
shoes = ProductBlueprint(name="Running Shoes", price=80.00, category="Apparel")

print(laptop.displayDetails())
laptop_discount = 15
final_laptop_price = laptop.calculateDiscount(laptop_discount)
print(f"Price after {laptop_discount}% discount: ${final_laptop_price:.2f}\n")

print(shoes.displayDetails())
shoes_discount = 20
final_shoes_price = shoes.calculateDiscount(shoes_discount)
print(f"Price after {shoes_discount}% discount: ${final_shoes_price:.2f}")
