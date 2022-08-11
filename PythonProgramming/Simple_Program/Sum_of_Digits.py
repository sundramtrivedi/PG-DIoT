#Python Program to Find Sum of Digits of a Number

n = int(input("Enter number : "))

sum = 0

while( n > 0):
	dig = n % 10
	sum = sum + dig
	n = n // 10
print(sum)
