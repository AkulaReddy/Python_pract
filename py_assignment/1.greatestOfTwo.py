a=int(input("enter first no."))
b=int(input("enter second no."))
if a==b:
    print("Both are equal")
else:
    print("Biggest no. is:",end=" ")
    if a>b:
        print(a)
    else:
        print(b)
