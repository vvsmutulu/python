import getpass
import hashlib
import os
clear = lambda: os.system('cls')


def main():
    clear()
    print("MAIN MENU")
    print("---------")
    print()
    print("1 - Register")
    print("2 - login")
    print()
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1','2']:
            break
    if userChoice == '1':
        register()
    else:
        login()
        
    

def register():
    clear()
    print("REGISTER")
    print("--------")
    print()
    while True:
        userName = input("Enter Your Name").title()
        if userName != ' ':
            break
    userName = sanitizeName(userName)
    while True:
        userPassword = input("Enter Your Password: ")
        if userPassword != '':
            break
    while True:
        confirmPassword = input("Confirm your password: ")
        if confirmPassword == userPassword:
            break
        else:
            print("Passwords Don't Match")
            print()
    if userAlreadyExist(userName, userPassword):
        while True:
            print()
            error = input("You are already registered.\n\n Press (T) to try again:\nPress (L) To Login: ").lower()
            if error == 'T':
                Register()
                break
            elif error == 'L':
                login()
                break
    addUserInfo([userName, hash_password(userPassword)])
    
def login():
    clear()
    print("LOGIN")
    print("-----")
    print()
    userInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            userInfo.update({line[0]: line[1]})
    while True:
        userName = input("Enter your name: ")
        userName = sanitizeName(userName)
        if userName not in usersInfo:
            print("You are not registered")
            print()
        else:
            break
    print()
    print('Logged In') 

def addUserInfo():
    with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')
        

def userAlredyExist(userName, userPassword):
    usersInfo = {}
    with open('userInfo.txt', 'r')as file:
        for line in file:
            line = line.split()
            if line[0] == userName and line[1] == hash_password(userPassword):
                usersInfo.update({line[0]: line[1]})
    if usersInfo == {}:
        return False
    return usersInfo[userName] == userPassword

                                                                

def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName
    

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    return hash_password(password) == hash

main()

                        
