'''
    Vigenère cipher

'''

def generateKey(string, key): 
    

    if len(string) == len(key): 
        return key

    else: 
        key = list(key)
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 

    return("" . join(key)) 
      

def cipherText(string, key):
    _key = list(key)
    alphabeth = list(range(97, 123))
    
    table = {}
    for char in alphabeth:
        table[chr(char)] = list(map(chr,range(char, 123)))
        i = 97
        while len(table[chr(char)]) < 26:
            table[chr(char)].append(chr(i))
            i+=1

    result = []
    for s in string:

        ascii = ord(s)

        if ascii >= 97 and ascii <= 122:
            row = _key.pop(0)
            column = ord(s) - 97
            result.append(table[row][column])
        else:
            result.append(s)

    return "".join(result)

def encode():

    string = input()
    code = input()
    key = generateKey(string, code)

    return cipherText(string,key) 


