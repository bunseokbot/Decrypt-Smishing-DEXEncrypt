import os
from Crypto.Cipher import DES
import sys
import zipfile

def main(encdir):
	print "DES/AES DEX Encryption Decryptor v0.1"
	print "Developed by bunseokbot@bob"
	print "Contact admin@smishing.kr"
	output = 'output.zip'
	des = DES.new("gjaoun\x00\x00", DES.MODE_ECB)
	with open(encdir, 'rb') as encfile:
		with open(output, 'a') as decfile:
			while True:
				chunk = encfile.read()
				if len(chunk) == 0:
					break	
				decfile.write(des.decrypt(chunk))

	dex = zipfile.ZipFile(output)
	dex.extract('classes.dex')
	os.remove('output.zip')
	print "Decrypt DEX Success!"

if __name__ == "__main__":
	try:
		main(sys.argv[1])
	except Exception, e:
		print e
		print "Usage : python decrypt.py <encrypted_dex>"
