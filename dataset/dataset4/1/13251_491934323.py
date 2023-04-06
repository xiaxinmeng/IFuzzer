
async with StreamServer(host, port) as server:
    await server.serve_forever()
