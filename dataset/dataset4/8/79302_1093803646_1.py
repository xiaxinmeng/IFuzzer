def path_return_ok(self, path, request):
    req_path = request_path(request)
    if req_path == path:
        return True
    elif req_path.startswith(path) and ((path.endswith("/") or req_path[len(path)] == "/")):
        return True
        
    return False