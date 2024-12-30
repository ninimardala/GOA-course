""" დავალება1:
ეცადეთ შექმნათ სარეგისტრაციო ფორმა,
შექმენით ინფუთები, რომლითაც მომხმარებელს მოსთხოვთ gmail-ს,
და
password-ს.
ასევე გამოიყენეთ and და or ოპერატოები."""


print("please go to registration")
Name = input("enter the name: ")

mail = input("enter the mail: ")

password = input("enter the password: ")
print("Registration was completed successfully")

print("login")

Name1 = input("enter the name: ")
password1 = input("enter the password: ")

if Name == Name1 and password == password1:
    print("login is completed")   
else:
    print("login is error")