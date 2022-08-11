#Python Program to Print All Odd Numbers in a Range

n = int(input("Enter number : "))
for i in range(n):
	if(i%2 != 0):
		print(i)
