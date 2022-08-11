#Python Program to Calculate Grade of a Student

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 1 : "))
n3 = int(input("Enter number 1 : "))
n4 = int(input("Enter number 1 : "))
n5 = int(input("Enter number 1 : "))

avg = (n1+n2+n3+n4+n5)

if(avg>90):
	print("Grade A")
elif(avg>80):
	print("Grade B")
elif(avg>70):
	print("Grade C")
elif(avg>60):
	print("Grade D")
else:
	print("Fail")
