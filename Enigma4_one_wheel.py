
#  Enigma 4.2 Overclocked
#  
#  Copyright 2017  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


import random
MAX_KEY_SIZE = 26
 
def getMode():
    while True:
        print('\nEnigma Encrypter v4.2 \nDo you wish to encrypt or decrypt or brute force a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = random.randrange(1, 26)
    return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        message = message[len(key) + 1:]
        key = int(key)
        key = -key

    translated = ''
    if mode[0] == 'e':
        translated += str(key) + ' '
    for symbol in message:
        if symbol.isalpha():
            if mode[0] == 'e':
                key += 1
            if mode[0] == 'd':
                key -= 1 
            if key > 26:
                key = 1
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated
while (True):
    mode = getMode()
    message = getMessage()
    if mode[0] == 'e':
        key = getKey()
    if mode[0] == 'd':
        key = ''
        for number in message:
            if number == ' ':
                break
            else:
                key += number
        #key = input("what is the first number in your encriped messege? \n")
        # uncoment to manualy enter the key
    print('Your translated text is:')
    if mode[0] != 'b':
        print(getTranslatedMessage(mode, message, key))
    else:
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, getTranslatedMessage('decrypt', message, key)) 

