# pass_fmanipulator.py file responsible for using the "alternate data streams"
# and creating/opening files
import os
import pass_crypt


'''create_file function creates a new file with the encrypted text in the alternate stream'''
def create_file(file_name,key, set_list):
    text = ""
    for curr_set in set_list:
        text += "{"+curr_set.getPlat()+":"+curr_set.getName()+":"+curr_set.getPass()+"},"
    enc_text = pass_crypt.encrypt(text,key)

    fname = pass_crypt.hash_txt(file_name)
    reg_inp = os.system('cmd /c echo ' + fname + ' >> ' + fname + '.txt')
    stream_inp = os.system('cmd /c echo '+enc_text.hex()+' > '+fname+'.txt:'+fname)
    print("result: ", stream_inp,stream_inp)


'''get_from_file function opens the correct file and returns the decrypted text'''
def get_from_file(list_name,key):
    try:
        print('trying to open ',list_name)
        fname = pass_crypt.hash_txt(list_name)
        print('hashed file_name is ', fname)
        with open(fname+".txt:"+fname, "r") as file:

            decrypted = pass_crypt.decrypt(bytes.fromhex(file.read()), key)
            print('decrypted ',decrypted)
            if decrypted[:7].decode() == 'success':
                return decrypted[7:]
    except:
        return -1


'''delete_file function deletes the file by the list name'''
def delete_file(list_name):
    fname = pass_crypt.hash_txt(list_name)
    if os.path.exists(fname+".txt"):
        os.remove(fname+".txt")
        return 0
    else:
        print("File does not exist")
        return -1