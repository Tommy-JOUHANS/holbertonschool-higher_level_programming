a = 1024
b = 1024
del a
del b
c = 1024
print(c is a)  # False — they point to DIFFERENT objects
print(id(c) == id(a))  # False

