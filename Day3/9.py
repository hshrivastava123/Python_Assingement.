#classwork assingement--date--17 april 2024


k1=[]
k2=[]
k3=[]
password = input('Enter the password: ')
leng=len(password)
print(leng)


i=0
while(i<leng):
    if (password[i].islower()):
        k1.append(password[i])
        i=i+1
    elif (password[i].isupper()):
        k1.append(password[i])
        i=i+1
    elif (password[i].isdigit()):
        k2.append(password[i])
        i=i+1
    else:
        k3.append(password[i])
        i=i+1
            
print(k1)
print(k2)
print(k3)               
    
if(leng>=9):
    if(len(k1)>=4):
        if(len(k2)>=4):
            if(len(k3)>=1):
                print("valid password")
            else:
                print("invalid passsword special character")
        else:
            print("invalid password for digit")
    else:
        print("invalid password for character")
else:
    print("password length is small")        
                
                
    