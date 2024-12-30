"""შექმენით ფუქნცია და შეამოწმეთ რიცხვი ლუწია თუ კენტი."""

def check_parity(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
try:
    number = int(input("შეიყვანეთ რიცხვი: "))
    parity = check_parity(number)
    print(f"რიცხვი {number} არის {parity}.")
except ValueError:
    print("შეიყვანეთ ვალიდური მთელი რიცხვი.")
