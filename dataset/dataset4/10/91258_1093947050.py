with self.create_alg('hash', 'hmac(sha1)') as algo:
    algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, b"Jefe")
    op, _ = algo.accept()
    with op:
        op.sendall(b"what do ya want for nothing?")
        self.assertEqual(op.recv(512), expected)