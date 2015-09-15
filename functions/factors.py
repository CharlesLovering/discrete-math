#simple function to find the factors of a number
#Usage: python3 factors {integer - optional}

import sys

def findRoots(n):
  listR = [];
  if n == 0:
    listR = [0];
    return listR;
  if n == 1:
    listR = [1];
    return listR;
  if n < 0:
    listR = [-1];
    n *= -1;   
  while n % 2 == 0:
    listR.append(2);
    n /= 2;
  while n % 3 == 0:
    listR.append(3);
    n /= 3;
  if n != 1:
    f = 5;  
    while f <= n and n != 1:
      while n % f == 0:   
        listR.append(f);
        n /= f;
      f += 2;
  return listR;

def formDictionary(listR):

  listDup = list(listR);
  finalD = {};

  for n in listOfRoots:
    if listDup:
      listDup.pop(0);
      for n2 in listDup:
        if n == n2:
          if n in finalD:
            finalD[n] = finalD[n] + 1;
            listDup.pop(0);
          else:
            finalD[n] = 2;
      if not n in finalD:
        finalD[n] = 1;
  return finalD;

def printDictionary(dict):
  first = True;
  for n in finalDictionary:
    if n != 1:
      if not first: 
        print( " *", end = ' ');
      if finalDictionary[n] != 1:
        print( n, "^",finalDictionary[n], end='');
      else:
        print(n, end='');
      first = False;
    else: 
      print(1, end='');

def printFactors(listR, dictR):
  print ("/" * 50);
  print ("\tExtended form: ", listOfRoots);
  print ("\tFactored form:", end=' ');
  print (' [', end = '');

  printDictionary(dictR);
  print (']');
  print ("/" * 50);

print("why here am i")
if (len(sys.argv) == 2):
    number = sys.argv[1];
else:
    number = input("Enter a integer: ");
number = int(number);
listOfRoots = [1];
listOfRoots = findRoots(number);
finalDictionary = formDictionary(listOfRoots);
printFactors(listOfRoots, finalDictionary);

