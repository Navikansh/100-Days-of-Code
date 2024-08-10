letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']
def encode(str, shift):
    code = ''
    for i in str:
        code += letters[(letters.index(i)+shift)%26]
    print(code)

def decode(str, shift):
    message = ''
    for i in str:
        message += letters[(letters.index(i)-shift)%26]
    print(message)
def main():
    reply = 'yes'
    while reply == 'yes':
        action = input("Type 'encode' to encrypt, 'decode' to decrypt. \n").lower().strip()
        match action:
            case 'encode':
                str = input('Type your message: \n')
                shift = int(input('Type the shift number: \n'))
                encode(str, shift)
            case 'decode':
                str = input('Type your message: \n')
                shift = int(input('Type the shift number: \n'))
                decode(str, shift)

if __name__ == '__main__':
    main()
