"""
Read all the names from words.txt, line by line,
 and store only those names in another list , 
 where the length of each name is greater than 4 and print those names
 from that list, into another file 'words_out.txt'

 words.txt
 *********
  Viaan
  Nabhya
  John
  Robin
  Joe
  Sandeep
  chi
  Huan
  Codingal
"""

file = open("word.txt", "r")
lines = file.readlines()
file.close()

outfile = open("words_out.txt", "w")
for line in lines:
    if len(line.strip()) > 4:
        outfile.write(line)
outfile.close()
print("Names with length greater than 4 have been added to 'words_out.txt'.")