
def json_default(obj):
    try:
        return obj.__json__()
    except AttributeError:
        raise TypeError("{} can not be JSON encoded".format(type(obj)))


json.dumps(foo(), default=json_default)
