# Python Program to Check if a Date is Valid and Print the Incremented Date if it is.

date = int(input("Enter any date : "))

if( date <= 31 and date > 0):
	new_date = date + 1
	print("Next date is : " , new_date)
else: 
	print("Please enter valid date")
