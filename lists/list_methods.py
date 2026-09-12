list = [2, 4, 3, 5]

# Add one element at the end 
list.append(6)
print("After appendt:", list)

# Sort in ascending order 
list.sort()
print("After sort:", list)

# Sort in desending order
list.sort(reverse=True)
print("After sort(reverse=True):", list)

# Reverse list
list.reverse()
print("After reverse:", list)

# Insert element atv index
list.insert(2, 7)
print("After insert:", list)

# Removes percticular element
list.remove(3)
print("After remove:", list)

# Remove element at index
list.pop(1)
print("After pop:", list)