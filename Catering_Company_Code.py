import math

people = int(input("Hello, how many people do you want to cater for? "))

chicken = 15.00
beef = 20.00
fries = 5.00
mashed_potatoes = 7.00
rice = 4.00

tax_rate = 0.13
discount = 0.10 if people > 10 else 0

if people > 20 or people <= 1:
    print("Sorry, we can only cater for up to 19 people.")
    exit()

food = input("What type of food would you like to have, chicken or beef? ").lower()
if food == "chicken":
    chicken_side = input("What side would you like with the chicken, rice or fries? ").lower()

    Tip = input("How much would you like to tip? ")
    if Tip == "0":
        print("No tip, no problem!")
    else:
        print("Thank you")
    if chicken_side == "rice":
        total_cost = (((chicken + rice) * people) * (1 + tax_rate)) * (1 - discount) + float(Tip)
    else:
        total_cost = (((chicken + fries) * people) * (1 + tax_rate)) * (1 - discount) + float(Tip)
    total_cost = round(total_cost, 2)
    print(f"You have ordered {people} servings of chicken with {chicken_side}. Your total will be: ${total_cost}")
elif food == "beef":
    beef_side = input("What side would you like with the beef, mashed potatoes or fries? ").lower()

    Tip = input("How much would you like to tip? ")
    if Tip == "0":
        print("No tip, no problem!")
    else:
        print("Thank you for your generosity!")
    if beef_side == "mashed potatoes":
        total_cost = (((beef + mashed_potatoes) * people) * (1 + tax_rate)) * (1 - discount) + float(Tip)
    else:
        total_cost = (((beef + fries) * people) * (1 + tax_rate)) * (1 - discount) + float(Tip)
    total_cost = round(total_cost, 2)
    print(f"You have ordered {people} servings of beef with {beef_side}. Your total will be: ${total_cost}")
else:
    print("Sorry, we only serve chicken or beef.")
