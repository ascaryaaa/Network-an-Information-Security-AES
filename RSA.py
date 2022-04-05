import Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_OAEP
import binascii
import ast
import time

random_generator = Random.new().read
#generate pub and priv key
key = RSA.generate(1024, random_generator) 

#pub key export for exchange
publickey = key.publickey() 
encryptor = PKCS1_OAEP.new(publickey)

start = time.time()

#message to encrypt
encrypted = encryptor.encrypt(b'this is a secret message that needs to be encrypted')

#ciphertext
print('\n encrypted message:', encrypted)
print('\n encrypted message in HEX:', binascii.hexlify(encrypted)) 
f = open ('RSA encrypted.txt', 'w')
#write ciphertext to file
f.write(str(encrypted)) 
f.close()

end = time.time()
print('\nEncryption Execution Time: ', end-start)

#decrypted code below
start2 = time.time()

f = open('RSA encrypted.txt', 'r')
message = f.read()

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print('\n decrypted :', decrypted.decode('ascii'))

f = open ('RSA decrypted.txt', 'w')
f.write(str(decrypted.decode('ascii')))
f.close()

end2 = time.time()                                                                       
print('\nDecryption Execution Time: ', end2-start2, '\n')
