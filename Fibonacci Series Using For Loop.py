#To Print The n Fibonacci Series
def probius_fib():
    n=int(input("Enter the limit for the fibonaacci series : "))
    x=0
    y=1
    print(x)
    print(y)
    for i in range(1,n-1):
        z=x+y
        print(z)
        x,y=y,z
probius_fib()
