from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

key = b"12345678"
text = input("Enter plaintext: ").encode()
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
encrypted = cipher.encrypt(pad(text, Blowfish.block_size))
print("Encrypted:", encrypted.hex())
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
decrypted = unpad(cipher.decrypt(encrypted), Blowfish.block_size)
print("Decrypted:", decrypted.decode())