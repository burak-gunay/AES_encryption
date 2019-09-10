import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
#Generates the key &creates a new file if it does not exist. If the file exists, simply overwrite it
def generate():
    key_file = open('AESkey.key','wb')
    key_file.write(os.urandom(32))
    key_file.close()
def encrypt(msg_filename):
    #One of the things, generate a new iv for each encryption and save it accordingly.
    msg_file = open(msg_filename,'rb')
    plaintext = msg_file.read()

    key_file = open('AESkey.key','rb')
    key = key_file.read()

    #Now, also make a corresponding iv
    iv = os.urandom(16)
    iv_file = open(msg_filename + 'IV.iv','wb')
    iv_file.write(iv)

    padder = padding.PKCS7(256).padder()
    padded_plaintext = padder.update(plaintext)
    padded_plaintext += padder.finalize()
    
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key),modes.CBC(iv),backend = backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_plaintext) + encryptor.finalize()

    encrypted_file = open(msg_filename + '.enc','wb')
    encrypted_file.write(ct)
    
    msg_file.close()
    key_file.close()
    iv_file.close()
    encrypted_file.close()
    pass
def decrypt(msg_filename):
    encrypted_file = open(msg_filename + '.enc','rb')
    padded_ciphertext = encrypted_file.read()

    key_file = open('AESkey.key','rb')
    key = key_file.read()
    
    iv_file = open(msg_filename + 'IV.iv','rb')
    iv = iv_file.read()

    backend = default_backend()
    cipher = Cipher(algorithms.AES(key),modes.CBC(iv),backend = backend)
    decryptor = cipher.decryptor()

    unpadder = padding.PKCS7(256).unpadder()
    ciphertext = unpadder.update(padded_ciphertext)
    ciphertext += unpadder.finalize()

    decrypted_msg = decryptor.update(ct) + decryptor.finalize()
    print(decrypted_msg)
    
    pass
    
if __name__ == "__main__":
    if (sys.argv[1] == 'generate'):
        print("Generate key please")
        generate()
        pass
    elif (sys.argv[1] == 'encrypt'):
        if (len(sys.argv) != 3):
            raise Exception('encrypt usage is like: python3 hw2.py encrypt FILENAME.EXTENSION')
        print("Encrypt please")
        encrypt(sys.argv[2])
        pass
    elif (sys.argv[1] == 'decrypt'):
        print("Decrypt please")
        if (len(sys.argv) != 3):
            raise Exception('decrypt usage is like: python3 hw2.py decrypt FILENAME.EXTENSION')
        decrypt(sys.argv[2])
        pass
    else:
        print('wrong command')
        pass
    pass
