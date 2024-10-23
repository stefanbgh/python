### 31 ###
# functions
# => python3 src/parts/functions.py

from functions.hello import hello
from functions.change_money import change_money
from functions.full_name import full_name

hello("Person1", "Wazzzzzuppppppp?!")
hello("Person2", "Good morning!")
hello("Person3", "Good night.")
    
buy_euros = change_money(1200, "euro")
print(f"{buy_euros:.2f}€")

buy_rsd = change_money(buy_euros, "rsd")
print(f"{buy_rsd:.2f}rsd")

name = full_name("sTeFaN", "BlagoJEVIC")
print(name)
