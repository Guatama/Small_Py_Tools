import argparse
from string import ascii_lowercase, ascii_uppercase, ascii_letters


def shift_ascii(key: int) -> str:
    return ascii_lowercase[key:] + ascii_lowercase[:key]\
           + ascii_uppercase[key:] + ascii_uppercase[:key]


def rot_encrypt(plain_text: str, key: int = 13) -> str:
    """Encrypt message with caesar cipher

    Arguments:
        plain_text {str} -- [message to encrypt]

    Keyword Arguments:
        key {int} -- [encryption key] (default: {13})

    Returns:
        str -- [encrypted message]
    """
    table = plain_text.maketrans(ascii_letters, shift_ascii(key))
    return plain_text.translate(table)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true', default=False)
    parser.add_argument('text', nargs='*')
    parser.add_argument('-k', '--key', type=int, default=13)
    args = parser.parse_args()

    text_string = ' '.join(args.text)
    key = args.key
    if args.decrypt:
        key = -key
    cyphertext = rot_encrypt(text_string, key)
    print(cyphertext)


if __name__ == "__main__":
    main()