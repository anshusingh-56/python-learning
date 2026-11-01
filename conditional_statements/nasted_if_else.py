# find greater number among three numbers
a, b, c = map(int, input("Enter three numbers : ").split())

if a==b and a==c:
    print("All numbers are same: ")
else:
    if a>b:
        if a>c:
            print(a, " is greater")
        else:
            print(c, " c is greater")
    else:
        if b>c:
            print(b, " is greater")
        else:
            print(c, " c is greater")
