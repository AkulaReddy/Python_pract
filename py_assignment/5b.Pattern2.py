n=int(input("Enter the no. of rows:"))
for i in reversed(range(1,n+1)):
    for j in range(i):
        print("*",end=" ")
    print("")
