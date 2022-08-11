# Python Program to Check Whether a Given Number is Perfect Number

n = int(input("Enter number : "))

temp = n

k = 0

for i in range(1, n):
	if(n%i == 0):
		k = k + i

if(k == temp):
	print("Number is perfect")
else:
	print("Number is not perfect")	

