
def add(num1, num2):
    return num1 + num2
 
 
def subtract(num1, num2):
    return num1 - num2
 

def multiply(num1, num2):
    return num1 * num2
 

def divide(num1, num2):
    return num1 / num2
 
print("Please select operation -\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
 
choice = None


choice = input("Select operations form 1, 2, 3, 4 :")
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if choice == '1' :
    print ( add( number_1, number_2 ) )
elif choice == '2' :
    print  ( subtract ( number_1, number_2 ) )
elif choice == '3' :
    print ( multiply ( number_1, number_2 ) )
elif choice == '4':
    print ( divide ( number_1, number_2 ) )
else :
    print ( "Invalid input" )
