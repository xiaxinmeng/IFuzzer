modname = "foo.bar.baz.baq"
mod = __import__(modname, {}, {}, [modname.rsplit(".", 1)[-1]])