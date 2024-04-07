#import libraries here

def main():
  p = int(input("Enter the wavelength in nm: "))
  if p>=380 and p<450:
      print("The relevant color is Violet")
  elif p>=450 and p<495:
      print("The relevant color is Blue")
  elif p>=495 and p<570:
      print("The relevant color is Green")
  elif p>=570 and p<590:
      print("The relevant color is Yellow")
  elif p>=590 and p<620:
      print("The relevant color is Orange")
  elif p>=620 and p<=750:
      print("The relevant color is Red")
  else:
      print("Invalid input")
  pass

if __name__ == "__main__":
  main()
