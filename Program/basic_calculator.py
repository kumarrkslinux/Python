#!/usr/bin/python3

repeat = 'Y'

print("Basic calculator")

while repeat == 'Y':
    number1 = float(input("Enter your first number: "))
    operator = input('''please enter your operator value from below
                       + --> addtion,
                       - --> subtraction,
                       * --> multiplication,
                       / --> division,
                       // --> floor division,
                       % --> modulus and 
                       ** --> power operator,
                       ''')
    number2 = float(input("Enter your second number: "))

    if operator == '+':
       sum = number1 + number2
       print(number1, ' + ', number2, ' = ', sum)

    elif operator  == '-':
        sum = number1 - number2
        print(number1, ' - ', number2, ' = ', sum)
    
    elif operator  == '*':
        sum = number1 * number2
        print(number1, ' * ', number2, ' = ', sum)

    else:
        print("'Invalid' Please give valid operator ")

    y_or_n = input("press Y for continue or presss any key")

    repeat = y_or_n.upper()

    if repeat != 'Y':

       print("Thank you")
       

                      
                     
