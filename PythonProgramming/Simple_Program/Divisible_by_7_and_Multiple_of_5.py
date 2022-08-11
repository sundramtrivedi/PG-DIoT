#Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

lower_range = int(input("Enter lower range number : "))
upper_range = int(input("Enter upper range number : "))

for i in range(lower_range, upper_range+1):
	if(i%7 == 0 and i%5 == 0):
		print(i)


