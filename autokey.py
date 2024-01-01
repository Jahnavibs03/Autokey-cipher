alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    while True:
        print(" 1.Encryption \n 2.Decryption \n 3.exit\nEnter the choice: ")
        choice = int(input())
        if choice == 3:
            print("THANKYOU!!!")
            break
        if(choice == 1):
            print("Enter the plain text:  ")
        else:
            print("Enter the cipher text:  ")
        msg = input().upper()
        print("Enter the auto key:  ")
        key = input().upper()
        if key.isdigit():
            key = alphabet[int(key)]
        if choice == 1:
            enc = autoEncryption(msg, key)
            print("Plaintext : " + msg)
            print("key: " + key + msg)
            print("Encrypted : " + enc)
        elif choice == 2:
            enc = autoDecryption(msg, key)
            print("Plaintext : " + msg)
            print("key: " + key + msg)
            print("Decrypted : " + enc)
        else:
            print("Wrong choice!!!")

def autoEncryption(msg, key):
    len_msg = len(msg)
    new_key = key + msg
    new_key = new_key[:len(new_key) - len(key)]
    encrypt_msg = ""
    for x in range(len_msg):
        first = alphabet.index(msg[x])
        second = alphabet.index(new_key[x])
        total = (first + second) % 26
        encrypt_msg += alphabet[total]
    return encrypt_msg

def autoDecryption(msg, key):
    current_key = key
    decrypt_msg = ""
    for x in range(len(msg)):
        get1 = alphabet.index(msg[x])
        get2 = alphabet.index(current_key[x])
        total = (get1 - get2) % 26
        total = total + 26 if total < 0 else total
        decrypt_msg += alphabet[total]
        current_key += alphabet[total]
    return decrypt_msg.lower()

if __name__ == "__main__":
    main()