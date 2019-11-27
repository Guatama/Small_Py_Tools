#!/usr/bin/env python
import argparse

def rot_encrypt(plain_text, key=13):
    """
    Unicode codes in Python 3
    unicode_range = { 
                    'a': [97, 122],
                    'A': [65, 90],
                    'а': [1072, 1103],
                    'А': [1040, 1071]
                    }
    """
    result = ''

    for char in plain_text:
        alphabet = [26, [65, 90], [97, 122]]

        if char.isalpha():
            if ord(char) >= 1040 and ord(char) <= 1103:
                alphabet = [32, [1040, 1071], [1072, 1103]]

            number = ord(char) + key

            if char.isupper():
                if number > alphabet[1][1]:
                    number -= alphabet[0]
                elif number < alphabet[1][0]:
                    number += alphabet[0]      
            elif char.islower():
                if number > alphabet[2][1]:
                    number -= alphabet[0]
                elif number < alphabet[2][0]:
                    number += alphabet[0]

            result += chr(number)
        
        else:
            result += char

    return  result


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('text', nargs='*')
    parser.add_argument('-k', '--key', type=int, default=1)
    args = parser.parse_args()

    text_string = ' '.join(args.text)
    key = args.key
    if args.decrypt:
        key = -key
    cyphertext = rot_encrypt(text_string, key)
    print(cyphertext)

if __name__ == "__main__":
    main()
