valid = False

while not valid:
    
    try:
        n = int(input("Enter a number:"))
        
        
        if n%2 == 0:
            print("Bye BYe")
            valid = True
            
    except ValueError:
        print("INvalid data type")
