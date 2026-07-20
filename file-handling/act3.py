file = open("sample.txt", "r")
lines = file.readlines()
file.close()

outfile = open("odd_lines.txt", "w")

for i in range(0, len(lines), 2):
        outfile.write(lines[i])

outfile.close()
print("Odd lines have been added to 'Outfile.txt'.")