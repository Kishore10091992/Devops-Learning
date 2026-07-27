def average(maths, tamil, english, social, science) :
    average = (maths + tamil + english + social + science) / 5
    print(f"Average mark is {average}")

maths = int(input("Enter Your Maths Mark :"))

tamil = int(input("Enter Your Tamil Mark :"))

english = int(input("Enter Your English Mark :"))

social = int(input("Enter Your Social Mark :"))

science = int(input("Enter Your Science Mark :"))

average(maths, tamil, english, social, science)