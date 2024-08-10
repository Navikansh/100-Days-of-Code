import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def value(sum:int, cards):
    '''Assigns the cards appropriate value'''

    values = []
    for each in cards:
        match each:
            case '2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'|'10':
                card_value = int(each)
            case 'J'|'Q'|'K':
                card_value = 10
            case 'A':
                if (sum + 11 > 21) and not(sum + 1 >21):
                    card_value = 1
                elif not(sum + 11 > 21):
                    card_value = 11
                else:
                    card_value = 1
        values.append(card_value)
    return values

def choose(num:int):
    '''Chooses cards for player and dealer'''
    choices = random.choices(cards,k = num)
    return choices



def main():
    sum1 = 0
    choices = choose(4)
    dealercards = [choices[2], choices[3]]
    choices.pop(3)
    choices.pop(2)
    values = value(sum1, choices)
    sum2 = 0
    sum1 = values[0]+values[1]
    print(f'Your Cards:\n{choices[0], choices[1]}\nSum: {sum1}')
    print(f'Dealer\'s Cards:\n {dealercards[0]}')
    reply = input('Type \'y\' to deal another card and \'n\' to pass\n').lower()
    sum2 = sum(value(sum2, dealercards))
    while True:
        match reply:
            case 'y':
                choice_new = choose(1)
                choices+=choice_new
                values = value(sum1, choices)
                sum1 = sum(values)
                print(f'Your Cards:\n{choices}\nSum: {sum1}')
                print(f'Dealer\'s Cards:\n {dealercards[0]}')
                reply = input('Type \'y\' to deal another card and \'n\' to pass\n').lower()
            case 'n':
                if sum2 > 21:
                    print('You Win!')
                    break
                if sum1 > sum2:
                    print('You Win!')
                    break
                elif sum2 > sum1:
                    print('You Lose')
                    break
        
        if sum1 > 21:
            print('You Lose')
            break
        elif sum1 == 21:
            print('You Win!')
            break



if __name__ == '__main__':
    main()
