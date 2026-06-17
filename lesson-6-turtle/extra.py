import sys

word= input("Enter a word: ").strip()

if not word or not word.isalpha():
    print("Please enter a valid word.")
    sys.exit(1)

letter = input("Enter a letter: ").strip()
if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single letter.")
    sys.exit(1)

word = word.lower()
letter = letter.lower()

frequency = word.count(letter)
if frequency > 0:
      print(f"The letter '{letter}' appears {frequency} time(s) in the word '{word}'.")
else:
      print(f"The letter '{letter}' does not appear in the word '{word}'.")

  
