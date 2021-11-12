import collections


def encrypt(key, text):
    encrypted_text = ''
    # Add key to every char in string
    for char in text:
        encrypted_text += chr((ord(char)+key) % 128)
    return encrypted_text


def decrypt(key, text):
    decrypted_text = ''
    # Sub key from every char in string
    for char in text:
        decrypted_text += chr((ord(char)-key) % 128)
    return decrypted_text


def check_common(text):
    # check which letter is the most common
    return collections.Counter(text).most_common(1)[0][0]


def generate_key(common_char):
    # returns the key of the encryption ' ' is the most common symbol
    return (ord(common_char) - ord(' ')) % 128


if __name__ == '__main__':
    with open("LoremIpsumEncrypted.txt", 'r') as f:
        text = f.read()
    common = check_common(text)
    key = generate_key(common)
    text = decrypt(key, text)
    print(text)
