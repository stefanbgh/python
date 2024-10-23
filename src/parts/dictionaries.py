### 25 ###
# dictionaries

users = {
    1: "Person1",
    2: "Person2",
    3: "Person3"
}

users.update({ 4: "Person4" })
users.update({ 5: "Person5" })
users.pop(3)
users.popitem()

# users.values() - (['Person1', 'Person2', 'Person4'])
# users.keys()   - ([1, 2, 4])
# users.items()  - ([(1, 'Person1'), (2, 'Person2'), (4, 'Person4')])

usr_id = 4
get_user = users.get(usr_id)

if get_user is None:
    print("The user was not found")
else: 
    print(f"The name of the user is: {get_user}")

print(users)