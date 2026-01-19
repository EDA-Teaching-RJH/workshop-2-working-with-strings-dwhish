import math  

def main():
  A= int(input("what is the length of A"))
  B= int(input("what is the length of B"))
  C= pythag(A,B)
  print(C)


def pythag(A,B):
   csquared= A**2 + B**2
   return math.sqrt(csquared)


main()
