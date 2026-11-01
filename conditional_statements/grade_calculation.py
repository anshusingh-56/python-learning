marks = int(input("Enter your number: "))
if marks > 0 and marks <= 100:
    if marks < 35:
        print("Fail")
    elif marks < 50:
        print("Passed with D grades")
    elif marks < 75:
        print("Passed with C grades")
    elif marks < 85:
        print("Passed with B grades")
    elif marks < 90:
        print("Passed with A grades")
    elif marks <= 100:
        print("Passed with A+ grades\nU r a brillrant student..")
else:
    print("Invalid Marks !!!")
