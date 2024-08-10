import os
players = {}

def main():
    reply = 'yes'
    while reply == 'yes':
        os.system('clear')
        name = input('Name of bidder:\n')
        bid = int(input('Bid amount:\n').strip('$'))
        players[bid] = name 
        reply = input('Are there anymore players?\n').lower().strip()
    init = None
    for key in players:
        if init == None or key > init:
            init = key
    print(f'The item goes to {players[init]} for {init}$!')

if __name__ == '__main__':
    main()
