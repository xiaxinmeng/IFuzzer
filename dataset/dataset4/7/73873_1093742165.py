
import smtplib
import socks

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, proxy_host, proxy_port)
socks.wrapmodule(smtplib)

smtp = smtplib.SMTP()
