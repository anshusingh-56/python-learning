# Fibonacci series
n = int(input("Enter number of terms: "))

f = 0
s = 1
print("Fibonacci series is:", f, s, end = " ")  # using end = " " to print in same line
for j in range (3, n+1):
    next = f + s
    f = s
    s = next
    print(next, end = " ")
