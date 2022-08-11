# Python Program to Find Prime Numbers in a Given Range

lower_range = int(input("Enter lower range number : "))

upper_range = int(input("Enetr upper range number : "))

for a in range(lower_range, upper_range + 1):

	k = 0

	for i in range(2, a//2 + 1):
		if(a%i == 0):
			k = k + 1
				
	if(k <= 0):
		print(a, "Number is prime number")
	else:
		print(a, "Number is not prime number")
