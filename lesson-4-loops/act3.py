limit = int(input("Enter the limit: "))
totol_sum = 0
start = 1
while start <= limit:
    totol_sum += start
    start += 1
print("sum of ", limit, "natural numbers:", totol_sum)
