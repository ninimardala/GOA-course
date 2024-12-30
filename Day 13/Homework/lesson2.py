"""დაწერეთ პირობითი დებულება, რომელიც ამოწმებს რიცხვი დადებითია, უარყოფითი ან ნული. 
დაბეჭდეთ შესაბამისი შეტყობინება თითოეული შემთხვევისთვის."""

num = int(input("enter number: "))

if num > 0:
    print ("number is positive")
elif num < 0:
    print ("number is negative")
elif num == 0:
    print ("number is 0")
