#This Python code will ask the user's age and its category according to their age.
#Source: I don't remember but I found it on Google. Correct me if I'm wrong. 

age = int(input("Dear human, please enter your age: "))

category_a = "baby"
category_b = "young adults"
category_c = "middle age adults"
category_d = "old adults"

if age >= 0 and age <= 2:
	print("Your age is",age)
	print("You're in",category_a, "category")
	print("How cute! :)")
elif age >= 3 and age <= 39:
	print("Your age is",age)
	print("You're in",category_b, "category")
elif age >= 40 and age <= 59:
	print("Your age is",age)
	print("You're in",category_c, "category")
elif age >= 60:
	print("Your age is",age)
	print("You're in",category_d, "category")
else: 
	print("Something is wrong, please try again...")
