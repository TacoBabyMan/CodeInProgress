import math as math

symbol = str(input("Input symbol: "))
number = int(input("Input odd number: "))
spaces = 0
spaceStore = []
oddNumbers = []

p = 0
k = 0
def Aliens(p,k):
    x = spaceStore[p]
    bricks = "";
    while k < x:
        bricks += str(" ")
        k+=1

    x = oddNumbers[p]
    letters = ""
    k = 0
    while k < x:
        letters += str(symbol)
        k+=1

    print(bricks,letters)
    k = 0
    if(p != len(spaceStore)-1):
        p+=1
        Aliens(p,k)

for x in range(1,int(number+1)):
    evenChecker = math.floor(x/2)
    evenChecker = evenChecker*2

    if (evenChecker != x):
        spaces = number - x+1
        oddNumbers.append(spaces)


for x in range(1,int(number+1)):
    evenChecker = math.floor(x/2)
    evenChecker = evenChecker*2

    if (evenChecker != x):
        spaces = number - x
        spaceAdd = int( spaces/2)
        spaceStore.append(spaceAdd)

    if(x == number):
        oddNumbers.reverse();
        Aliens(p,k)
