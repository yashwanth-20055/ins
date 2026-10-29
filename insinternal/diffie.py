p = 23
g = 5
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))
A = pow(g, a, p)
B = pow(g, b, p)
key_alice = pow(B, a, p)
key_bob = pow(A, b, p)
print("Alice's public key:", A)
print("Bob's public key:", B)
print("Shared secret:", key_alice)