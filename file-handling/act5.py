n= int(input("How many Characters to preview?: "))
file = open("class-notes.txt", "r")
print(file.read(n))
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
print(file.read(n))
file.close()
print("Total lines:",len(lines))
for i in range(len(lines)):
    print("Line",i+1,"->",lines[i].strip()) 
print()

word = input("skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->",line.strip())

    else:
        print("keep ->",line.strip())
    
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("class-notes-odd.txt", "w")
for i in range(0 ,len(lines) ,2):
        out.write(lines[i])
out.close()
print("Odd lines have been written to 'class-notes-odd.txt'.")