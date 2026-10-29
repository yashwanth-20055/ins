#Certificate Generation Command

#```openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes```


#Server.py
import socket
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("server.crt", "server.key")
server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)
with context.wrap_socket(server, server_side=True) as ssock:
    conn, addr = ssock.accept()
    print("Secure connection established")
    data = conn.recv(1024).decode()
    print("Client:", data)
    conn.send(b"Hello from secure server")
    conn.close()


#Client.py
import socket
import ssl
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
with socket.create_connection(("localhost", 12345)) as sock:
    with context.wrap_socket(sock, server_hostname="localhost") as ssock:
        ssock.send(b"Hello from secure client")
        print("Server:", ssock.recv(1024).decode())