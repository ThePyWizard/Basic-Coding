#Factorial of a number using while loop
print("For factorial of a number")
a=int(input("Enter a number : "))
c=1
for i in range(1,a):
  c+=c*i
print("The factorial of number",a,"is",c)
