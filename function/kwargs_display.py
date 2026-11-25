# **kwargs - variable length keyword arguments
# - internally xdictionary hota he 

def display(**kwargs):
    print(type(kwargs))
    for i in kwargs:
        print(i,":",kwargs[i])

display(roll=24, name="Nayan", age=23, marks=56.77)
