# Python Program to Check if a Number is a Strong Number

n = int(input("Enter number : "))

temp = n

sum = 0

while(n > 0):
	fact = 1
	dig = n % 10
	for i in range(1, dig + 1):
		fact = fact * i
	sum = sum + fact
	n = n // 10 
print(fact)
print(sum)
if(temp == sum):
	print("Number is strong")
else:
	print("Number is not strong")
