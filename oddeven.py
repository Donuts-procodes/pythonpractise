def is_odd(n):
    if n==1:
        print(f"{n} is odd")
        return True
    elif n%2==0:
        print(f"{n} is even")
        return False
    else:
        print(f"{n} is odd")
        return True

print(is_odd(10))