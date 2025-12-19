#exception handling in simple calculator

while True :
    try:
        num= int (input("Enter any 1st number: "))
        num1= int (input("Enter any 2nd number: "))
        operator= input("Enter any operator(+,-,*,/): ")
        
        
        if operator == "+":
            print("addition",num+num1)
    
        elif operator == "-":
            print("substraction",num-num1)
    
        elif operator == "*":
            print("addition",num*num1)  
    
        elif operator == "/":
            print("addition",num/num1)

            
        num2 =input("Type q for Quit,Or press 'Enter' for continue: ")
        if num2=="q":
            break
        
            
    except ZeroDivisionError:
        print("Can't divide by zero. ")

    except ValueError:
        print("Invalid input, try any number.")

 
