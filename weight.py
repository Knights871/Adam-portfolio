import math

total_weight_kg = int(input("What is your total weight in kg? "))
clothes_weight_kg = int(input("What is the weight of your clothes in kg? "))
body_weight_kg = total_weight_kg - clothes_weight_kg
print(str(body_weight_kg) + " kg")

if total_weight_kg - clothes_weight_kg < 65:
    print("You don't have to lose weight")
else:
    print("You have to lose weight")
if total_weight_kg > 65:
    str_inp = str(input("Do you want to lose weight? Yes or No? "))
    if str_inp != "Yes" and str_inp != "No":
        print("Only Yes or No, dummy!!")
        exit()
    elif str_inp == "Yes":
        print("You should exercise more or eat less")
    elif str_inp == "No":
        print("You should try and lose weight")
    else:
        print('what??')
        
    weight_in_kg= body_weight_kg
    weight_in_lbs = (body_weight_kg * 2.2 )
    value_1 = weight_in_kg
    value = weight_in_lbs
    rounded_value_1 = round(value_1, ndigits=3)
    rounded_value = round(value, ndigits=3)
    print(str(rounded_value_1) + "kg" +" " + str(rounded_value) + "lbs")

else :
    print("You should keep your current diet and exercise routine")
