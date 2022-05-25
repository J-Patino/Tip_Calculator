print("Welcome to the tip calculator!")

total = float( input("What was your total bill? $") )

tip = int (input("What percentage tip would you like to give? ") )

people = int ( input("How many people to split the bill? ") )

final_amount = round((total + (tip/100 * total)) / people, 2)

print(f"Each person should pay: ${final_amount} ")


