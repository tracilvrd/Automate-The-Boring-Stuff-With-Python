birthdays = {'Alice': 'Oct 2', 'John': 'January 1', 'Mary': 'May 4'}

while True:
    print('Enter a name: ')
    name = input()
    if name == ' ':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
