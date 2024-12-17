def only_odd():
    n=int(input("enter a number: "))
    odd=[print(x, end=" ") for x in range(n+1) if x%2!=0]
only_odd()