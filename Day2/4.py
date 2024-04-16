#-----ROLL_NUMBER---83925----------
#-----NAME---Kshitij_Shrivastava----------


year = int(input("Enter Year to predict value is leap or not "))

# Leap Year Check 
if year % 4 == 0 and year % 100 != 0:
    print("This is a Leap Year ---->",year)
elif year % 100 == 0:
    print("This is not a Leap Year--->",year)
elif year % 400 ==0:
    print( "This is a Leap Year--->",year)
else:
    print("This is not a Leap Year--->",year)