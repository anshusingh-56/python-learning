# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

sub1 = input("Enter first subject marks: ")
sub2 = input("Enter second subject marks: ")
sub3 = input("Enter third subject marks: ")

marks = {
    "maths": sub1,
    "science": sub2,
    "physics": sub3
}

print(marks)