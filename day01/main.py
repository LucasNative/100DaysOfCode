###############################
##       100DaysOfCode       ##
##       Day01               ##
###############################

# Tip calculator

print("\nWelcome to the Tip Calculator\n")
bill = int(input("What was the total bill? "))
percent = int(input("What percentage would you like to give? "))
peoples = int(input("How many people to split the bill? "))

amount = bill * (percent / 100 + 1)
total = amount // peoples
print(f"\nEach person should pay: ${total}")


