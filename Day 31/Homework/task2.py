"""გამოთვალეთ მართკუთხედის ფართობი
შექმენით ფუქნქცია, რომელსაც ეწოდება calculate_area
ამ ფუნქციაში უნდა იყვეს ორი პარამეტრი, length და width
 გამოიყენეთ ფორმულა, area = length * width """

def calculate_area(length, width):
    area = length * width
    return area
length = float(input("შეიყვანეთ მართკუთხედის სიგრძე: "))
width = float(input("შეიყვანეთ მართკუთხედის სიგანე: "))
area = calculate_area(length, width)
print(f"მართკუთხედის ფართობია: {area}")