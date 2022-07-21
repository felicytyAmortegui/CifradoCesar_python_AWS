#abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
#print(getDoubleAlphabet(abc))

def getMessage():
    stringToEncrypt = input("Por favor, ingresa el mensaje a cifrar: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input( "Ingresa la llave por favor (entre el numero 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
#print(encryptMessage("Gato!", 3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#print(decryptMessage("JDWR!", 3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


#print(encryptMessage("Perro", 3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#print(decryptMessage("SHUUR", 3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
runCaesarCipherProgram()

    



    
