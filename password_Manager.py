from cryptography.fernet import Fernet

'''
def key_generator():
    key = Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)'''

def key_loader():
    file=open('key.key', 'rb')
    key = file.read()
    return key

master_pwd = input("What is the master password: ")

if master_pwd != "hello":
    print("The master password you entered is wrong!")
    exit()
key = key_loader() 
fer = Fernet(key)

def view():
    try:

        with open("password.txt", 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User :",user, " Password :" ,fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("password.txt file is not found")

def add():
    Account = input("Account name:")
    pwd = input("Enter the password: ")

    with open("password.txt",'a') as f:
        f.write(Account + "|" +fer.encrypt(pwd.encode()).decode()+ "\n")

while True:
    mode = input("Do u want to add new password or view existing one (view,add), press q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
