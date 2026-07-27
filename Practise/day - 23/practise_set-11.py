text = "coding in python is fun"

sum = 0

vowels = ("a", "e", "i", "o", "u")

for char in text :
    if (char in vowels) :
        sum +=1

print(f"Thers are {sum} vowels in this sentence")