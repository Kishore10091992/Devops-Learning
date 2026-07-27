# 1

def greet(name = "guest") :
    return f"hi {name}"

print(greet(name = "guest"))

# 2

def greet(name = "guest") :
    return f"hi {name}"

name = greet(name = "kishore")

print(name)

# 3

def sum(a, b, c=4) :
    return a+b+c

d = sum(4, 2)

print(d)

# 4

def sum(a, b, c=4) :
    return a+b+c

d = sum(4, 2, 6)

print(d)