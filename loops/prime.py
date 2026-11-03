# Check weather a given number is prime or not

num = int(input("Enter your number: "))

isPrime = True
for i in range(2, num//2+1):
    if num % i == 0:
        isPrime = False
        break

if isPrime:
    print("Prime number")
else:
    print("Not a Prime number")