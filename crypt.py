import os
import sys
import random
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aesencrypt(text, aeskey):
    AESobject=AES.new(aeskey, AES.MODE_ECB)
    encodedtext=text.encode('utf-8')
    padding=pad(encodedtext, AES.block_size)
    aescipher=AESobject.encrypt(padding)
    return aescipher

def rsaencrypt(aeskey, pubkey):
    with open(pubkey,'r') as file:
        for line in file:
            values=line.strip().split(',')
        n1,e1=values
    n=int(n1)
    e=int(e1)
    #I'm converting it into int to perform operations
    intaeskey=int.from_bytes(aeskey, 'big')
    Rencrypt=pow(intaeskey,e,n)
    #to_bytes gives output in binary, need to convert into bytes
    RSAinbytes=Rencrypt.to_bytes((Rencrypt.bit_length()+7) // 8, 'big')
    #bytes has to be base64 encoded before decoding in utf because to ensure that all the binary values are able to be decoded in utf8 into proper ascii characters (strings)
    RSAb64encoded=base64.b64encode(RSAinbytes)
    RSAdecoded=RSAb64encoded.decode('utf-8')
    return RSAdecoded


def encryptfile(pubkey, ip, op):
    with open(ip, 'r') as file:
        PT=file.read()
    aeskey=os.urandom(16)
    afterAES=aesencrypt(PT, aeskey)
    RSAonAESkey=rsaencrypt(aeskey,pubkey)
    #After AES is in bytes and needs to be b64 encoded
    with open(op, 'wb') as file:
        file.write(base64.b64encode(afterAES) + b'\n')
        #Encode in utf-8 to convert into byte object since write expects that
        file.write(RSAonAESkey.encode('utf-8'))

def rsadecrypt(aeskey, prvkey):
    with open(prvkey, 'r') as file:
        for line in file:
            values=line.strip().split(',')
        n1,d1=values
    n=int(n1)
    d=int(d1)
    aeskeydecoded=base64.b64decode(aeskey)
    #Convert it to int for operations
    intaeskey=int.from_bytes(aeskeydecoded, 'big')
    Dintaeskey=pow(intaeskey, d, n)
    #from binary to bytes
    DAKinB=Dintaeskey.to_bytes((Dintaeskey.bit_length()+7)//8,'big')
    return DAKinB

def aesdecrypt(CT, Daeskey):
    AESobject2=AES.new(Daeskey, AES.MODE_ECB)
    Plaintext=AESobject2.decrypt(CT)
    removepad=unpad(Plaintext, AES.block_size)
    finalPT=removepad.decode('utf-8')
    return finalPT
    


def decryptfile(prvfile, ip, op):
    with open (ip, 'rb') as file:
        CT=base64.b64decode(file.readline().strip())
        EAESkey=file.readline().strip().decode('utf-8')
    DAESkey=rsadecrypt(EAESkey, prvfile)
    DecryptedPT=aesdecrypt(CT,DAESkey)
    with open (op, 'w') as file:
        file.write(DecryptedPT)
    
EnorDe = sys.argv[1]
key_file = sys.argv[2]
ip = sys.argv[3]
op = sys.argv[4]
if EnorDe == '-e':
    encryptfile(key_file, ip, op)
elif EnorDe == '-d':
    decryptfile(key_file, ip, op)
else:
    print("INVALID")
sys.exit(1) # type: ignore