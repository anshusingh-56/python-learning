students = []

n = int(input("Enter no of student: "))

for i in range(n):
    print("Enter marks of students: ", i+1)
    m = int(input())
    students.append(m)

print("Total marks of students: ", students)
print("Maximum marks of students: ", max(students))
print("Minimum marks of students: ", min(students))

total = sum(students)
no_of_student = len(students)

avg = total / no_of_student
print("Average marks of students: ", avg)

# delete
rem = n = int(input("Enter marks to remove: "))
if rem in students:
    students.remove(rem)
else:
    print("Marks not exit")

print(students)

# Search
search = n = int(input("Enter marks to search: "))
if search in students:
    print(search, "found")
else:
    print(search, "not found")

print(students)

length = len(students)

# Update
update = n = int(input("Enter marks to update: "))

for i in range(0, length):
    if students[i] == update:
        newmarks = int(input("Enter new marks: "))
        students[i] = newmarks
        break
        
print(students)
