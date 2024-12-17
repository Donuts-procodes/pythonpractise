def palindrome(x: str):
    for i in range(len(x) // 2): 
        if x[i] != x[len(x) - i - 1]: 
            print("It is not a palindrome")
            return
    print("It is a palindrome")
palindrome("abcbca")
