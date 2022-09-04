#main.py - main programm
import pass_viewer as pv

'''
this programm will keep sets of {"platform":"username":"password"} in a 'Alternate data stream' files
the passwords will be incripted using a key
function to randomize a key/pass word
function to check password strenth
ask for a password (or a face recognition, or a picture) to show saved passwords
passwords (including platform name and username) can be updated and encrypted again
(check) if the file with the encrypted data is sent, the data is stripped off
(if ^ is true) the data can be accessed only from the users computer with the files
'''

def start_passkeeper():
    print(f'Hello and Welcome to the passKeeper')
    pv.loop_funct()


if __name__ == '__main__':
    start_passkeeper()
