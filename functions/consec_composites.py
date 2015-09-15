#Constructs a list of N consecutive composite (non-prime) numbers
import sys
import math

def findCC(N):
    listCC = []
    for z in range(1,  N):
      x = math.factorial(N + 1) + z;
      listCC.append(x)
    return listCC
    



def prompt():
  if (len(sys.argv) == 2):
    number = sys.argv[1];
  else:
    number = input("Enter a integer: ");
  number = int(number);
  listOfCC = findCC(number);
  print(listOfCC);

prompt();
