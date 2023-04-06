GetCfgSectionNameDialog_spec = {
  'kwds': {'title':'Get Name',
         'message':'Enter something',
         'used-names': {'abc'}},
  'msg': "After the text entered with [Ok] is stripped, <nothing>, "
         "'abc', or more that 30 chars are errors. "
         "Close with a valid entry (printed), [Cancel], or [X]"}

def run(klas):
  root = tk.Tk()
  klas_spec = globals[klas.__name__+'_arg']
  klas_spec.kwds['parent'] = root # does Idle use 'parent' consistently?
  def run_klas():
    widget = klas(**klas_spec.kwds)
    try:
      print(widget.result)
    except AttributeError:
      pass
  Message(root, text=klas_spec.msg).pack()
  Button(root, text='Test ' + klas.__name__, command=run_klas).pack()
  root.mainloop()