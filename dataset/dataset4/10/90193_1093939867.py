# python/Lib/mimetypes.py

class MimeTypes:
# ...
    def guess_type(self, url, strict=True):
# ...

        if ext in _types_map_default:
            # prefer the python-internal values over /etc/mime.types
            return _types_map_default[ext], encoding

        if ext in types_map:
            return types_map[ext], encoding