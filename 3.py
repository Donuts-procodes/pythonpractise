def is_prime(n):
        for i in range (2,n,1):
            if (n%i==0):
                print(f"{n} is not prime")
                return False
            else:
                print(f"{n} is prime")
                return True

x=is_prime(5)
print(x)