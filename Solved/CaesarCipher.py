def caeserChiperEnc(string,key):
    newLetters=[]
    newKey = key %26
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey))
    return "".join(newLetters)

def getNewLetter(letter,key):
    nLc= ord(letter)+key
    if nLc<=122:
        return chr(nLc)
    else:
        return chr(96+nLc%122)
