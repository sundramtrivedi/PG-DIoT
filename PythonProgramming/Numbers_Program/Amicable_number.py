# Python Program to Check If Two Numbers are Amicable Numbers or Not.

n1 = int(input("Enter num1 : "))

n2 = int(input("Enter num2 : "))

sum1 = 0

sum2 = 0

for i in range(1, n1+1):
	if(n1%i == 0):
		sum1 = sum1 + i
print(sum1)
		
for j in range(1, n2+1):
	if(n2%j == 0):
		sum2 = sum2 + j
print(sum2)

if(sum1 == sum2):
	print("Number is Amicable")
else:
	print("Number is not Amicable")
