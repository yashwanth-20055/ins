import math

def get_order(key):
    return sorted(range(len(key)), key=lambda k: key[k])


def encrypt(text, key):
    text = text.replace(" ", "").upper()

    cols = len(key)
    rows = math.ceil(len(text) / cols)

    text += 'X' * (rows * cols - len(text))

    matrix = [list(text[i:i + cols])
              for i in range(0, len(text), cols)]

    order = get_order(key)

    cipher = ""

    for col in order:
        for row in range(rows):
            cipher += matrix[row][col]

    return cipher


def decrypt(cipher, key):
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)

    order = get_order(key)

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0

    for col in order:
        for row in range(rows):
            matrix[row][col] = cipher[index]
            index += 1

    plain = ""

    for row in matrix:
        plain += "".join(row)

    return plain.rstrip('X')


text = input("Enter plaintext: ")
key = input("Enter key: ")

cipher = encrypt(text, key)
print("Encrypted:", cipher)

print("Decrypted:", decrypt(cipher, key))