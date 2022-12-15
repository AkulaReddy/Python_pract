n=int(input("Enter a no."))
flag=0
if n==0 or n==1:
    print(n,"is not a prime")
elif n>1:    
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print(n,"is a prime")
    else:
        print(n,"is not a prime")
else:
    print("Invalid Number")
