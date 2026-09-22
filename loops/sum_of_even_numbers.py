# Sum of even number

number = int(input("Enter a number: "))

sum = 0

for i in range(0, number + 1, 2):
    sum += i

print("Sum of even number = ", sum)