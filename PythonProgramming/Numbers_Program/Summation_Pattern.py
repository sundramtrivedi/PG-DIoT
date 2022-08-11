# Python Program to Print the Natural Numbers Summation Pattern.

n = int(input("Enter number : "))

sum = 0 

pattern = ""

for i in range(1, n + 1):
	sum += i
	if(i == 1 or i == (n + 1)):
		pattern += str(i)  
	else:
		pattern += " + " + str(i)
	print(pattern , " = " , sum)
