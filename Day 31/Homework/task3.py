"""მაქსიმალური რიცხვის პოვნა:
განსაზღვრეთ ფუნქცია სახელით find_max.
ფუნქციამ უნდა მიიღოს ორი პარამეტრი: num1 და num2 (ორივე მთელი ან წილადი რიცხვი).
ფუნქციამ უნდა შეადაროს ორი რიცხვი და დააბრუნოს მათი მაქსიმალური მნიშვნელობა."""

def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
max_value = find_max(num1, num2)
print(f"მაქსიმალური რიცხვია: {max_value}")
