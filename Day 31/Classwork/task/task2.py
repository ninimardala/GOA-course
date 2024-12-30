"""შექმენით ფუნქცია,
რომელიც მიესალმება მომხმარებელს.
ტექსტი: 'გამარჯობა {სახელი},
კეთილი იყოს შენი მობრძანება,
გისურვებ წარმატებას და წინ სვლას"""

name = input("enter name: ")

def greet_user(name):
    greeting_message = f"გამარჯობა {name}, კეთილი იყოს შენი მობრძანება, გისურვებ წარმატებას და წინ სვლას"
    return greeting_message

user_name = name
print(greet_user(user_name))