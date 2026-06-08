temp = float(input("Enter a temperature in Celsius: "))

if temp <=10:
    print("It's a very cold day.")
elif temp > 10 and temp <=25:
    print("It's a pleasant day.")
elif temp > 25 and temp <=35:
    print("It's a hot day.")
else:
    print("It's a very hot day.")