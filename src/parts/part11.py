### 16 ###
# while

n = int(input("Enter a number between 1-10: "))

while n <= 1 or n >= 10:
    print(f"#{n} is not valid. Try again!")
    print("------------------------")
    n = int(input("Enter a number between 1-10: "))

print(f"Your number is: {n}. Good job!")

### 17 ###
# another calc

### 18 ###
# for, continue, break

# range(start,end,step)
# reversed()

print("# For loop")

for x in range(1, 6):
    if x == 1 or x == 3:
        continue
    elif x == 5:
        break
    else:
        print(x)