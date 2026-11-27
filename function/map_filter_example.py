# Program to demonstrate map() and filter()

l1 = [1, 2, 3, 4, 55, 7, 8, 9]

# Square of elements
squares = map(
    lambda x: x * x,
    l1
)

# Odd numbers
odd_numbers = filter(
    lambda x: x % 2 != 0,
    l1
)

print("Squares:", list(squares))
print("Odd Numbers:", list(odd_numbers))
