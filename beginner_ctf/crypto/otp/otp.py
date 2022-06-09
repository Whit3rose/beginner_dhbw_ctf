import os

def encrypt(key, text, key_length, index):
    key_list = []
    for letter in key.lower():
        key_list.append(ord(letter) - 97)

    text_list = []
    for letter in text.lower():
        text_list.append(ord(letter) - 97)

    cipher = []
    for i, value in enumerate(text_list):
        cipher.append((value + key_list[(i + index) % key_length]) % 26)

    cipher_text = ""
    for value in cipher:
        cipher_text += chr(value + 97)

    index += len(text)
    return cipher_text, index

if __name__ == '__main__':
    key_length = 400
    key = os.environ['KEY']
    flag = "testflag"
    index = 0
    cipher, index = encrypt(key, flag, key_length, index)
    print(f"flag: {cipher}")
    while True:
        user_input = str(input("Enter the string you would like to encrypt: "))
        cipher, index = encrypt(key, user_input, key_length, index)
        print(f"cipher: {cipher}")