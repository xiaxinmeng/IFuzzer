factory = unittest.mock.Mock()

### test example
foo_obj = factory.create("foo"),do_thing()

# !! MUST BE CALLED AFTER .create("foo") !!
bar_obj = factory.create("bar").do_thing()
###