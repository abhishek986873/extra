# import statement
import pandas as pd
import docx

# -----------------------------------------------------------------------------------------------------------------------
# creating the dictionary that contain key as work name and values as their prize

price = {"(1) DMLS = ": 600, "(2) METAL FREE = ": 1800, "(3) PFM = ": 350
    , "(4) FLEXIBLE = ": 0, "(5) RPD = ": 600, "(6) ORTHO = ": 700, "(7) REPAIR = ": 150, "(8) DENTAL REPAIR = ": 150
    , "(9) CD = ": 600, "(10) ZIRCONIA = ": 1800}

# -----------------------------------------------------------------------------------------------------------------------
# displaying the amounts of work to user, so he can check and decide whether he has to change the prize or not

s1 = pd.Series(price)
print("-" * 40 + "⚫ PRICE" + "-" * 40 + '\n')
print(s1)
print('-' * 87)

# ------------------------------------------------------------------------------------------------------------------------------
# asking for add work
while True:
    add_work = input("DO YOU WANT TO ADD WORK [Y/N] = ")
    if not add_work.isalpha() or add_work not in ['Y', 'N', 'y', 'n']:
        print("PLEASE ENTER A VALID INPUT !")
    else:
        break

# ------------------------------------------------------------------------------------------------------------------------------

if add_work == "Y" or add_work == 'y':
    how_many_changes = int(input("HOW MANY PRICE  YOU WANT TO ADD =  "))
    i = 0
    while i < how_many_changes:
        while True:
            new_work = input("ENTER WORK = ")
            new_price = input("ENTER PRICE = ")
            if not new_work.isalpha() or not new_price.isdigit():
                print("ENTER A VALID [PRICE OR WORK] !")
            else:
                price.update({new_work: int(new_price)})
                break
        i = i + 1



        # else:
# updating the index with new price


