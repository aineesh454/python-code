file = open("sample.txt", "r")
lines = file.readlines()
file.close()

outFile = open("appended.txt", "a")
for line in lines:
    outFile.write("\n" + line)
outFile.close()