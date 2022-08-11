#Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

n = int(input("Enter number : "))

for i in range(n):
	if(i%2 != 0 and i%3 != 0):
		print(i)
