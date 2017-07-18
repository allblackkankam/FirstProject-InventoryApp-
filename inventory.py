
print ("Welcome! Keep inventory here!")
print ("Type 'add' to add items OR Type 'check' to check inventory. ")
command = raw_input()
#stock = raw_input("Type 'check' to check inventory")

if command == "add":
# Estabilishing data to be collected
#building stock
    item = raw_input("Name of item: ")
    print ("%s has been added." % item)
    quantity = int(raw_input("Quantity in stock: "))
    print ("Quantity of %s is %d." % (item, quantity))

    stock_info = {item:quantity, }
    print stock_info

elif command == "check":
    print ("hold on a second")

else:
    print ("WRONG ENTRY! Please try again.")

command = raw_input("Type 'edit' to edit stock. ")
if command == "edit":
    print ("gimme a sec")
    item = raw_input("Name of item: ")
    print ("%s will be editted." % item)
    consumed = int(raw_input("Quantity consumed: "))
    print ("Quantity of %s consumed is %d." % (item, consumed))
    # quantity = quantity - consumed
    #stock_info[quantity] -= consumed .... its not working
    # print stock_info
