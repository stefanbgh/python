### 7 ###
# ternary operator

print("------------------------")

light = input("Please, press one button on our lamp: (on/off) ")
role = input("Choose one role: (user/admin) ")

print("------------------------")
print("------------------------")

lamp = "The lamp is turned on." if light == "on" else "The lamp is turned off."
print(f"{lamp}")

access = "Full Access" if role == "admin" else "Limited Access"
print(f"{access}")

print("------------------------")