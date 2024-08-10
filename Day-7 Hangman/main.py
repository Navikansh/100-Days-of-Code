
import random
import art
words = ['JAWAN', 'ANIMAL', 'PATHAN']



def prep():
    chosen_word = random.choice(words)
    progress = []
    chosen_list = []
    for i in chosen_word:
        print('_', end=' ')
        progress += '_'
        chosen_list += i
    return chosen_word, progress, chosen_list

lives = 7
def main(chosen_word, progress, chosen_list):
    while lives > 0:
        guess = input().upper()
        print()

        if guess in chosen_word:
            for i in range(0,len(chosen_word)):
                if chosen_word[i] == guess:
                    print(chosen_word[i], end=' ')
                    progress[i] = guess
                else:
                    print(progress[i], end=' ')
            print('\n')
            if progress == chosen_list:
                print('Congrats You Won!')
                break
        else:
            print(art.stages[lives - 1])
            lives -= 1

if __name__== '__main__':
    p = prep()
    main(p)
