# Program to find square of elements using map()

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square = lambda x: x * x

m1 = map(square, l2)

print(list(m1))
