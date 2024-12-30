"""გამოთვალეთ მართკუთხედის ფართობი
შექმენით ფუქნქცია, რომელსაც ეწოდება calculate_area

ამ ფუნქციაში უნდა იყვეს ორი პარამეტრი, length და width

 გამოიყენეთ ფორმულა, area = length * width """

def calculate_area(length, width):
    area = length * width
    return area

length = 5
width = 3
print(f"მართკუთხედის ფართობია: {calculate_area(length, width)}")