factorial_no = int(input("Eneter the factorial no:"))

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(factorial_no))