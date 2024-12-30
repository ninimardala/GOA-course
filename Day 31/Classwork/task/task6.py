"""მაქსიმალური რიცხვის პოვნა:
განსაზღვრეთ ფუნქცია სახელით find_max.
ფუნქციამ უნდა მიიღოს ორი პარამეტრი: num1 და num2 (ორივე მთელი ან წილადი რიცხვი).
ფუნქციამ უნდა შეადაროს ორი რიცხვი და დააბრუნოს მათი მაქსიმალური მნიშვნელობა."""

def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(find_max(10, 20))
print(find_max(25.5, 15.3))
print(find_max(-5, -10))
print(find_max(0, 0))
