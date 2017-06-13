def add(a,b):
    print(f"ADDING {a} and {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} and {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} and {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} and {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(20,1)
height = subtract(78,4)
weight = multiply(35,2)
iq = divide(100,2)

print(f"Age: {age}\n Height: {height}\n Weight: {weight}\n IQ: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becones:", what, "Can you do it by hand?")
