# Building a simple calculator using Python
#This is a simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication,division and modulus
#steps:
    #1)greet the user
    #2)take input from user 
    #3)perform operation
    #4)say thanks to user


def greet():
    print("MAGIC CALCULATOR")   #The name of the calculator is Magic Calculator
    print("Hey, welcome to magic calulator")  #Greeting the user
    print("lets get started.....")

greet()

try:
    a=int(input("Enter first number: "))   #Taking input from the user

    b=int(input("Enter second number: "))

    o=input("Enter the operation to be performed:")

    match o:       
        case "+":   #performs addition if the case is matched 
            print(f"The Addition is {a+b}")
        
        case "-":  #performs subtraction if the case is matched 
            print(f"The Subtraction is {a-b}")
        
        case "*":  #performs multiplication if the case is matched 
            print(f"The Multiplication is {a*b}")

        case "/":  #performs division if the case is matched 
            print(f"The Division is {a/b}")

        case "%":  #performs modulus if the case is matched 
            print(f"The Remainder is {a%b}")

        case default:        #default statement if the user entered an invalid operator
            print("Enter a valid operator")
        

except Exception as e:   #throws an error if the user enters a string or symbol
    print("Please enter a valid number")

def closing():    #thanking the user for using magic calculator
    print("Thanks for using magic calulator")

closing()
