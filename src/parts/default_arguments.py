### 32 ###
# default arguments

num = 3
def_arg = 2

def dp(x, y=def_arg):
    return x + y

res = dp(num)

print(f"{num} + {def_arg} = {res}")