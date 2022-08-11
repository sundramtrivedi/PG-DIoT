#Python Program to Print All Numbers in a Range Divisible by a Given Number

lower_range = int(input("Enter lower range number : "))
upper_range = int(input("Enter upper range number : "))
n = int(input("Enter division number : "))

for i in range(lower_range, upper_range+1):
	if(i%n == 0):
		print(i)
