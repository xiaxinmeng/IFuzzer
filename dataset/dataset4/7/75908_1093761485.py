import ssl
import ftplib

print(ssl.OPENSSL_VERSION)

ftps = ftplib.FTP_TLS('test.rebex.net', timeout=2)
ftps.ssl_version = ssl.PROTOCOL_TLS
ftps.login('demo','password')

ftps.prot_p()
ftps.set_pasv(True)
ftps.dir()
ftps.nlst()
ftps.retrlines('LIST')