#To Find The Factorial Of a Number
def probius_fact():
    num=int(input("Enter a number : "))
    fact=1
    a=1
    while a<=num:
        fact*=a
        a+=1
    print("The factorial of",num,"is",fact)
probius_fact()
