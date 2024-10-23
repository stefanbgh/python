### 4 ###
# input()

print("------------------------")

nickname = input("What is your nickname? ")
favorite_game = input("What is your favorite game? ")

print("------------------------")

dota_set = ["dota", "dota2"]
lol_set = ["leagueoflegends", "lol"]
gta_set = ["gta", "grandtheftauto"]

check_game = "".join(favorite_game.split()).lower()

print(f"Hey {nickname}!")

if check_game in dota_set:
    print(f"{favorite_game}?! Interesting a strategic game, good choice!")
elif check_game in lol_set:
    print(f"{favorite_game}?! Ohh, that's so good! I love this game.")
elif check_game in gta_set:
    print(f"{favorite_game}?! What a classic. This is one of the most popular video games.")
else:
    print(f"{favorite_game}?! I'm glad to hear that.")

print("Thanks for participating in our survey. See you!")

print("------------------------")
print("------------------------")

answer = input("Did you like our survey? (yes/no): ").lower()

while answer != "yes" and answer != "no":
    print("Sorry, you can enter just: 'yes' or 'no'.")
    print("------------------------")
    answer = input("Did you like our survey? (yes/no) ").lower()

if answer == "yes":
    print("Thanks for your positive feedback!")
elif answer == "no":
    print("Thanks for your response!")

print("------------------------")