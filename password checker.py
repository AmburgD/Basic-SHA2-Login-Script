import hashlib
import json

#function to hash the password using SHA256
def encodePass(password): 
    passHash = hashlib.sha256(password).hexdigest()
    return passHash

#open a json file with the accounts
with open('accounts.json', 'r') as accounts:
 
    # Reading from json file
    accounts = json.load(accounts)

#visual check to see if persistant data worked
print(accounts)
print(type(accounts))

signIn = True

while signIn:

    choice = input("create an account [1] or sign in as existing user [2]: ")

    if choice == '1':
        username = input("Enter Username: ")
        password = input("Enter Password: ").encode("ascii")
        encryptedPass = encodePass(password)
        
        #add account data to dictonary from json file
        accounts.update({username:encryptedPass})
        print(accounts)
        
        #store account data in json file
        with open('accounts.json', 'w') as convert_file:
            convert_file.write(json.dumps(accounts, indent=4))

    elif choice == '2':
        invalid = True
        while invalid:
            username = input("Enter your username: ")
            password = input("Enter your password: ").encode("ascii")
            encryptedPass = encodePass(password)
            if username in accounts and encryptedPass in accounts.values():
                print("Welcome to DaxSoft")
                invalid = False

            else:
                print("Available accounts: ")
                print(accounts)
                print("Please try again")
    else:
        signIn = False




