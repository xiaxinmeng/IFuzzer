import _ssl

def main():
    while True:
        _ssl._test_decode_cert("/path/to/cert.pem")

main()