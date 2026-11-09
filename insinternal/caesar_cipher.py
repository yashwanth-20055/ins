def caesar(text, key):
    result = ""

    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + key) % 26 + base)
        else:
            result += c

    return result

text = input("Enter plaintext: ")
key = int(input("Enter key: "))

cipher = caesar(text, key)
plain = caesar(cipher, -key)

print("Encrypted:", cipher)
print("Decrypted:", plain)