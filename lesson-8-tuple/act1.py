pasta=("pasta Arrabbita","italian pasta",20,"medium")
biriani=("chicken biriani","indian rice",45,"spicy")

print("Recipe 1", pasta)
print("Name of Recipe 1: ", pasta [0])
print("Cuisine of Recipe 1", pasta [1])
print(f"Prep Time of Recipe 1: {pasta [2]} minutes")
print("Difficulty level of Recipe 1", pasta[-1])

print("\n")
print("*"*30)
print("\n")
    
all_tuples = (pasta, biriani)
print(f"First Recipe Name {all_tuples[0][0]}")
print(f"Second Recipe Name: {all_tuples [1][0]}")
print(f"Second Recipe prep time: {all_tuples [1][2]} minutes")
print(f"Second Recipe difficulty: {all_tuples [1][3]}")

print("\n")
print("*"*30)
print("\n")

print("iterate/loop through the tuple")
for detail in pasta:
    print("-", detail)

print("\n")
print("*"*30)
print("\n")

print("enumerate through the tuple")
for idx, detail in enumerate(biriani ,start=1):
    print(f"{idx} : {detail}")

print("\n")
print("*"*30)
print("\n")

fruits = ("apple", "banana", "orange", "date", "kiwi")
f1,f2,f3,f4,f5 = fruits
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

x,*y = fruits
print(x)
print(y)

print(fruits.index("apple"))

print(fruits.count("apple"))

print("apple" in fruits)
print("apple" not in fruits)

t1 = (1,2,3)
t2 = ("john","david","mayank")

t3= dict(zip(t1,t2))

print("\n")
print("*"*30)
print("\n")
for id,name in t3.items():
    print(f"{id} : {name}")