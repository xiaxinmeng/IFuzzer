# Start a server on localhost with a random port
server = await loop.create_server(
    EchoServerProtocol,
    host="localhost",
    port=0
)

# Retrieve and log the port
port = server.sockets[0].getsockname()[1]
print(f"listening at tcp://localhost:{port}")