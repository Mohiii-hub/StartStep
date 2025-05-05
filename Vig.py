#Vigenere Cipher Encryption
def repeat_key(text, key):
    #Repeat
    repeated_key = ""
    key_index = 0
    for char in text:
        if char.isalpha():  # فقط برای حروف
            repeated_key += key[key_index % len(key)]
            key_index += 1
        else:
            repeated_key += char  # فاصله یا علامت‌ها رو همونطور می‌ذاریم
    return repeated_key

def encrypt_vigenere(text, key):
    text = text.upper()
    key = repeat_key(text, key.upper())
    encrypted = ""

    for t, k in zip(text, key):
        if t.isalpha():
            c = chr(((ord(t) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A'))
            encrypted += c
        else:
            encrypted += t  # فاصله یا علامت‌ها رو همونطور می‌ذاریم
    return encrypted

def decrypt_vigenere(cipher, key):
    cipher = cipher.upper()
    key = repeat_key(cipher, key.upper())
    decrypted = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            t = chr(((ord(c) - ord('A')) - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
            decrypted += t
        else:
            decrypted += c
    return decrypted

# Test
message = "Hallo"
key = "Mohi"

encrypted = encrypt_vigenere(message, key)
print("Encrypt:", encrypted)

decrypted = decrypt_vigenere(encrypted, key)
print("رمزگشایی شده:", decrypted)