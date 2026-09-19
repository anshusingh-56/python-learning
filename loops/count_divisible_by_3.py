# Count numbers divisible by 3

number = 100

count = 0

for i in range(1, number + 1):
    if i % 3 == 0:
        count +=1
    
print("Count:",count)