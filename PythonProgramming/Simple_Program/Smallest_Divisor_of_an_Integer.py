#Python Program to Find the Smallest Divisor of an Integer

n = int(input("Enter number : "))

for i in range(2, n+1):
	if(n%i == 0):
		break
print(i)
