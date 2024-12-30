"""დავალება2:  ეცადეთ შექმნათ კალკულატორი პითონში."""

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
operation = input("(+ - 1)(- - 2)(* - 3)(/ - 4): ")

if operation == "1":
    print (num1 + num2)
elif operation == "2":
    print (num1 - num2)
elif operation == "3":
    print (num1 * num2)
elif operation == "4":
    print (num1 / num2)
else:
    print ("invalid option")