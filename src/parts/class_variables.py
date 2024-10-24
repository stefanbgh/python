### 47 ###
# class

print("------------------------")
class User:
    year = 2024

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_info(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nPassword: {self.password}"
    
    @staticmethod
    def fn():
        return "My parent is the User"

user1 = User("Stefan", "Blagojevic", "stefan@gmail.com", "qwerty")

res = user1.get_info()
sm = User.fn()

print(res)
print("------------------------")
print(sm)

print("------------------------")
