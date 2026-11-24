# Menu driven

def sum():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2st number: "))
    c = a + b
    print("Addition is : ", c)

def sub():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2st number: "))

    return a-b

def mul(a,b):
    c = a * b
    print("Multiplication is : ", c)

def div(a,b):
    return a/b

while True:
    print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Exit")
    ch = int(input())

    if ch == 1:
        sum()

    elif ch == 2:
        print("Subtraction is : ", sub())

    elif ch == 3:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2st number: "))
        mul(a, b)

    elif ch == 4:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2st number: "))

        print("Division is :",div(a,b))

    elif ch == 5:
        break
