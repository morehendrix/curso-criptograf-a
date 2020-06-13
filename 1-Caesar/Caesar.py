plainText = input("Introduce text to cipher: ")
shift = int(input("Introduce shift: "))

def encrypt(plainText,shift):
  result = ""
  for i in range(len(plainText)):
    char = plainText[i]
     
    # Encrypt uppercase characters in plain text
    if (char.isupper()):
      result += chr((ord(char) + shift-65) % 26 + 65)
    # Encrypt lowercase characters in plain text
    elif (char.islower()):
      result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      result += char
  return result
  #check the above function

cipherText = encrypt(plainText, shift)
print("Ciphertext is: ", cipherText)
