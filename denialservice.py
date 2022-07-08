from socket import AF_INET, SOCK_STREAM, socket

gateway = (
    # Host,
    # port
)
payload = b'''GET / HTTP/1.1

'''

while True:
    with socket(AF_INET, SOCK_STREAM) as so:
        so.connect(gateway)
        so.sendall(payload)
