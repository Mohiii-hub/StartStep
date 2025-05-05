# Caesar Cipher Encrypt
def caesar_cipher_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    print(result)
    return result

# Caesar Cipher Decrypt
def caesar_cipher_decrypt(text, shift):
    # To decrypt, we reverse the shift by using -shift
    return caesar_cipher_encrypt(text, -shift)

# Example usage
eingabe_Text = str(input("Tippe dei Satz ein :"))
eingabe_Zahl = int(input("Tippe dein Key ein:"))
encrypted = caesar_cipher_encrypt(eingabe_Text,eingabe_Zahl)
print("Encrypted:", encrypted)

decrypted = caesar_cipher_decrypt(encrypted, eingabe_Zahl)
print("Decrypted:", decrypted)