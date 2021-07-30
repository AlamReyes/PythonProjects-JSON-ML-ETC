# This program is a tip calculato
quit = False
while quit == False:
    yn = input("Do you wanna give a tip: ")

    if yn == "no":
        print("Thank you for your preferences, have a nice day.")

    elif yn == "yes":
        print("The percentage amount you can select are: \n5% \n10% \n20% \n30% ")
        tip = int(input("Please, write the percentage of the tip:"))
        total = float(input("Please, write the total of your bill:"))
        if tip == 5:
            convertion_tip = .05*total
            convertion_total = convertion_tip + total
            print("The total of your bill is $" , convertion_total , ". The amount of tip you are giving is $" , convertion_tip )
            print("\n Thank you, have a nice day!.")
            break

        elif tip == 10:
            convertion_tip = .10*total
            convertion_total = convertion_tip + total
            print("The total of your bill is $" , convertion_total , ". The amount of tip you are giving is $" , convertion_tip )
            print("\n Thank you, have a nice day!.")
            break

        elif tip == 20:
            convertion_tip = .20*total
            convertion_total = convertion_tip + total
            print("The total of your bill is $" , convertion_total , ". The amount of tip you are giving is $" , convertion_tip )
            print("\n Thank you, have a nice day!.")
            break

        elif tip == 30:
            convertion_tip = .30*total
            convertion_total = convertion_tip + total
            print("The total of your bill is $" , convertion_total , ". The amount of tip you are giving is $" , convertion_tip )
            print("\n Thank you, have a nice day!.")
            break
    else:
        print("Write yes or no, please")

else:
    quit = True




