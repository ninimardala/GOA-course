"""6)  input() ფუნქციის დახმარებით მომხმარებელს შემოაქვს ორი რიცხვი a და b.
while ციკლის გამოყენებით ტერმინალში
გამოიტანეთ რიცხვები
a-დან b-მდე"""


a = int(input("enter number: "))
b = int(input("enter number: "))

while  a <= b:
    print(a)
    a += 1