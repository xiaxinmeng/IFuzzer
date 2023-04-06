def setUp(self):
  try:
    do_a_bunch_of_stuff_that_could_fail()
  finally:
    conditionally_undo_setup()
  do_more()

def conditionally_undo_setup(self):
  if self.foo: 
    self.foo.close()
  if self.bar:
    shutil.rmtree(self.bar)

def tearDown(self):
  conditionally_undo_setup()
  undo_more()