# import statement

import pandas as pd
import docx

# -----------------------------------------------------------------------------------------------------------------------
# creating the dictionary that contain key as work name and values as their prize


price = {"DMLS": 600, "METAL FREE": 1800, "PFM": 350
    , "FLEXIBLE": 0, "RPD": 600, "ORTHO": 700, "REPAIR": 150, "DENTAL REPAIR": 150
    , "CD": 600, "ZIRCONIA": 1800}

# -----------------------------------------------------------------------------------------------------------------------
# displaying the amounts of work to user, so he can check and decide whether he has to change the prize or not

s1 = pd.Series(price)
print("-" * 40 + "⚫ PRICE" + "-" * 40 + '\n')
print(s1)
print('-' * 87)

# ------------------------------------------------------------------------------------------------------------------------------
# asking for add work dfining function
def general_asking(x):
    while True:
        add_work = input(f"DO YOU WANT TO {x} [Y/N] = ")
        if len(add_work) != 1:
            #or not add_work.isalpha() or add_work not in ['Y', 'N', 'y', 'n']:
            print("INVALID INPUT :- PLEASE ENTER A SINGLE CHARACTER !")
        elif not add_work.isalpha():
            print("INVALID INPUT :- PLEASE ENTER ALPHABET ONLY AVOID SYMBOL , NUMBERS ETC !")
        elif add_work not in ['Y', 'N', 'y', 'n']:
            print("INVALID INPUT :- ENTER ONLY [Y/N]")
        else:
            break
    return add_work

# calling this
ask = general_asking("ADD WORK")
# ------------------------------------------------------------------------------------------------------------------------------
# defining a function that take new price and work input and append to dictionary

def new_work_add():
    while True:
        new_work = input("ENTER WORK = ")
        new_price = input("ENTER PRICE = ")
        if not new_work.isalpha() or not new_work.isalnum():
            print("ENTER A VALID WORK NAME (NO NUMBERS OR SPECIAL CHARACTERS ALLOWED)!")
        elif not new_price.isdigit() or int(new_price) <= 0:
            print("ENTER A VALID PRICE (POSITIVE INTEGER ONLY)!")
        elif new_work in price:
            print("WORK ALREADY EXISTS. PLEASE ENTER A DIFFERENT WORK NAME.")
        else:
            print("SUCCESSFULLY ADDED ✔")
            print('-'*87)
            price.update({new_work: int(new_price)})
            print(s1)
            break

# ------------------------------------------------------------------------------------------------------------------------------
# defining function that will take the number that how many changes he want to perform

def how_many_changes(z):
    while True:
        # asking user how many new work he wants to add

        y = input(f"HOW MANY WORK YOU WANT TO {z} =  ")

        if not y.isdigit():
            print("PRINT ENTER A VALID NUMBER !")

        else:
            print('-'*87)
            integer_converted = int(y)
            break

    return integer_converted



# ------------------------------------------------------------------------------------------------------------------------------

# now if user enter yes then it append and take prize ,etc

if ask.lower() == "y":
    print('-'*87)
    integer_converted = how_many_changes("ADD")


    for i in range(integer_converted):
        new_work_add()

# ------------------------------------------------------------------------------------------------------------------------------

# SECTION - B / price changes

# ------------------------------------------------------------------------------------------------------------------------------

# WRITING CODE FOR any prize changes

# ------------------------------------------------------------------------------------------------------------------------------

#print('-'*87)
price_changes = general_asking("CHANGE PRICE")

if price_changes.lower() == "y":
    integer_converted = how_many_changes("CHANGE")
    for i in range(integer_converted):
        tell_me_work_to_change = input("ENTER THE WORK NAME TO CHANGE = ")
        tell_me_price_of_work = input("ENTER THE NEW PRICE = ")
        price[tell_me_work_to_change] = tell_me_price_of_work

print('_'*87)
print(s1)
