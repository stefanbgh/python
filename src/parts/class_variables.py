### 47 ###
# class

# magic methods 
# __eq__       -> ==
# __lt__       -> <
# __gt__       -> >
# __add__      -> +
# __contains__ -> in
# __getitem__  -> if

print("------------------------")
class User:
    year = 2024

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        User.year += 1

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nPassword: {self.password}"


    def get_info(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nPassword: {self.password}"
    
    @staticmethod
    def fn():
        return "My parent is the User"
    
    @classmethod
    def get_year(cls):
        return f"{cls.year}"

user1 = User("Stefan", "Blagojevic", "stefan@gmail.com", "qwerty")

# res = user1.get_info()
sm = User.fn()

# __str__
get_info = user1 # don't need to call the method .get_info()

print(get_info)
print("------------------------")
print(sm)
print(f"Year: {User.get_year()}")

print("------------------------")
