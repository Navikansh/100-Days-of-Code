
def main():
    print('Welcome to the tip calculator! ')
    amt = float(input('What was the total bill? $'))
    tip = float(input('How much would you like to tip? '))
    ppl = float(input('How many people to split the bill? '))
    print(f'Each person should pay ${(amt + amt*tip/100)/ppl: .2f}')

if __name__ == '__main__':
    main()
