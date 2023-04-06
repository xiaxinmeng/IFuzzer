
proxies['http']=proxies['http'] or'socks4://localhost:8080'
proxies['https']=proxies['http'] or'socks4://localhost:8080'
proxies['socks']='socks://localhost:8080'
