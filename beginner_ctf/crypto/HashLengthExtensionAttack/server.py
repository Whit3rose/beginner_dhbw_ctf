import socket
import hashlib

# ./hash_extender --data user --secret 14 --append admin --signature e90db5fd33bfd21f1e6c91a0f813473e --format md5
#                                      len(secret)
#                                                  value we want to append
#                                                                    public signature     

secret = "dhbw{use_hmac}"
data = "user"
value = secret + data
signature = hashlib.md5(value.encode())

input_hash  = data + "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x00\x00\x00\x00\x00\x00" + "admin"
required_hash = secret + input_hash

b = bytearray()
b.extend(map(ord, required_hash))
m = hashlib.md5(b)

# message = '757365728000000000000000000000000000000000000000000000000000000000000000000000000000900000000000000061646d696e'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    HOST = "0.0.0.0"
    PORT = 8080
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
