'''Write a function that takes a message and an increment amount
and outputs the same letters shifted by that amount in the alphabet.
Assume lowercase and no punctuation. Preserve spaces.'''


def caesarCipher(str, amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for idx, char in enumerate(str):
        # preserve spaces
        if char == ' ':
            encoded += char
        else:
            # now alphabets
            offset = (alphabet.index(char) + amount) % 26
            encoded += alphabet[offset]
    return encoded


print(caesarCipher('how are you', 4))
