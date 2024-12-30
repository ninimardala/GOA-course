"ლუწი და კენტ რიცხვთა სიის პოვნა შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ორ ცალკე სიას – ერთში იქნებიან ლუწი რიცხვები, ხოლო მეორეში კენტი რიცხვები."

from typing import List, Tuple
def separate_even_odd(numbers: List[int]) -> Tuple[List[int], List[int]]:
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers, odd_numbers
example_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = separate_even_odd(example_numbers)
print("ლუწი რიცხვები:", even_numbers)
print("კენტი რიცხვები:", odd_numbers)