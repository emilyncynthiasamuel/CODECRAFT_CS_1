def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char   
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)   

def main():
    print("Caesar Cipher")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()

    if choice == 'E':
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}")
    elif choice == 'D':
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
