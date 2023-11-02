#This code is created to let 2 input perform mathematical operations in Python. 
#Let's start

#Let user enter first number: 
num1 = float(input("Enter first number: "))

#Mathematical operations: 
print("Select one operation to perform: ")
print("1) +")
print("2) -")
print("3) x")
print("4) ÷")

ops = int(input("1,2,3 or 4 (Choose number only): "))

#Then, second number:
num2 = float(input("Enter second number: "))

#if-else statement:
if ops == 1: 
	total_1 = num1 + num2
	print("Addition:",num1,"+",num2)
	print("Answer: ",total_1)
elif ops == 2:
	total_2 = num1 - num2
	print("Substraction:",num1,"-",num2)
	print("Answer: ",total_2)
elif ops == 3:
	total_3 = num1 * num2
	print("Multiplication:",num1,"x",num2)
	print("Answer: ",total_3)
elif ops == 4: 
	total_4 = num1 / num2
	print("Division:",num1,"÷",num2)
	print("Answer: ",total_4)
else:
	print("Something is wrong, please try again...")
