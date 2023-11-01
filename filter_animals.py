animals = ['cat', 'dog', 'canary', 'chihuahua', 'narwhal']
filtered_animals = []
for animal in animals:
    if(animal[:1]=='c'):
        capital_animal = animal.upper()
        print (capital_animal)
        filtered_animals.append(capital_animal)
        length = len(filtered_animals)
txt = "Number of C-animals: {}"
print(txt.format(length))