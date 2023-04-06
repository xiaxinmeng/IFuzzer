import crypt

for salt in ('foo', '$2a$04$5BJqKfqMQvV7nS.yUguNcueVirQqDBGaLXSqj.rs.pZPlNR0UX/HK'):
    t = 'test'
    h = crypt.crypt(t, salt)
    print("'%s' with '%s' -> %s" % (t, salt, h))