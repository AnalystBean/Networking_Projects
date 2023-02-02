def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_value = ord(char) + shift
            if char.isupper():
                ciphertext += chr(shift_value) if shift_value <= 90 else chr(shift_value-26)
            else:
                ciphertext += chr(shift_value) if shift_value <= 122 else chr(shift_value-26)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_value = ord(char) - shift
            if char.isupper():
                plaintext += chr(shift_value) if shift_value >= 65 else chr(shift_value+26)
            else:
                plaintext += chr(shift_value) if shift_value >= 97 else chr(shift_value+26)
        else:
            plaintext += char
    return plaintext