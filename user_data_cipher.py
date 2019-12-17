from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import MD4

def encipher():
    # print('start encipher()')
    # creation 256 bit session key
    sessionkey = MD4.new(b'abc').digest() + Random.new().read(16)  # 256 bit
    # encryption AES of the message
    f = open('data/users11.json', 'rb')
    plaintext = f.read()
    f.close()
    iv = Random.new().read(16)  # 128 bit
    obj = AES.new(sessionkey, AES.MODE_CFB, iv)
    ciphertext = iv + obj.encrypt(plaintext)
    f = open('data/users11.json', 'wb')
    f.write(bytes(ciphertext))
    f.close()
    # encryption RSA of the session key
    publickey = RSA.importKey(open('publickey.txt', 'rb').read())
    cipherrsa = PKCS1_OAEP.new(publickey)
    sessionkey = cipherrsa.encrypt(sessionkey)
    f = open('sessionkey.txt', 'wb')
    f.write(bytes(sessionkey))
    f.close()
    # print('end encipher()')


def decipher():
    # print('start decipher()')
    # decryption session key
    privatekey = RSA.importKey(open('privatekey.txt', 'rb').read())
    cipherrsa = PKCS1_OAEP.new(privatekey)
    f = open('sessionkey.txt', 'rb')
    sessionkey = f.read()
    f.close()
    sessionkey = cipherrsa.decrypt(sessionkey)
    # decryption message
    f = open('data/users11.json', 'rb')
    ciphertext = f.read()
    f.close()
    iv = ciphertext[:16]
    obj = AES.new(sessionkey, AES.MODE_CFB, iv)
    plaintext = obj.decrypt(ciphertext)
    plaintext = plaintext[16:]
    f = open('data/users11.json', 'wb')
    f.write(bytes(plaintext))
    f.close()
    # print('end decipher()')