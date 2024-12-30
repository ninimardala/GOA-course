"""შექმენით ფუნქცია რომელიც, გამოიტანს მხოლოდ event, ხოლო კენტზე odd_ს"""
while True:
 num = int(input("enter number: "))

 if num % 2 == 0:
        print (str(num) + " " + "is event")
 else :
    print (str(num) + " " + "is odd")
