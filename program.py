import math as math;

symbol = "A";#input("Input symbol: ");
number = 9#input("Input odd number: ");
spaces = 0;

spaceStore = [];
rowTracker = 0;

for x in range(1,int(number+1)):
    evenChecker = math.floor(x/2)
    evenChecker = evenChecker*2
    if (evenChecker != x):
        spaces = number - x;
        spaceAdd = int( spaces/2);
        spaceStore.append(spaceAdd);

print(spaceStore);
function 
    for x in range(1,int(spaceStore[rowTracker])+1):
        print(spaceStore[rowTracker]);
        if(x == spaceStore[rowTracker]):
            rowTracker+=1;
            print(rowTracker);

        print();
