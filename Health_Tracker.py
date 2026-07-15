
def health_tracker():
    age = int(input("What is your age? "))
    if age < 18:
        print("Sorry, this program is only for adults.")
        return
    starting_weight = float(input("Enter your starting weight (in pounds): "))
    ending_weight = float(input("Enter your ending goal weight (in pounds): "))
    daily_calories = float(input("How many calories do you eat in a day? "))
    
    # Weight-loss goal
    weight_loss_goal = starting_weight - ending_weight


    maintenance_calories = 15 * starting_weight

    # Daily deficit
    daily_deficit = maintenance_calories - daily_calories

    if daily_deficit <= 0:
        print("You are eating too many calories to lose weight.")
    else:
        print("You are on track to lose weight.")
        return
  # Total calorie deficit needed to lose 1lb of fat
    total_calorie_deficit = weight_loss_goal * 3500

    # Days needed
    days_to_goal = total_calorie_deficit / daily_deficit

    print("Your goal is to lose",weight_loss_goal," pounds.")
    print("Your daily calorie deficit is",daily_deficit," calories.")
    print("It will take about",days_to_goal, "days to reach your goal.")
health_tracker()
