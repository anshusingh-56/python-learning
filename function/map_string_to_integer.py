# Map – Used for transforming data within a sequence or collection.
# map returns map object 
# Convert string values into integers.
# syntax - map(function, sequence)

l1 = ["1", "2", "3", "4"]

print(l1)
newlist = map(int, l1)
print(list(newlist))
