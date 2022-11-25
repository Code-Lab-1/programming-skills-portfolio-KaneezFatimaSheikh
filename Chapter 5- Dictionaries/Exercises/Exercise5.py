## Exercise 5: Pets :ballot_box_with_check:

# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
# owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
# each pet

pets = []


pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)


for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
     print("\t" + key + ":"+str(value))