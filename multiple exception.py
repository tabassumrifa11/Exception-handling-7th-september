print('\033c')

try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    
    result = num1/num2
    
    print(f"Result is: {result}")
    print(f"Result is: {result1}")
    
    
except ZeroDivisionError:
    print("Division by zero is not allowed")
    
    
except ValueError:
    print("Please enter numerical value")
    
    
except NameError as ex:
     print(f"The exception is: {ex}")
     
    
finally:
     print("I will execute no matter what happens")
     
     
print("I am outside everything")