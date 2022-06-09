import socket
import hashlib

HOST = "127.0.0.1"
PORT = 8080

secret = "flagWithLen=14"
data = "user"
value = secret + data
signature = hashlib.md5(value.encode())

input_hash  = data + "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x00\x00\x00\x00\x00\x00" + "admin"
required_hash = secret + input_hash

b = bytearray()
b.extend(map(ord, required_hash))
m = hashlib.md5(b)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        signature = "signature: " + str(signature.hexdigest() + "\n")
        conn.sendall(bytes(signature, 'utf-8'))
        data = "data: " + data + "\n"
        conn.sendall(bytes(data, 'utf-8'))
        conn.sendall(bytes("Make sure to authenticate by appending your \'admin\' username at the end of the hash. But remember... The server always checks if the hash is valid \n", 'utf-8'))
        conn.sendall(bytes("Answer: ", 'utf-8'))
        while True:
            answer = conn.recv(1024)
            if not answer:
                break
            
            try:
                message =  secret.encode().hex() + answer.decode('utf-8')
                byte_value = bytes.fromhex(message)
                decode = hashlib.md5(byte_value)
                if m.hexdigest() == decode.hexdigest():
                    conn.sendall(bytes(secret, 'utf-8'))
                else:
                    conn.sendall(bytes("This does not look like a correct hash. Or maybe you forgot to append \'admin\'? \n Try again: ", 'utf-8'))
            except:
                conn.sendall(bytes("This does not look like a correct hash. Or maybe you forgot to append \'admin\'? \n Try again: ", 'utf-8'))
