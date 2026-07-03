num_1 = int(input("Enter the number 1:"))
num_2 = int(input("Enter the number 2:"))

operation = input("Enter the operation :")

match operation:
    case "+":
        print(num_1 + num_2)
    case "-":
        print(num_1 - num_2)
    case "*":
        print(num_1 * num_2)
    case "/":
        print(num_1 / num_2)