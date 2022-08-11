# Python Program to Find Whether a Number is a Power of Two

n = int(input("Enter number : "))

flag = 0

for i in range(0, n + 1):
	if(2**i == n):
		flag = 1
		break
		
	else:
		flag = 0
		
if(flag == 1):
	print("Number is a power of 2")
else:
	print("Number is not a power of 2")
		 
