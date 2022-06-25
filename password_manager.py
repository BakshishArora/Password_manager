from time import time
from cryptography.fernet import Fernet

# key + password +text to encrypt = random text 
# random text + password + key = text to encrpt 

# the write_key function is defined to generate a random key for encrpting the master password 

'''def write_key():
    key = Fernet.generate_key()
    #wb= white bytes
    with open("key.key", "wb") as keyfile:
        keyfile.write(key)

# the load_key function stores the encrypted key 
#  compares it with the enterd master password 
# if not matched retuns garbage values'''
def load_key():
    file= open("key.key","rb")
    key= file.read
    file.close()



pwd= input("Input the Master Password : ")
#write_key()
#encode() converts the strings into bytes
#key= (b'load_key()') + pwd.encode()
#fer = Fernet(key)

def view():
    with open("passwords.txt", 'r') as f:
        for lines in f.readlines():
            data =lines.rstrip()
            user, password= data.split("|")
            print("User : ", user ,"---","Password :", password)
    


def add():
    while True:

        name =input("Account Name :")
        pwd2= input("Enter the new Password :")
        con_pwd2 =input("Re-enter the Password :")
        if pwd2==con_pwd2:
            with open("passwords.txt", 'a') as f:
                f.write(name + "|" + pwd2 + "\n")
                another=input("Add another one? (y/n)")
                if another=='y':
                    continue
                elif another=='n':
                    break
                else:
                    print("Wrong Choice !")
                    break
        else:
            print("You have entered the wrong password! Try again")
            break
            
    #file = open("passwords.txt", 'a') 
    #file.close()


while True:
    mode= input("would you like to access an old password or add new?  (view ,add)  press q to quit ").lower()
    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode!")
        continue
