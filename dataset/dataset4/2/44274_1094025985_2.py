def get_text(self, text_id):
	try:
		r = self.tk.call(self._w, 'itemconfigure', text_id, '-text')
		return self.tk.splitlist(r)[-1]
	except TclError:
		return ''