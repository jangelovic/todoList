import pickle
print("Welcome to the To Do List ")
todoList = []
print("Enter a to add an item")
print("Enter r to remove an item")
print("Enter p to print the list")
print("Enter q to quit")
print("Enter l to load a previous list")
print("Enter m to pull up the menu")
while True:
	choice = input("Make your choice ")

	if choice == "q":
		pickle.dump(todoList, open("save.p", "wb"))
		break
	elif choice == "a":
		a = input("What would you like to add to the list? ")
		todoList.append(a)
		# add an itme to the list
	elif choice == "r":
		r = input("What would you like to remove from the list? ")
		todoList.remove(r)
		# remove an item from the list
	elif choice == "p":
		print(todoList)
		# print the list
	elif choice == "m":
		print("Enter a to add an item")
		print("Enter r to remove an item")
		print("Enter p to print the list")
		print("Enter q to quit")
		print("Enter l to load a previous list")
	elif choice == "l":
		todoList = pickle.load(open("save.p", "rb"))
	else:
		print("This input is not present in the To Do List code")
