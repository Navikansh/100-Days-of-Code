def main():
    print('''Welcome to Treasure Island\nYour mission is to find the treasure''')
    c1 = input('Where do you want to go lef or right? ').strip().lower()
    if c1 == 'left':
        c2 = input('''You have reached a lake.\nWould you like to wait for a boat or swim across the lake? ''').strip().lower()
        if c2 == 'swim':
            print('The lake was full of hungry crocodiles which were very eager to eat you.\nGame Over')
        else:
            c3 = input('''You reached the island safely.\n
                  You find three doors in front of you, one is red, one is blue and one is yellow.\n Which one do you choose? ''').strip().lower()
            if c3 == 'yellow':
                print('You found the treasure box!\nYou Win!')
            elif c3 == 'red':
                print('The fire behind the red door killed you.\nGame Over')
            elif c3 == 'blue':
                print('The room behind the blue door was full of poisonous gas.\nGame Over')
    else:
        
        print('The right path had a lion in it which killed you.\nGame Over')

if __name__ == '__main__':
    main()
