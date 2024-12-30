"""შექმენით ფუნქცია,
რომელიც გამოიტანს x და y ჯამს,
მოახდინეთ ოპერაცია შემდეგ ოპერატორებზე: +, -. *. //"""

x = int(input("enter number: "))
y = int(input("enter number2: "))

def calculate_operations(x, y):
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    integer_division = x // y
    
    return addition, subtraction, multiplication, integer_division


results = calculate_operations(x, y)

print(f"ჯამი (x + y): {results[0]}")
print(f"განსხვავება (x - y): {results[1]}")
print(f"გამრავლება (x * y): {results[2]}")
print(f"მთელი ნაწილი (x // y): {results[3]}")
