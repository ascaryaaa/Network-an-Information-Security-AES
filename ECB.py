#AES ECB Method
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import binascii
import time

#plain text
plaintext = 'secret password text'
#key
key = pad(b"k3yp422w0rd", AES.block_size)

#encryption timer start
start = time.time()           

#Encrypt
def _encrypt(plaintext):                                                                
    data_bytes = bytes(plaintext, 'utf-8')
    padded_bytes = pad(data_bytes, AES.block_size)
    AES_obj = AES.new(key, AES.MODE_ECB)
    ciphertext = AES_obj.encrypt(padded_bytes)
    return ciphertext
ciphertext = _encrypt(plaintext)

print('text to be encrypted: ', plaintext)
print('key:', key)
print('key in HEX format: ', binascii.hexlify(key))
print('\nencrypted output: ', ciphertext)
#encryption timer end
end = time.time()                                                                      

print('\nEncryption Execution Time: ', end-start)

#decryption timer start
start2 = time.time()                          

#Decrypt
def _decrypt(ciphertext):                                                               
    AES_obj = AES.new(key, AES.MODE_ECB)
    raw_bytes = AES_obj.decrypt(ciphertext)
    extracted_bytes = unpad(raw_bytes, AES.block_size)
    return extracted_bytes
plaintext = _decrypt(ciphertext)
print('\ndecrpyted output: ', plaintext)
print('decrypted output in plain text: ', plaintext.decode('ascii'))
#decryption timer end
end2 = time.time()                                                                       
print('\nDecryption Execution Time: ', end2-start2, '\n')

# REFERENCE: 
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html