# read animals.txt
# and write animals_new.txt

file = open('animals.txt', mode='rt')
animals = file.read().split('\n')

new_file = open('animals_new.txt', mode='at')
new_animals = ' '.join(animals)
new_file.write(new_animals)

file.close()
new_file.close()
