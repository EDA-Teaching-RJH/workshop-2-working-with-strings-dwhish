import math  

def main():
  A= input(int"what is the length of A")
  B= input(int"what is the length of B")
  C= pythag(A,B)
  print(C)


def pythag(A,B):
   csquared= A**2 + B**2
   math.sqrt(csquared)


main()
