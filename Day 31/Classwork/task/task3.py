"""შექმენით ფუნქცია,
რომელიც სიყვარულის წერილს მიუძღვნის მომხმარებელს:
ტექსტი თქვენ მოიფიქრეთ.
ტექსტის ბოლოს აუცილებლად ჩაამატეთ ეს ნაწილი: 'სიყვარულით {სახელი}' """

name = input("enter name: ")
name1 = input("enter your name: ")
def სიყვარული_წერილი(სახელი):
    წერილი = (
        f"ძვირფასო {სახელი},\n\n"
        "გამარჯობა! "
        "ძალიან ძალიან მენატრები .\n\n"
        "და ძალიან ძალიან მივარხარ ერთი სული მაქვს როდის გნახავ.\n\n"
        f"სიყვარულით, {name1}სგან"
    )
    return წერილი

# ფუნქციის გაწვდვის მაგალითი:
print(სიყვარული_წერილი(name))
