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
	-------------------
	1. Add item
	2. View Inventory
	3. To Edit Quantity
	4. Remove item
	0. Exit Program
	-------------------
	NOTE: Please Use Numbers For Program 
	* Options 
	* Quantity and When Asked
	Failure Would Crash Program !!!

	--------------------------------------"""

#input for inventory
option = int(raw_input("Enter Option: "))

#loop to keep the program running
while option != 0:
#option to Add item to the empty dictionary	
	if option == 1 :
		item =raw_input("Enter Item: ")
		if item in inventor:
			print """-------------------------------
Item Already Exist
Any Number To Add OR 0 To Pass"""
			qnty = int(raw_input("Add Quantity: "))
			inventor[item] += qnty
			print "(%s"% qnty, "of%s" %item, "has been added )"
		else:
			qnty = int(raw_input("Enter Quantity: "))
			inventor[item]= qnty
			print "(%d"% qnty, item, "has been added to Inventory )"


#option to view item to the dictionary
	elif option ==2 :
		for item in inventor:
			print item,":",inventor[item]
		
#option to edit quantity to the items in dictionary
	elif option == 3 :
		print "1. Add 	\n0. Reduce 	\n----------"
		choice = int(raw_input("Choice: "))
		if choice == 1:
			item = raw_input("Enter Item: ")
			if item not in inventor:
				print"""-----------------------
Item Not in Inventory
Use Option 1 To Add"""
				pass
			else: 
				qnty = int(raw_input("Enter Number to Add: "))
				inventor[item] += qnty
				print "(%s" % qnty, "of%s" %item, "has been added )"

		elif choice == 0:
			item = raw_input("Enter Item: ")
			if item not in inventor:
				print"""-----------------------
Item Not in Inventory
Use Option 1 To Add"""
				pass
			else: 
				qnty = int(raw_input("Enter Number to Reduce: "))
				inventor[item]-= qnty
				print "(%s" % item, "has been reduced by%s" % qnty, ")"
		

#option to Add item to the empty dictionary
	elif option == 4:
		item =raw_input("Enter Item: ")
		print "Are You Sure You Want to Remove Item"
		print "1. Remove  \n0. Cancel "
		choice = int(raw_input("Choice: "))
		if choice == 1:
			del inventor[item]
			print "(%s" % item,"has been removed )"
		else:
			pass
			print "(%s" % item,"has not been removed )"
#option to exit program
	elif option != 0 :
		print """	Invalid Option !!! 
	\n 	1. Add item
	2. View Inventory
	3. To Edit Quantity
	4. Remove item
	0. Exit Program"""
		
	option = int(raw_input("\nEnter Option: "))

	
else:
	print "\n\nInventory Program Has Ended !!! "
	print "________________________________"


#file writing 
filename = "invent.txt"
file = open (filename, "w")
pickle.dump(inventor,file)

file = open(filename,"r")
invet = pickle.load(file)




	