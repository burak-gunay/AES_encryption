import os
import sys
def generate():
    key_file = open('AESkey.key','wb')
    key_file.write(os.urandom(32))
    key_file.close()

if __name__ == "__main__":
    if (sys.argv[1] == 'generate'):
        print("Generate key please")
        generate()
    elif (sys.argv[1] == 'encrypt'):
        print("Encrypt please")
    elif (sys.argv[1] == 'decrypt'):
        print("Decrypt please")
    
