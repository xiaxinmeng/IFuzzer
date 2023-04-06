def path_return_ok(self, path, request):
    _debug("- checking cookie path=%s", path)
    req_path = request_path(request)
    if not req_path.startswith(path):
        _debug("  %s does not path-match %s", req_path, path)
        return False
    return True