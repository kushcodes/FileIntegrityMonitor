import hashlib
import logging

logging.basicConfig(filename="python_fim.log", level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

print("This is a File Integrity Monitor. Please enter the path of the file you want to monitor.")
filePath = input("Enter the file path (e.g., /home/downloads/passwords.txt): ")

def getHash(filePath):
    sha256 = hashlib.sha256()
    with open(filePath,'rb') as file:
        hash = file.read()
        sha256.update(hash)
        return sha256.hexdigest()
    
baseline = getHash(filePath)
print("[+] Just calculated your baseline")
print("[+] Checking")
while True:
    check = getHash(filePath)
    if check != baseline:
        print("[+] The file has changed")
        logging.info('is when this file changed.')
        baseline = check