#Simple algorithim that finds the roots of a number
#Usage: python3 factors {integer - optional}

import sys

def findRoots(n, listR):
    while n % 2 == 0:
        listR.append(2);
        n /= 2;
    while n % 3 == 0:
        listR.append(3);
        n /= 3;
    if n != 1:
        f = 5;
        while f <= n:
          while n % f == 0:
            listR.append(f);
            n /= f;
          f += 2;

if (len(sys.argv) == 2):
    number = sys.argv[1];
else:
    number = input("Enter a integer: ");
number = int(number);
listOfRoots = [1];

findRoots(number, listOfRoots);
listDup = listOfRoots;
finalDictionary = {};

for n in listOfRoots:
  for n2 in listDup:
    if n == n2:
      if n in finalDictionary: finalDictionary[n] = finalDictionary[n] + 1;
      else: finalDictionary[n] = 2;
      listDup.remove(n2);

print(" ");
#print ("*" * 50);
print ("\tExtended form: ", listOfRoots);
#print ("*" * 50);
print ("\tFactored form:", end=' ');
print (' [', end = '');
for n in finalDictionary:
  if n != 1:
    print( "*", end = ' ');
    if finalDictionary[n] != 1:
      print( n, "^",finalDictionary[n], end=' ');
    else:
      print( n, end=' ');
  else: 
    print(1, end=' ');
print (']\n');

