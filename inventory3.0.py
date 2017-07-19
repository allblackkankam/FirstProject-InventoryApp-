#pickle to be able to write to text file
import pickle
#empty dictionary
inventory={}

#heading print out

print"""----------------------------------------

	PYTHON INVENTORY TAKER
	______________________

----------------------------------------"""


print """	Inventory Options
	----------------
	1. Add item
	2. View Inventory
	3. To Edit Quantity
	4. Remove item
	0. Exit Program
	-----------------"""

#input for inventory
option = int(raw_input("Enter Option: "))

#loop to keep the program running
while option != 0:
#option to Add item to the empty inventory
	if option == 1 :
		item =raw_input("Enter Item: ")
		if item in inventory:
			print "Item already Exist"
			print "Any number to add 0R 0 to Pass"
			qnty = int(raw_input("Add Quantity: "))
			inventory[item] += qnty
		else:
			qnty = int(raw_input("Enter Quantity: "))
			inventory[item] = qnty
		print "________________________________"
		print "%r has been added to stock" % item
		print ("Quantity of %r is now %d." % (item, inventory[item]))

#option to view item to the inventory
	elif option ==2 :
		if inventory == {}:
			print "Inventory is empty"
		else:
	 		for item in inventory:
				print item,":",inventory[item]

#option to edit quantity to the items in inventory
	elif option == 3 :
		print "1. Add 	\n0. Reduce"
		choice = int(raw_input("Choice: "))
		if choice == 1:
			item = raw_input("Enter Item: ")
			qnty = int(raw_input("Enter Number to Add: "))
			inventory[item] += qnty
			print "________________________________"
			print ("Quantity of %r is now %d." % (item, inventory[item]))
		elif choice == 0:
			item = raw_input("Enter Item: ")
			qnty = int(raw_input("Enter Number to Reduce: "))
			inventory[item] -= qnty
			print "________________________________"
			print ("Quantity of %r is now %d." % (item, inventory[item]))
#option to remove item(s) from the inventory
	elif option == 4:
		item =raw_input("Enter Item: ")
		print "Are You Sure You Want to Remove Item"
		print "1. Remove  \n0. Cancel "
		choice = int(raw_input("Choice: "))
		if choice == 1:
			print "________________________________"
			print "%r has been removed from stock." % item
			del(inventory[item])
		else:
			print "%r was not removed." % item
			pass

#Exceptions
	elif option != [0, 1, 2, 3, 4]:
		print "________________________________"
		print "WRONG ENTRY! Please try again"
		print """	Inventory Options
	----------------
	1. Add item
	2. View Inventory
	3. To Edit Quantity
	4. Remove item
	0. Exit Program
	-----------------"""
#option to exit program
	elif option == 0 :
		print "Inventory Program Has Ended !!! "
		print "________________________________"
	option = int(raw_input("\nEnter Option: "))



else:

	print "\n\nInventory Program Has Ended !!! "
	print "________________________________"

#file writing
filename = "invent.txt"
file = open (filename, "wb")
pickle.dump(inventory,file)

file = open(filename,"rb")
invet = pickle.load(file)
