from warnings import warn

class TestWarning(Warning):
	def __str__(self):
		return u'\u00ae'

warn(TestWarning())