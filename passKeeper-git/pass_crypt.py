# pass_crypt.py - responsible for cryptography of texts and passwords
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import string
import secrets


'''pad funtion pads the text with zeroes to a correct block size'''
def pad(s):
    return s+b"\0"*(AES.block_size - len(s) % AES.block_size)


'''pad_key function pads the password with zeroes to the size of 16 or 32'''
def pad_key(key):
    for i in range(4,5):
        if len(key) < pow(2, i):
            print('padded key: ', key + '0' * (pow(2, i)-len(key)))
            return key+'0'*(pow(2, i)-len(key))
        else:
            print('key is shorter than ',pow(2, i))
    return key[:32]


'''encrypt function encrypts the text with the password as a key and returns the cipher with the iv'''
def encrypt(message, key, key_size=256):
    print('encrypting {}, with key: {}'.format(message,key))
    pad_key(key)
    message = pad(b'success'+message.encode())
    iv = Random.new().read(AES.block_size)
    print('iv: ', iv)
    cipher = AES.new(pad_key(key).encode(), AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)


'''decrypt function decrypts the text using the passwords and returns the plain text'''
def decrypt(cipher_text, key):
    print('decrypting {}, with key {}'.format(cipher_text, key))
    iv = cipher_text[:AES.block_size]
    print('iv ',iv)
    cipher = AES.new(pad_key(key).encode(), AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(cipher_text[AES.block_size:])
    print('plain_text ', plain_text)

    print(plain_text[:6])
    return plain_text.rstrip(b"\0")


'''hash_txt function gets a text and returns its hash'''
def hash_txt(text):
    print('hashing ', text)
    sha1 = hashlib.sha1()
    sha1.update(text.encode())
    print('{}:{}'.format(sha1.name, sha1.hexdigest()))
    return sha1.hexdigest()


'''get_pass function creates and returns a random password from the alphabet'''
def get_pass(len):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*'
    print(alphabet)
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if sum(c.isupper() for c in password) >= 2 and sum(c.isdigit() for c in password) >= 2:
            break
    print(password)
    return password


'''pass_check gets a password and returns a grade to describe its strength'''
def pass_check(password):
    grade = 0
    options = [False for i in range(5)]
    if len(password) > 8:
        options[0] = True
    for element in password:
        if element in string.ascii_uppercase:
            options[1] = True
        if element in string.ascii_lowercase:
            options[2] = True
        if element in string.punctuation:
            options[3] = True
        if element in string.digits:
            options[4] = True

    for i in options:
        if i:
            grade += 20
    return grade
