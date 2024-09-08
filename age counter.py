print('\033c')


def CheckAge(b):
    if b < 0:
        raise ValueError("Only integers greater than zero are allowed.")
        
        
    if b % 2 == 0:
        print("The age is an even integer.")
        
    else:
        print("The age is an odd integer.")
        
        
try:
    bohubrihi = int(input("Enter your age:"))
    CheckAge(bohubrihi)
    
    
except ValueError:
    print("Only integers greater than zero are allowed.This is handled outside of the function.")