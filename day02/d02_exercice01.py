###############################
##       100DaysOfCode       ##
##       d02_exercice01      ##
###############################

# Leap year

def leap(ayear):
	if ayear % 4 == 0:
		if ayear % 100 == 0:
			if ayear % 400 == 0:
				print("Leap year")
			else:
				print("Not eap year")
		else:
			print("Leap year")
	else:
		print("Not leap year")

while year != "y":
	year = int(input("\nWich year do you want to check? "))
	leap(year)
	exit = input("\nWant exit? y/n: ")
