#from factors import findRoots, formDictionary, printDictionary
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

  for n in listR:
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

def printDictionary(dictD):
  first = True;
  for n in dictD:
    if n != 1:
      if not first: 
        print( " *", end = ' ');
      if dictD[n] != 1:
        print( n, "^",dictD[n], end='');
      else:
        print(n, end='');
      first = False;
    else: 
      print(1, end='');


def smaller(a, b):
	if a > b:
		return b;
	else:
		return a;
def larger(a, b):
  if a > b:
    return a;
  else:
    return b;
def gcf(a, b):
	listA = findRoots(a);
	listB = findRoots(b);
	dictA = formDictionary(listA);
	dictB = formDictionary(listB);
	gcf = {};
	for n in dictA:
		if n in dictB:
			gcf[n] = smaller(dictA[n], dictB[n]);
	printDictionary(gcf);
	print("");
def lcm(a, b):
  listA = findRoots(a);
  listB = findRoots(b);
  dictA = formDictionary(listA);
  dictB = formDictionary(listB);
  lcm = {};
  for n in dictA:
    if n in dictB:
      lcm[n] = larger(dictA[n], dictB[n]);
    else:
      lcm[n] = dictA[n]
  for n in dictB:
    if not n in dictA:
      lcm[n] = dictB[n]

  
def prompt:
  if (len(sys.argv) == 4):
    a = int(sys.argv[2]);
    b = int(sys.argv[3]);
  else:
    a = int(input("Enter int, a: "));
    b = int(input("Enter int, b: "));

  if (len(sys.argv) == 2):
    if (sys.argv[1] == "lcm"):
      lcm(a, b);
    elif (sys.arg[1] == "gcf"):
      gcf(a, b);
  else:
    print("functions [function] {~a} {~b}");
    prompt();

prompt();
