def greet_programmer(): 
    pass
    print("Hello, programmer!")

def greet(name):
    pass
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b  

def halve(value):
    if isinstance(value, (int, float)): 
        return value / 2 
    else:
        return None  