import math as math

symbol = str(input("Input symbol: "))
number = int(input("Input number: "))
spaces = 0
spaceStore = []
oddNumbers = []

order = []

even = 0;

p = 0
k = 0
def Aliens(p,k):
    x = spaceStore[p]
    bricks = "";
    while k < x:
        bricks += str(" ")
        k+=1
    x = oddNumbers[p]
    walls = "";
    k = 0
    while k < x:
        walls += str(" ")
        k+=1
    order.append(bricks+symbol+walls)
    k = 0
    if(p != len(spaceStore)-1):
        p+=1
        Aliens(p,k)
def OddNormalise(num):
    width = len(num)
    for x in range(width-1,width):
        oddNumbers.pop(x)
def finalise(order):
    for x in range(1,len(order)-1):
        order[x] += symbol
    x = len(order)-1
    symbolStack = ""
    for g in range(1,number):
        symbolStack += symbol
    order[x] += symbolStack
    if(even == 1):
        order[0] += symbol
    for l in range(0,len(order)):
        print(order[l])
for x in range(1,int(number+1)):
    evenChecker = math.floor(x/2)
    evenChecker = evenChecker*2

    if (evenChecker != x):
        spaces = number - x+1
        oddNumbers.append(spaces)


for x in range(1,int(number+1)):
    evenChecker = math.floor(x/2)
    evenChecker = evenChecker*2
    if((math.floor(number/2))*2 == number):
        even = 1
    if (evenChecker != x):
        spaces = number - x
        spaceAdd = int( spaces/2)
        spaceStore.append(spaceAdd)

    if(x == number):
        oddNumbers.reverse()
        OddNormalise(oddNumbers)
        OddNormalise(oddNumbers)
        oddNumbers.insert(0,0)
        oddNumbers.insert(len(oddNumbers),0)
        Aliens(p,k)
        finalise(order)
