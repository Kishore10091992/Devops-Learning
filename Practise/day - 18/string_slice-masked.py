api_key = input("Enter the api key :")

masked = "*" * 10 + api_key[-4:]

print(masked)