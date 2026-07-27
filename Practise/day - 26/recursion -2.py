count = int(input("Enter Your Count :"))

def countdown(n):
    if n==0 :
        print('0 its done!')
        return

    print(n)
    countdown(n - 1)

countdown(count)