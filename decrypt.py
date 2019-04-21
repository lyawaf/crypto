import os, sys

def decrypt(file):
    import pyAesCrypt
    
    password="h"
    bufferSize=512*1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
    print("Decrypt")
    os.remove(file)
    
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if name != "Windows":
            if os.path.isfile(path):
                decrypt(path)
            else:
                walk(path)
            
walk("Test")