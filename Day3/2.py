#-----ROLL_NUMBER---83925----------
#-----NAME---Kshitij_Shrivastava----------

mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',str(size),'elements')

for i in range(size):
    data = int(input())
    mylist.append(data)

print('Alternate elements are:')

for i in range(0,size,2):
    print(mylist[i])