# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 02:18:23 2017

@author: dianlin
"""
import random

""" 

Encrypt a message by shifting the message by a given amount of time

"""

def encryption(string,rotation):
    resultString = ""
    if rotation<0:
        rotation = rotation +26
    for letter in string:
        # Check if the letter is upper-case
        if(isUpper(letter)):
            # Encrypt and add the letter to the resultString
            resultString = resultString + str(encryptionUpperCase(letter,rotation))
        # Check if the letter is upper-case
        elif (isLower(letter)):
            # Encrypt and add the letter to the resultString
            resultString = resultString + str(encryptionLowerCase(letter,rotation))
        # If it is not a letter, add it to the resultString
        else:
            resultString = resultString + letter
    return resultString
    
""" 

Encrypt a lower case letter by shifting the letter by a given amount of time

"""      

def encryptionLowerCase(char,rotaion):
    resultchar = chr(ord(char)+rotaion)
    if(ord(resultchar)>122):
        resultchar = chr(ord(resultchar)-26)
    if(ord(resultchar) < 97):
        resultchar = chr(ord(resultchar)+26)
    return resultchar
    
""" 

Encrypt an upper case letter by shifting the letter by a given amount of time

"""  

def encryptionUpperCase(char,rotataion):
    resultchar = chr(ord(char)+rotataion)
    if(ord(resultchar)>90):
        resultchar = chr(ord(resultchar)-26)
    if(ord(resultchar)< 65):
        resultchar = chr(ord(resultchar)+26)
    return resultchar
  
  
"""

Check if the char is an upper case letter 

"""

def isUpper(char):
    if (ord(char)<=90 and ord(char)>=65):
        return True
    return False
    
"""

Check if the char is an lower case letter 

"""

def isLower(char):
    if (ord(char)<=122 and ord(char)>=97):
        return True
    return False

""" 

Decrypt a message by shifting the message by a given amount of time

"""

def decryption(string,number):
    rotation = -1*number
    resultString = encryption(string,rotation)
    return resultString

task = input("Enter e to encrypt and d to decrypt \n")
if(task=="e"):
    messageToEncrypt = input("Message to encrypt \n")
    random_key = random.randrange(27)
    encryptedMessage = encryption(messageToEncrypt,random_key)
    print("Your encrypted message is "+encryptedMessage +
            " and your key is "+ str(random_key))
elif(task=="d"):
    messageToDecrypt = input("Message to decrypt \n")
    key = input("Enter your key \n")
    decryptedMessage = decryption(messageToDecrypt,int(key))
    print ("Your decrypted message is "+decryptedMessage)
