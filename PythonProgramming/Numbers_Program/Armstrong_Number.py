# Python Program to Check Armstrong Number

n = int(input("Enter number : "))

temp = n

sum = 0

while( n > 0):
	dig = n % 10
	sum = sum + dig * dig * dig
	n = n // 10
print(sum)
if( sum == temp):
	print("Number is armstrong")
else:
	print("Number is not armstrong")


