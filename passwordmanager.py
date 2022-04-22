#program to manage passwords
from cryptography.fernet import Fernet

'''def write_key(key):
    key=Fernet.generate_key()

    with open('key.key','wb') as f:
        f.write(key)

write_key(pwd)'''

def load_key():
    file= open('key.key','rb') 
    key=file.read()
    file.close()
    return key



pwd=input("What is the master password:")
key=load_key()+pwd.encode()
fer=Fernet(key)


def add():
    pwd=input("Account Name:")
    passw=input("Input Password:")


    with open('passwords.txt','a') as f:
        f.write(pwd + "|" + str(fer.encrypt(passw.encode)) + "\n")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            passw=line.rstrip()
            print(passw,str(fer.decrypt(passw.encode)))



while True:
    mode=input("Enter V to view your password or A to add a new password or q to quit:").lower()

    if mode=="a":
        add()
    elif mode=="v":
        view()
    elif mode=="q":
        break
    else:
        print("Invalid input")
        print("")
        print("Game Over")
        print("")
        break
