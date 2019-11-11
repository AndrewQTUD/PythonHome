#Buffet food tuple 
foodStuffs = ("Pizza", "Cheese", "Kebab", "Chocolate")

print("The items we sell are : " + str(foodStuffs))



foodStuffs = ("Pizza", "Sausage", "Kebab", "Chocolate")

print("New menu items are : " + str(foodStuffs))

print("What is your favourite?")

fs = input("Enter your favourite food?")

if fs in foodStuffs:
    print("Good choice")

print(fs)