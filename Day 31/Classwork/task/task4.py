"""შექმენით ფუნქცია,
სადაც შემოიტანთ თქვენს თავზე ინფორმაცია,
სახელი, გვარი, ასაკი, ქვეყანა, ქალაქი, საყვარელი ჰობი და ა.შ"""

saxeli = input("enter name: ")
gvari = input("enter lastname: ")
asaki = input("enter age: ")
qveyana = input("enter country: ")
qalaqi = input("enter city: ")
hobi = input("enter hobi: ")
def შექმენი_ბიოგრაფია(სახელი, გვარი, ასაკი, ქვეყანა, ქალაქი, საყვარელი_ჰობი):
    ბიოგრაფია = (
        f"გამარჯობა! მე ვარ {saxeli} {gvari}.\n"
        f"მე ვარ {asaki} წლის და წარმოშობით {qveyana}-დან ვარ. ამჟამად ვცხოვრობ {qalaqi}-ში.\n"
        f"ჩემი საყვარელი ჰობი არის {hobi}"
    )
    return ბიოგრაფია

print(შექმენი_ბიოგრაფია(saxeli, gvari, asaki, qveyana, qalaqi, hobi))