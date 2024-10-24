### 40 ###
# scope resolution

# example 1

def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def fn():
    first_name = "John"
    last_name = "Doe"

    return full_name(first_name, last_name)

res = fn()
print(res)

# example 2

def closure(y):
    x = 3

    def fn(x):
        return x + y
    
    return fn(x)

y = 2

res = closure(y)
print(res)