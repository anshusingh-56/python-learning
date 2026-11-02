# Break Keyword (Terminates the loop)
for i in range(1, 100):
    if i == 11:
        break  # Exit the loop when i becomes 11
    print(i)

# Continue Keyword (Skips the current iteration)
for i in range(1, 100):
    if i % 5 == 0:
        continue  # Skip numbers divisible by 5
    print(i)

# Pass Keyword (Placeholder statement)
age = 12

if age > 19:
    pass  # Do nothing for now
else:
    print("Incorrect")
