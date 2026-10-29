from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()
message = input("Enter message: ").encode()
signature = private_key.sign(message, hashes.SHA256())
print("Digital Signature:", signature.hex())
try:
 public_key.verify(signature, message, hashes.SHA256())
 print("Signature Verified: Valid")
except InvalidSignature:
 print("Signature Verified: Invalid")