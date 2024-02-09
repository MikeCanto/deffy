from random import getrandbits
import hashlib

g = 2
deffy = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF"

p = int(deffy, 16)

# se generan los numero aleatorios
a_alice = getrandbits(256)
e_eve = getrandbits(256)

# se generan las llaves privadas
a = g ^ a_alice % p
e = g ^ e_eve % p

# se genera la llave compartida (publica)
s1 = e ^ a_alice % p
s2 = a ^ e_eve % p

# Hash s1 and s2
hash_s1 = hashlib.sha256(str(s1).encode()).hexdigest()
hash_s2 = hashlib.sha256(str(s2).encode()).hexdigest()

print(f"Alice: {hash_s1}")
print(f"Eve: {hash_s2}")

e_eve = getrandbits(256)
b_bob = getrandbits(256)

# se generan las llaves privadas
e = g ^ e_eve % p
b = g ^ b_bob % p

# se genera la llave compartida
s1 = b ^ e_eve % p
s2 = e ^ b_bob % p

# Hash s1 and s2
hash_s3 = hashlib.sha256(str(s1).encode()).hexdigest()
hash_s4 = hashlib.sha256(str(s2).encode()).hexdigest()

print(f"Eve: {hash_s3}")
print(f"Bob: {hash_s4}")