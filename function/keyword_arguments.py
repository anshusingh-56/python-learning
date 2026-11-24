def display(roll, name, marks):
    print("Roll no:", roll)
    print("Name:", name)
    print("Marks:", marks)
    print()

# Function call using keyword arguments
display(roll=12, name="Anshu", marks=85.25)

# Order can be changed because arguments are passed using keywords
display(name="Shikha", roll=25, marks=98.5)

display(marks=96.5, name="Shweta", roll=30)
