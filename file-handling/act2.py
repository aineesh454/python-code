word = input("Enter lines starting with to skip them: ")
file = open("sample.txt", "r")
lines = file.readlines()
for line in lines:
    if line.startswith(word):
        continue
    else:
        print(line.strip())

file.close()