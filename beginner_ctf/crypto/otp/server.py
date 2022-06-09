import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
key_length = 400
otp_key = "fctkmkxfjfzxrmqpcgfwmmuqdmnuehtfcbhjztnuuerurczgjenaehnpuqnarujauxpktjcpygefavhdcmqadyudgwjbcaaygymvfcknkzjminnqimktdbknprzczwprbjegdhjfhjqiynwyddmafgvtgpzcyigxhgfzywkiwxmyzgvhfxrigpcqmfheemfhmxpydbbftimhrhyphnpaafebuzejbddqwyqickhfpbjweyjwicmxnbauibqcdbnkjcbqcukkwbiuwcinezfmcxvvwgqainyrhibajbehmpqfcykneveqtiuyrcwcftfbxkpiambekqfzpxhigakwvarcpajzzwfdzimjpefzjrcpzdbwpywpnkibzukbkxrkufynaykkcihgfwik"
flag = "einonetimepadsollteeinonetimepadbleiben"


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    cipher, index = encrypt(otp_key, flag, key_length, 0)
    conn.sendall(bytes(f"flag: {cipher} \n", 'utf-8'))
    conn.sendall(bytes("Enter the string you would like to encrypt: ", 'utf-8'))

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


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            try:
                user_input = str(data.outb.decode('utf-8')).strip('\n')
                global index
                cipher, index = encrypt(otp_key, user_input, key_length, index)
                sock.sendall(bytes(f"cipher: {cipher} \n", 'utf-8'))
                sock.sendall(bytes("Enter the string you would like to encrypt below: ", 'utf-8'))
            except:
                sock.sendall(bytes("Something went wrong. Please renter the string you would like to encrypt below: ", 'utf-8'))
            sock.sendall(bytes(" -- Your last string: ", 'utf-8'))
            sent = sock.send(data.outb) 
            data.outb = data.outb[sent:]

host = "0.0.0.0"
port = 8080
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
index = 40
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
