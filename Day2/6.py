
#-----ROLL_NUMBER---83925 ----------
#-----NAME---Kshitij_Shrivastava----------

a = int(input("Enter the marks for 1 subject "))
b = int(input("Enter the marks for 2 subject "))
c = int(input("Enter the marks for 3 subject "))

avg = (a+b+c)/3
grade = " "

def calc_grade():
    if( 90 <= avg < 100):
        grade = 'A+ ---Excellent'
    elif(80 <= avg < 89):
        grade = 'B+ ---Very_Good'
    elif(70 <= avg < 79):
        grade = 'C+ ----Good'
    elif(60 <= avg < 69):
        grade = 'D+ ----Pass'
    else:
        grade = 'Fail ---Appear_Again'

    return grade

print("Final Grade received by the student is given as : " , calc_grade())




