import sys
import socket
import selectors
import types
import numpy as np

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    conn.sendall(b"Welcome to our calculator. We can calculate your input times 4. You can only enter integers! \n")
    conn.sendall(b"We just have to make sure that we do not receive -4 as a value: ")
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            calculation = np.array([0], dtype=int)
            user_input = str(data.outb.decode('utf-8')).strip("\n")
            try:
                number_input = int(user_input)

                if number_input == -4:
                    sock.sendall(b"This is not allowed!!!")

                else:
                    calculation[0] = number_input
                    calculation[0] = calculation[0] * 4
                    if calculation[0] == -4:
                        sock.sendall(b"dhbw{you_overflowed_me}")
                    else:
                        sock.sendall((str(calculation[0]) + '\nanother? ').encode('UTF-8'))
            except:
                sock.sendall(("Something went wrong with your input. Please try again but with a number!: \n").encode('UTF-8'))

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
