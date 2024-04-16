#-----ROLL_NUMBER---83925----------
#-----NAME---Kshitij_Shrivastava----------


q = int(input("Enter Total qauntity of items : "))
bill = 0
if ( q < 30):
    bill = 5*q
elif( 30<= q < 50):
    bill = (5*q) - (0.1*(5*q))
else:
    bill = (5*q) - (0.3*(5*q))

print("Total bill that required to pay by customer = ", bill)
