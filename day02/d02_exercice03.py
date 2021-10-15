###############################
##       100DaysOfCode       ##
##       d02_ecercice03      ##
###############################

# Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("\nWhat is your name? ")
name2 = input("What is their name? ")

lower_names = name1.lower() + name2.lower()

decimal = lower_names.count('t') + lower_names.count('r') + lower_names.count('u') + lower_names.count('e')
unit = lower_names.count('l') + lower_names.count('o') + lower_names.count('v') + lower_names.count('e')

score = int(str(decimal) + str(unit))

# For Love Scores less than 10 or greater than 90, the message should be:
if score < 10 or score > 90:
	print(f"\nYour score is {score}, you go together like coke and mentos.")
# For Love Scores between 40 and 50, the message should be:
elif score >= 40 and score <= 50:
	print(f"\nYour score is {score}, you are alright together.")
# Otherwise, the message will just be their score
else:
	print(f"\nYour score is {score}.")
