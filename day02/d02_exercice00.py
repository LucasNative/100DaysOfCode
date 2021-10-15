###############################
##       100DaysOfCode       ##
##       d02_exercice00      ##
###############################

# BMI calculator


height = float(input("\nEnter your heigtht in m: "))
weight = float(input("Enter your wight in kg: "))

bmi = weight / (height * height)


if bmi <= 18.5:
	print(f"\nYour BMI is {bmi:.2f}, you are underweight.\n")
elif bmi > 18.5 and bmi <= 25:
	print(f"\nYour BMI is {bmi:.2f}, you have a normal weight.\n")
elif bmi > 25 and bmi <= 30:
	print(f"\nYour BMI is {bmi:.2f}, you are slightly overweight.\n")
elif bmi > 30 and bmi <= 35:
	print(f"\nYour BMI is {bmi:.2f}, you are obese.\n")
else:
	print(f"\nYour BMI is {bmi:.2f}, you are clinically obese.\n")
