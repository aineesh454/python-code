star_count = int(input("Enter the height: "))
for i in range(1, star_count + 1):
    for j in range(i):
        print("*", end="")
    print()