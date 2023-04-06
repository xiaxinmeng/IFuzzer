cert_paths = [
    # Debian, Ubuntu, Arch, SuSE
    # NetBSD (security/mozilla-rootcerts)
    "/etc/ssl/certs/",
    # Debian, Ubuntu, Arch: maintained by update-ca-certificates
    "/etc/ssl/certs/ca-certificates.crt",
    # Red Hat 5+, Fedora, Centos
    "/etc/pki/tls/certs/ca-bundle.crt",
    # Red Hat 4
    "/usr/share/ssl/certs/ca-bundle.crt",
    # FreeBSD (security/ca-root-nss package)
    "/usr/local/share/certs/ca-root-nss.crt",
    # FreeBSD (deprecated security/ca-root package, removed 2008)
    "/usr/local/share/certs/ca-root.crt",
    # FreeBSD (optional symlink)
    # OpenBSD
    "/etc/ssl/cert.pem",
    # Mac OS X
    "/System/Library/OpenSSL/certs/cert.pem",
    ]