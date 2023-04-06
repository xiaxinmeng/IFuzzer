def connect():
    (major, minor, micro, releaselevel, serial) = sys.version_info
    if major == 2 and minor < 7:
        conn = NSSHTTPS(host, 443, dbdir="/etc/pki/nssdb")
    else:
        conn = NSSConnection(host, 443, dbdir="/etc/pki/nssdb")