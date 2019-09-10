# Secret Messages
Source code is in hw2.py
In order to use this tool, ensure you have Python's cryptography package installed.

Initially, you will need to generate a key. To do so, write in the shell;

'''bash
python3 hw2.py generate
'''

This will create a key file and save it as AESkey.key

Afterwards, you can encrypt a message like this;

'''bash
python3 hw2.py encrypt FILENAME.EXTENSION
'''

This will create the encrypted file (FILENAME.enc) and unique IV (FILENAME.enc.iv). To encrypt, it will use the AESkey.key that was generated prior

To decrypt the message, you should do;

'''bash
python3 hw2.py decrypt ENCRYPTEDFILE #Last argument should be FILENAME.EXTENSION.enc
'''

The program is expecting to receive the same filename for the encrypted file as it generated, FILENAME.enc. When this is complete, it will save the decrypted message as FILENAME.encDECRYPTED.

I've provided a sample file called file.txt to test it out.
