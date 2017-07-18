#pickle to be able to write to text file
import pickle
#empty dictionary
inventor={}

#heading print out 

print"""----------------------------------------
	
	PYTHON INVENTORY TAKER
	______________________

----------------------------------------"""


print """	Inventory Option
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
#option to Add item to the empty dictionary	
	if option == 1 :
		item =raw_input("Enter Item: ")
		if item in inventor:
			print "Item already Exist"
			print "Any number to add 0R 0 to Pass"
			qnty = int(raw_input("Add Quantity: "))
			inventor[item] += qnty
		else:
			qnty = int(raw_input("Enter Quantity: "))
			inventor[item]= qnty


#option to view item to the dictionary
	elif option ==2 :
		for item in inventor:
			print item,":",inventor[item]
		
#option to edit quantity to the items in dictionary
	elif option == 3 :
		print "1. Add 	\n0. Reduce"
		choice = int(raw_input("Choice: "))
		if choice == 1:
			item = raw_input("Enter Item: ")
			qnty = int(raw_input("Enter Number to Add: "))
			inventor[item] += qnty
		elif choice == 0:
			item = raw_input("Enter Item: ")
			qnty = int(raw_input("Enter Number to Reduce: "))
			inventor[item]-= qnty

#option to Add item to the empty dictionary
	elif option == 4:
		item =raw_input("Enter Item: ")
		print "Are You Sure You Want to Remove Item"
		print "1. Remove  \n0. Cancel "
		choice = int(raw_input("Choice: "))
		if choice == 1:
			del(inventor[item])
		else:
			pass
			
#option to exit program
	elif option == 0 :
		print "Inventory Program Has Ended !!! "

	option = int(raw_input("\nEnter Option: "))

	
else:
	print "\n\nInventory Program Has Ended !!! "
	print "________________________________"

#file writing 
filename = "invent.txt"
file = open (filename, "wb")
pickle.dump(inventor,file)

file = open(filename,"rb")
invet = pickle.load(file)




	