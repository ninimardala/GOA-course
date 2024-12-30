def animal_ages(humanYears):

    catYears = 0
    dogYears = 0

    if humanYears >= 1:
        catYears += 15
        dogYears += 15

    if humanYears >= 2:
        catYears += 9
        dogYears += 9

    if humanYears > 2:
        catYears += (humanYears - 2)
        dogYears += (humanYears - 2)
    
    return [humanYears, catYears, dogYears]

print(animal_ages(1))
print(animal_ages(2))
print(animal_ages(10))