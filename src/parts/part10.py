### 15 ###
# format specifier - {value:flags}
# .fnum
# :num (spread with white space on the start)
# :0num (spread without white space, instead use 0)
# <num (spread with white space from the end)
# =num (if num is positive + else -)
# ,num

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1: {price1:.3f}")
print(f"Price 2: {price2:.3f}")
print(f"Price 3: {price3:.3f}")