###############################
##       100DaysOfCode       ##
##       d02_ecercice02      ##
###############################

# Pizza Order

print("\nWelcome to Python Pizza Deliveries!\n")
size = input("\nWhat size pizza do you want? S, M or L: ")
peperoni = input("\nDo you want peperoni? Y or N: ")
extra_cheese = input("\nDo you want extra cheese? Y or N: ")

init_price = 0
if size == 'S' or size == 's':
	init_price = 15
elif size == 'M' or size == 'm':
	init_price = 20
elif size == 'L' or size == 'l':
	init_price = 25

price  = init_price
if peperoni == 'Y' or  peperoni == 'y':
	if size == 'S' or size == 's':
		price += 2
	elif size == 'M' or size == 'm' or size == 'L' or size == 'l':
		price += 3
if extra_cheese == 'Y' or extra_cheese == 'y':
	price += 1

print(f"\nYour final bill is: ${price:.2f}")
