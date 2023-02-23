from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# with open("master key", "wb") as mykey:
#     mykey.write(key)

with open("master key", "rb") as mykey:
    key = mykey.read()


# f = Fernet(key)

# with open("passwords.txt", "rb") as original_file:
#     original = original_file.read()

# encrypted = f.encrypt(original)

# with open("passwords.txt", "wb") as encrypted_file:
#     encrypted_file.write(encrypted)

f = Fernet(key)

with open("passwords.txt", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open("dec_passwords.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted)

master_pwd = input("what is the master password? ").lower()

def view():
    with open("dec_passwords.txt", "r") as f:
        line = f.read()
        print(line.rstrip())

def add():
    website = input("What is the name of the website: ")
    user_name = input("What is the username of your account: ")  
    pwd = input("What is the password to your account: ")
    with open("dec_passwords.txt", "a") as f:
        # Writing data to a file
        f.write(f'{website} | {user_name} | {pwd} \n')
        

    
    
def delete():
    # input text file
    inputFile = "dec_passwords.txt"
# Opening the given file in read-only mode.
    with open(inputFile, 'r') as filedata:
        # Read the file lines using readlines()
            inputFilelines = filedata.readlines()
        # storing the current line number in a variable
            lineindex = 1
        # Enter the line number to be deleted
            deleteLine = int(input("Enter the line number to be deleted = "))
        # Opening the given file in write mode.
    with open(inputFile, 'w') as filedata:
      # Traverse in each line of the file
      for textline in inputFilelines:
         # Checking whether the line index(line number) is
         # not equal to a given delete line number
         if lineindex != deleteLine:
            # If it is true, then write that corresponding line into file
            filedata.write(textline)
            # Increase the value of line index(line number) value by 1
            lineindex += 1
# Print some random text if the given particular line is deleted successfully
    print("Line",deleteLine,'is deleted successfully\n')
        



if master_pwd == "onwudinanti@20":
    while True:
        mode = input("Would you like to view your passwords, add a new one, delete one ,or quit (view/add/delete/quit): ").lower()
        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "delete":
            delete()
        elif mode == "quit":
            break
        else:
            print("Invalid mode.")
            continue
        


