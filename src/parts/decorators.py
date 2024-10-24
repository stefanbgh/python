### 57 ###
# decorators

def hello(func):
    def wrapper():
        return "Hello" + func() # f"Hello{func()}"
    return wrapper

def space(func):
    def wrapper():
        return " " + func()     # f" {func()}"
    return wrapper

def world(func):
    def wrapper():
        return "World" + func() # f"World{func()}" 
    return wrapper

@hello
@space
@world
def main():
    return "!"

@world
def question():
    return "???"

res = main()
fn = question()

print(res)
print(fn)