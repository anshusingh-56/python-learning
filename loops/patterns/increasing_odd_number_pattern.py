# Increasing Odd Number Pattern

sum = 1

for i in range(1, 7):
    for j in range(1, i + 1):
        print(sum, end=" ")
        sum += 2
    print()
