def calculate(num1 : int, symbol : str, num2 : int):
    '''Calculates and returns the calculated value of the parameters'''
    match symbol:
        case '+':
            print(f'{num1}+{num2} = {num1 + num2}')
            return num1 + num2
        case '-':
            print(f'{num1}-{num2} = {num1 - num2}')
            return num1 - num2
        case '*':
            print(f'{num1}*{num2} = {num1 * num2}')
            return num1 * num2
        case '/':
            print(f'{num1}/{num2} = {num1 / num2}')
            return num1 / num2
            


def main():
    print('Hi! Welcome to the calculator')
    reply = 'n'
    while reply == 'n':
        num1 = float(input('What\'s the first number?\n' ))
        symbol = input('Choose an operation: \n+\n-\n*\n/\n')
        num2 = float(input('What\'s the second number? \n'))
        temp = calculate(num1, symbol, num2)
        reply = input(f'Type \'n\' for a new calculation or type \'c\' to continue calculation with {temp}\n')

    while True:
        match reply:
            case 'c':
                num1 = temp
                symbol = input('Choose an operation: \n+\n-\n*\n/\n')
                num2 = float(input('What\'s the second number?\n'))
                temp = calculate(num1, symbol, num2)
                reply = input(f'Type \'n\' for a new calculation or type \'c\' to continue calculation with {temp}\n')
                
            case 'n':
                num1 = float(input('What\'s the first number?\n' ))
                symbol = input('Choose an operation: \n+\n-\n*\n/\n')
                num2 = float(input('What\'s the second number? \n'))
                temp = calculate(num1, symbol, num2)
                reply = input(f'Type \'n\' for a new calculation or type \'c\' to continue calculation with {temp}\n')


if __name__ == '__main__':
    main()