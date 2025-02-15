#Instructable text-based Calculator

'''0 - to quit
1  - to add
2 - to subtract
3 - multiply
4 - Divide
5 - modulus'''

# to add
def add(num1 , num2):
    sum = int(num1 + num2)
    print('Addition: ', sum)

# to subtract  
def subtract (num1 , num2):
    difference = int(num1 - num2)
    print('Subtraction:' , difference)

# to multiply    
def multiply(num1 , num2):
    mult = int(num1 * num2)
    print('Multiplication:' , mult)
 
# to divide   
def divide(num1 , num2):
    division = int(num1 / num2)
    print('Division: ', division)
    
#to find modulus
def modulus(num1 , num2):
       modulus = int(num1 % num2)
       print('Modulus:' , modulus)
       
#Calculator logic
while True: 
     print(''' 
                -- Calculator Menu --
                0. Quit
                 1. Add two numbers 
                 2. Subtract two numbers 
                 3. Multiply two numbers 
                 4. Divide two numbers 
                 5. Modulus of two numbers 
                     ''')
     
     command = int(input('Enter a command: '))
     print()
     
     if command == 1:
         print('-- To Add -- ')
         num_1 = int(input('Enter your first number: '))
         num_2 = int(input('Enter your second number: '))
         add(num_1 , num_2)
    
     elif command == 2:
         print (' -- To Subtract --')
         num_1 = int(input('Enter your first number: '))
         num_2 = int(input('Enter your second number: '))
         subtract (num_1 , num_2)
    
     elif command == 3:
         print (' -- To Multiply -- ')
         num_1 = int(input('Enter your first number: '))
         num_2 = int(input('Enter your second number: '))
         multiply(num_1 , num_2)
     
     elif command == 4:
         print (' -- To Divide -- ')
         num_1 = int(input('Enter your first number: '))
         num_2 = int(input('Enter your second number: '))
         divide(num_1 , num_2)
     
     elif command == 5:
         print ( ' -- To find Modulus -- ')
         num_1 = int(input('Enter your first number: '))
         num_2 = int(input('Enter your second number: '))
         modulus(num_1 , num_2)
     
     elif command == 0 :
         print('Exiting...')
         break
     
     else:
          print('Invalid command !')