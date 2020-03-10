# method on the top
def separator():
    print(60 * ':')

def menu():
    print(2 * '\n')
    separator()
    print(' Welcome to PyCalc ')
    separator()

    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Exit')




# instruction on the bottom

separator()

opc = ''
while(opc != 'x'):
    menu()
    opc = input('Select an option: ')
    if(opc == 'x'):
        break

    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))
    
    if(opc == '1'):
        res = num1 + num2
        print('Sum = ' +str(res))
    if(opc == '2'):
        res = num1 - num2
        print('Remainder = ' +str(res))
    if(opc == '3'):
        res = num1 * num2
        print('Product = ' +str(res))
    if(opc == '4'):
        if(num2 == 0):
            print("Error: Not Allowed")
        else:
            res = num1 / num2
            print('Quotient = ' +str(res))

    input('Press Enter to Continue')

print('Calc-you later!')
    