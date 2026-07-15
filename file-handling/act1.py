import time

file = open("sample.txt", "r")
whole_content = file.read()
print(whole_content)

file.seek(0)
lines = file.readline()
for i ,line in enumerate(lines):
    print(f"Line {i}th line - {line}")

file.seek(0)
print("printing the first 4 characters .....")
time.sleep(2)
print(file.read(4))

file.close()