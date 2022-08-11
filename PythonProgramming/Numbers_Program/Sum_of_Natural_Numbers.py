# Python Program to Find Sum of First N Natural Numbers

n = int(input("Enter number : "))

sum = 0

for i in range(1, n+1):
	sum = sum + i
print("Sum of First", n, "Natural Number is : ", sum)
