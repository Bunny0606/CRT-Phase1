for i in range(1,5):
    for j in range(1,5):
        print ("*",end="")
    print()

for i in range(1,6):
     for j in range(1,7-i):
         print("*",end="")
     print()

r=5
for i in range(1,6):
    for s in range(1,r-i+1):
        print("",end="")
    for j in range(1,1+i):
        print("*",end="")
    print()