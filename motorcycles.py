motorcycles = []

motorcycles.append('KTM')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')


myList = motorcycles

print('Original list.')
print(motorcycles)

for i in motorcycles:
    print(i.replace("a", ''))

print("\t")
print("Copy of list.")
print(myList)
print("\t")

popped_motorcycles = myList

popped_motorcycles = motorcycles.pop()
print("New list")
print(motorcycles)
print("\t")
print("Popped motorcycle")
print(popped_motorcycles)

