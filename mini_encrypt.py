import sys
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

if len(sys.argv) != 4:
    print("[!] Invalid number of arguments")
    print("[!] Usage: python mini_encrypt.py ['encrypt' or 'decrypt'] [key file] [target file]")
    exit(1)

_filename, action, rsa_key_file, target_file = sys.argv

infile  = open(target_file,  "r")
keyfile = open(rsa_key_file, "r")
rsa_key = RSA.import_key(keyfile.read())
rsa     = PKCS1_OAEP.new(rsa_key)

if action == "encrypt":
    outfile = open("message.encyrpted", "w")
    infile  = open(_filename, "r")
    block   = AES.block_size
    secret  = get_random_bytes(32)
    iv      = get_random_bytes(16)
    aes     = AES.new(secret, AES.MODE_GCM, iv)
    cipher_text, mac = key.encrypt_and_digest(plaintext)

    outfile.write( rsa.encrypt(secret) )
    outfile.write( rsa.encrypt(iv)     )
    outfile.write( rsa.encrypt(mac)    )
    
elif action == "decrypt":
    # Decrypt and print
else:
    print(f"Invalid action '{action}', choose either 'encrypt' or 'decrypt'")
