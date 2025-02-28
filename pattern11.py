#pattern --> 11
n=4
for i in range(n+1):
    for j in range(i-1):
        print("  ",end="  ");
    for j in range((2*n-2*i-1)):
        print("*",end="  ");
    print()
