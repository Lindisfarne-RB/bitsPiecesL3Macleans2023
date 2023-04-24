def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input an integer")


def validate_text_input(prompt, options):
    while True:
        try:
            text_input = input(prompt)
            return text_input
        except TypeError:
            print("Please enter text")


input_saving_goal = True
while input_saving_goal:

    # input salary type and calculating weekly income
    while True:
        try:
            saving_goal = int(input("Enter your saving goal"))

        except ValueError:
            print("Please input a number")
        # type_of_income = ""
        print("----------------------------")

        type_of_income = ""
        while type_of_income not in ["hourly", "annual"]:
            type_of_income = validate_text_input(
                """Do you have hourly wage or annual salary?
        Please input 'hourly' or 'annual'. """, ["hourly", "annual"])

            if type_of_income == "hourly":
                while True:
                    try:
                        hours_per_week = float(input("How many hours do you work per week?"))
                        if hours_per_week > 0:
                            break
                    except ValueError:
                        print("input a number")

                while True:
                    try:
                        hourly_wage = float(input("What is your hourly wage?"))
                        if hourly_wage > 0:
                            break
                    except ValueError:
                        print("input a number")

                weekly_income = hours_per_week * hourly_wage
                print("Weekly income =", weekly_income)


            elif type_of_income == "annual":
                # write code to calculate weekly income if you have annual salary
                while True:
                    try:
                        annual_salary = validate_float("What is your annual salary?")
                        if annual_salary > 0:
                            break
                    except ValueError:
                        print("Please input a number")
                weekly_income = annual_salary / 52
                print("Weekly income", weekly_income)

            else:
                pass

            tax_rate = float(input("What is your tax rate"))
            tax_multiplier = (100 - tax_rate) / 100
            income_after_tax = weekly_income * tax_multiplier

            weekly_rent = validate_float("How much is your weekly rent")
            weekly_food = validate_float("How much is your weekly expense on food")
            weekly_social = validate_float("How much is your weekly expense on socials")
            weekly_hobby = validate_float("How much is your weekly expense on hobbies")
            total_weekly_expense = weekly_hobby + weekly_social + weekly_food + weekly_rent

            weekly_saving = weekly_income - total_weekly_expense

            if weekly_saving > 0:
                weeks_to_goal = saving_goal / weekly_saving
                print("Thank you for using saving calculator")
                print("Your saving goal is $ {}".format(saving_goal))

                print("You save $ {}".format(weekly_saving))

                print("It will take {} weeks for you to save for your goal".format(weeks_to_goal))

        # ask the user to run the program again
        use_again = input("Do you wish to use this program again Press Y or N")
        if use_again == 'Y':
            input_saving_goal = True
        else:
            print("Thank you for using my program")
            input_saving_goal = False
            break
