#-----ROLL_NUMBER---83925----------
#-----NAME---Kshitij_Shrivastava----------

principle = float(input("Enter Principal Rate :"))
rate = float(input("Enter req rate of interest :"))
time = float(input("Enter time period :"))

def si(p,r,t):
    interest = (p*r*t)/100
    return interest

print("Simple interest = ", si(principle,rate,time))