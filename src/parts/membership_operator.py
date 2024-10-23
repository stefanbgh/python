### 35 ###
# membership operator

print("--------------------------------------")

# example 1
word = "qwerty"

letter = input("Guess a latter in the secret word: ")

def checkLetter(letter):
    if letter not in word:
        return f"{letter} was not found."
    
    return f"There is a \"{letter}\"." # or f'There is a \"{letter}\".'

cl = checkLetter(letter)
print(cl)

print("--------------------------------------")

# example 2

email = input("Enter a email address: \n- ")

def validEmail(email):
    if "@" in email and "." in email:
        return "Valid email"
    
    return "Invalid email"

ve = validEmail(email)
print(f"# {ve}")

print("--------------------------------------")
