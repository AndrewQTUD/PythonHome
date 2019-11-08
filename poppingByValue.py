motorcycles = ['KTM', 'Honda', 'Suzuki']

for i in motorcycles:
    print(i.upper())


copyList = motorcycles
print("\t")
motorcycles.remove('Honda')
print(motorcycles)

too_expensive = 'KTM'
motorcycles.remove(too_expensive)
print("\t")
print(motorcycles)
print("\nA " + too_expensive.upper() + " is too expensive for me.")

newMotorcycles = ['KTM', 'HONDA', 'SUZUKI', 'DUCATI', 'TRIUMPH', 'KTM', 'KTM']

for i in newMotorcycles:
    print('Show list unedited 1st')
    print(newMotorcycles)
    newMotorcycles.remove(too_expensive)
    print('Edited list')
    print(newMotorcycles)