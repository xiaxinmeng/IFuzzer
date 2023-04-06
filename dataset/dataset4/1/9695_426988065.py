def test_text_text(self):
    try:
        raise Exception("foo")
    except Exception as e:
        text = cgitb.text(sys.exc_info())
        print(text)
        self.assertNotIn('__init__', text)
        self.assertNotIn('__reduce__', text)