server = ldap.initialize(URL)
results = server.search_st(BASE, ldap.SCOPE_ONELEVEL,
    '(cn=anyone@gmail.com)',
    ['cn', 'email'])