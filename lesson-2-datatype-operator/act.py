snack_name = "chips"
price = 1.50
quantity = 10
is_available = True

print("Snack Name:", snack_name)
print("Price:", price)
print("in stock:", quantity)
print("Available:", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))
total_cost = price * quantity
print("Total Cost:", total_cost)
print("Sale Price:", price - 0.25)  
print("double quantity:", quantity * 2 )

print("is price under $2?", price < 2)
print("is quantity greater than 5?", quantity > 5)
print("is price equal to 1.50?", price == 1.50)

shop_name = "Quick"+" "+"bites"
print("Shop Name:", shop_name)
print("letters in snack name:", len(snack_name))
print("first letter of snack name:", snack_name[0])

price_a = 1.50
price_b = 3.00
print("before discount:", price_a,"and", price_b)

temp = price_a
price_a = price_b
price_b = temp
print("after discount:", price_a,"and", price_b)
