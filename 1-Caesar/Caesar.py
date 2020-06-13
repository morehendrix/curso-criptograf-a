plainText = input("Introduce el texto a cifrar: ")
shift = int(input("Introduce el desplazamiento: "))

def encrypt(plainText,shift):
  result = ""
  for i in range(len(plainText)):
    char = plainText[i]
    # Mayúsculas - A = ASCII(65)
    if (char.isupper()):
      result += chr((ord(char) + shift-65) % 26 + 65)
    # Minúsculas - a = ASCII(97)
    elif (char.islower()):
      result += chr((ord(char) + shift - 97) % 26 + 97)
    # El resto de caracteres los dejamos igual
    else:
      result += char
  return result

cipherText = encrypt(plainText, shift)
print("El texto cifrado es: ", cipherText)
