### 6 ###
# logical operators (or, and, not)

print("------------------------")

first_num = int(input("Enter a first num: "))
second_num = int(input("Enter a second num: "))

print("------------------------")

if first_num > 3 and first_num < 7:
    print(f"The number {first_num} is between 3 and 7.")
else:
    print("I don't know where the number is.")

if second_num > 9 and second_num < 11:
    print(f"The number is: {second_num}")
else:
    print("What is your number?")

print("------------------------")