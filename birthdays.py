bd = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol': 'Apr 17'}

while True:
    print('Enter a name : (blank to quit)')
    name = input()
    if name == '':
        break
    if name in bd:
        print(bd[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        bd[name] = bday
        print('Birthday database updated.')