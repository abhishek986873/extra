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
# asking for add work
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
            #price.update({new_work: int(new_price)})
            price[new_work] = int(new_price)
            break

# ------------------------------------------------------------------------------------------------------------------------------
# now if user enter yes then it append and take prize ,etc

if ask.lower() == "y":
    print('-'*87)
    while True:
        # asking user how many new work he wants to add

        how_many_changes = input("HOW MANY PRICE  YOU WANT TO ADD =  ")
        if not how_many_changes.isdigit():
            print("PRINT ENTER A VALID NUMBER !")

        else:
            print('-'*87)
            integer_converted = int(how_many_changes)
            print(price)
            break
    # using for loop to take x times of work and price and append it to dictionary

    for i in range(integer_converted):
        new_work_add()

# ------------------------------------------------------------------------------------------------------------------------------

# SECTION - B / price changes

# ------------------------------------------------------------------------------------------------------------------------------

# WRITING CODE FOR any prize changes

# ------------------------------------------------------------------------------------------------------------------------------

#print('-'*87)
price_changes = general_asking("CHANGE PRICE")

