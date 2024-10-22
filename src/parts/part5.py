### 5 ###
# arith and math

num1 = 2
num2 = 2

num1 += 1

res = num1 + num2

print(f"The result is: {num1} + {num2} = {res}")

print("------------------------")

numbers = input("Enter 5 numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))

while len(numbers) != 5:
    print("Please enter exactly 5 numbers.")
    print("------------------------")

    numbers = input("Enter 5 numbers separated by spaces: ")
    numbers = list(map(int, numbers.split()))

max_num = max(numbers)
min_num = min(numbers)

print("------------------------")

print(f"The largest number is: {max_num}")
print(f"The smallest number is: {min_num}")
print("Thank you!")

print("------------------------")