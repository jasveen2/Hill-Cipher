import string
import numpy as np
import math
import sys
from sympy import Matrix

key = sys.argv[1]
raw_message = sys.argv[2]
raw_message = raw_message.lower() ## make message lowercase
mode = sys.argv[3]
mode = mode.lower()

if len(raw_message) % 2 != 0:
    raw_message += "z" ## add a z if uneven # of letters to form digraphs

def tonum(letter):
    return string.ascii_lowercase.index(letter) - 1 ## - 1 because a = 0

def toletter(number):
    return chr(int(number) + 97) ## ascii (lowercase a = 97)

l1 = tonum(key[0]) + 1
l2 = tonum(key[1]) + 1
l3 = tonum(key[2]) + 1
l4 = tonum(key[3]) + 1

key = np.array([ [l1, l2], [l3, l4] ]) ## form a double array with the numeric version of the key

key_rows = key.shape[0]

def tomatrix(raw_message, key_rows): ## turn an alphabetic message into a matrix (split into digraphs)
    message = []
    for i in range(0, len(raw_message)):
        current_letter = (raw_message[i:i+1]).lower()
        if current_letter != ' ': ## not whitespace
            letter_index = tonum(current_letter) ## turn the letter into a numeric version
            message.append(letter_index + 1) ## add to message
    message = np.array(message) ## turn message into a double array
    message_length = message.shape[0]
    message.resize(int(message_length/key_rows), key_rows) ## make sure it is resized properly
    return message

def encrypt(message, key): ## encrypt a digraph
    encryption = key @ message ## product of arrays
    encryption = np.remainder(encryption, 26) ### mod 26 for the alphabet
    return encryption

def invkey(key): ## find the inverse of a matrix (needed for decryption)
    inv = Matrix(key).inv_mod(26) ## use sympy function to get the inverse matrix
    inv = np.array(inv) ## turn it back into an array
    inv = inv.astype(float) ## type cast
    return inv

def decrypt(encrypt, inverse): ## decrypt a digraph
    decryption = inverse @ encrypt ## multiply the inverse key by the encoded message
    decryption = np.remainder(decryption, 26).flatten()
    finalmessage = ""
    for i in range(0, len(decryption)):
        letter = toletter(decryption[i]) ## turn number back into letter
        finalmessage = finalmessage + letter ## add letter back to final message
    return finalmessage

def Hill(mode):
    if mode == "encrypt":
        message = tomatrix(raw_message, key_rows) ## turn message given into matrix
        encryptm = "" ## encrypted message
        for i in range(0, len(message)):
            encrypted = encrypt(message[i], key) ## encrypt each digraph
            encryptm = encryptm + toletter(encrypted[0]) + toletter(encrypted[1]) ## turn back into letters and add to encrypted message
        return encryptm
    else:
        inverse = invkey(key) ## take inverse of the key given
        message = tomatrix(raw_message, key_rows) ## turn encrypted message given into matrix
        decryptm = "" ## decrypted message
        for i in range(0, len(message)):
            decrypted = decrypt(message[i], inverse) ## decrypt digraphs
            decryptm += decrypted ## add decrypted letters
        return decryptm

print(Hill(mode))
