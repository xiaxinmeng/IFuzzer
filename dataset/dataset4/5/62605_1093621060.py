salt = base64.b64encode(os.urandom(salt_chars * 3 // 4), b"./").decode("ascii")