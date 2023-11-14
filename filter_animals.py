animals = ['cat', 'dog', 'canary', 'chihuahua', 'narwhal']
filtered_animals = []
for animal in animals:
    # No need for parenthesis around the conditional statement
    # you can simply access the first letter of the string
    # by index position 0 rather than index slicing
    #if (animal[:1]=='c'):
    if animal[0] == 'c':
        capital_animal = animal.upper()
        print (capital_animal)
        filtered_animals.append(capital_animal)
        # You can avoid the need for this extra variable
        # by simply calling len on filtered_animals at the end of script.
        #length = len(filtered_animals)
txt = "Number of C-animals: {}"
# Just call len on filtered_animals to get the count
#print(txt.format(length))
print(txt.format(len(filtered_animals)))
