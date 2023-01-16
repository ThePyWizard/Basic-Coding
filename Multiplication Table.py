# For multiplication table
def probius_multi():
    print("For multiplication table")
    b=int(input("Enter a number for the multiplication table : "))
    n=int(input("Enter a limit 10 or more than 10 as you like : "))
    for i in range(1,n+1):
        j=i*b
        print(i,'x',b,'=',j)
probius_multi()