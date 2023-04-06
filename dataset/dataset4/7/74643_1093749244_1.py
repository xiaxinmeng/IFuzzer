def do_request_(self, request):
    host = request.host
    ...
    sel_host = host
    ...
    if not request.has_header('Host'):
        request.add_unredirected_header('Host', sel_host)