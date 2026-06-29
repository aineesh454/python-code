mylist = []
print("empty list:", mylist)

mylist2 = [11, 7, 4, 99, 3, 12]
print(mylist2)

print(mylist2[0])

print(mylist2[-1])

print(mylist2[1:3])


print("my list :", mylist2)

mylist2.append(33)
print(mylist2)


mylist2.remove(3)
print(mylist2)


mylist2.pop()
print(mylist2)

mylist2.pop(2)
print(mylist2)

print("current list :", mylist2)
mylist2.sort()
print("current list after sorting  :", mylist2)

mylist2.reverse()
print("current list after reversing  :", mylist2)

print(mylist2[::-1])