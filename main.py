dictionary = {'a': 1, 'b': 6, 'c': 56, 'd': 22, 'e': 11, 'f': 26, 'g': 50, 'h': 60,
              'i': 24, 'j': 39, 'k': 97, 'l': 46, 'm': 821, 'n': 76, 'o': 81, 'p': 16,
              'q': 14, 'r': 94, 's': 23, 't': 55, 'u': 43, 'v': 67, 'w': 100, 'x': 88, 'y': 31, 'z': 34, ' ': 33}


def getkey(val):
    for key, value in dictionary.items():
        if val == value:
            return key
    print("Key doesn't exist.")


def encrypt():
    try:
        string = input('Insert plain text:')
        string2 = ''
        for letter in string:
            letter = letter.lower()
            string2 += str(dictionary[letter]) + ' '
        print(string2)
    except KeyError:
        print('plain text can contain no extra symbols\n')
        encrypt()


def decrypt():
    try:
        cyphertext = input('enter encrypted text:')
        numarray = cyphertext.split()
        string3 = ''
        for i in range(len(numarray)):
            numarray[i] = int(numarray[i])
        for x in numarray:
            string3 += getkey(x)
        print(string3)
    except ValueError:
        print('encrypted text can only contain numbers\n')
        decrypt()
    except TypeError:
        print('please enter a valid value\n')
        decrypt()


print('enter E for encrypt, D for decrypt')


def askformode():
    mode = input('enter mode:')

    if mode == 'E':
        encrypt()
    elif mode == 'D':
        decrypt()
    else:
        print('Enter valid mode\n')
        askformode()


askformode()
