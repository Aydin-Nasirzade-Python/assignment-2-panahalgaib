#import libraries here

def main():
  p = int(input("Enter the year [ex. 2021]: "))
  if p<0:
      print("Invalid year!")
  elif p==2000 or (abs(p-2000))%12==0:
      print("p is the year of Dragon")
  elif  p==2001 or (abs(p-2001))%12==0:
      print("p is the year of Snake")
  elif p==2002 or (abs(p-2002))%12==0:
      print("p is the year of Horse")
  elif p==2003 or (abs(p-2003))%12==0:
      print("p is the year of Sheep")
  elif p==2004 or (abs(p-2004))%12==0:
      print("p is the year of Monkey")
  elif p==2005 or (abs(p-2005))%12==0:
      print("p is the year of Rooster")
  elif p==2006 or (abs(p-2006))%12==0:
      print("p is the year of Dog")
  elif p==2007 or (abs(p-2007))%12==0:
      print("p is the year of Pig")
  elif p==2008 or (abs(p-2008))%12==0:
      print("p is the year of Rat")
  elif p==2009 or (abs(p-2009))%12==0:
      print("p is the year of Ox")
  elif p==2010 or (abs(p-2010))%12==0:
      print("p is the year of Tiger") 
  else:
      print("p is the year of Hare")
  pass

if __name__ == "__main__":
  main()
