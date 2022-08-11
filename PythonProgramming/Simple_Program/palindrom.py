#Python Program to Check if a Number is a Palindrome

n = int(input("Enter any number : "))

temp = n

rev = 0

while(n > 0):
	dig = n % 10
	rev = rev * 10 + dig
	n = n // 10
print(rev)

if(temp == rev):
	print("Number is palindrom")
else:
	print("Number is not palindrom")
