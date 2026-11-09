def matrix(key):
    s = ""
    for c in key.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        c = "I" if c == "J" else c
        if c.isalpha() and c not in s:
            s += c

    return [s[i:i+5] for i in range(0, 25, 5)]


def prepare(text):
    text = "".join(c for c in text.upper() if c.isalpha()).replace("J", "I")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            result += a + "X"
            i += 1
        elif a == text[i + 1]:
            result += a + "X"
            i += 1
        else:
            result += a + text[i + 1]
            i += 2

    return result


def playfair(text, key, decrypt=False):
    m = matrix(key)
    pos = {m[r][c]: (r, c) for r in range(5) for c in range(5)}

    if not decrypt:
        text = prepare(text)

    result = ""
    shift = -1 if decrypt else 1

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = pos[a]
        r2, c2 = pos[b]

        if r1 == r2:
            result += m[r1][(c1 + shift) % 5]
            result += m[r2][(c2 + shift) % 5]

        elif c1 == c2:
            result += m[(r1 + shift) % 5][c1]
            result += m[(r2 + shift) % 5][c2]

        else:
            result += m[r1][c2] + m[r2][c1]

    return result


key = input("Enter key: ")
text = input("Enter plaintext: ")

cipher = playfair(text, key)
print("Encrypted:", cipher)
print("Decrypted:", playfair(cipher, key, True))