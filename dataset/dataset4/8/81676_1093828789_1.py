
def do_ping(request):
    """This is an insecure example, DO NOT REUSE THIS CODE"""
    ip = request['ip']

    # Try to parse as ipv4 and save to db as just 4 bytes
    try:
       ip_bytes = socket.inet_aton(ip)
    except OSError:
       return 'IP is not a valid IPv4.'

    save_ping_request_to_db(ip_bytes)

    return subprocess.check_output('ping -c1 %s' % ip, shell=True)  # an ip of "1.1.1.1 ; whomai" triggers a command injection vulnerability here
