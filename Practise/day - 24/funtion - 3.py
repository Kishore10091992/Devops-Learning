def average(maths, english, tamil, social, science) :
    return(maths + english + tamil + social + science) / 5

maths = int(input("Enter Your Maths Mark :"))

english = int(input("Enter Your English Mark :"))

tamil = int(input("Enter Your Tamil Mark :"))

social = int(input("Enter Your Social Mark :"))

science = int(input("Enter Your Science Mark :"))

avg = average(maths, english, tamil, social, science)

print(f"Your Average Mark Is : {avg}")