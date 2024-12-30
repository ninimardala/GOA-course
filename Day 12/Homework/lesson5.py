"""6)  input() ფუნქციის დახმარებით მომხმარებელს შემოაქვს ორი რიცხვი a და b.
for ციკლის გამოყენებით ტერმინალში გამოიტანეთ რიცხვები a-დან b-მდე
( range(a, b) )"""

a = int(input("enter number: "))
b = int(input("enter number: "))

for i in range(a, b):
    print(i)
