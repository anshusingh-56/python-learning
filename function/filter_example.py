# Program to demonstrate filter()
# Select only odd numbers from the list.

l1 = [1, 2, 3, 4, 55, 7, 8, 9]

odd_numbers = filter(
    lambda x: x % 2 != 0,
    l1
)

print("Odd Numbers:", list(odd_numbers))
