#import libraries here

def main():
  letter_1 = "y"
  letters = "aeiou"

  p = input("Enter a letter of alphabet: ")

  if p in letter_1:
      print("Sometimes it is a vowel, and sometimes it is a consonant!")
  elif p in letters:
      print("Entered alphabet is a vowel!")
  else:
      print("Entered alphabet is a consonant!")

  pass

if __name__ == "__main__":
  main()
