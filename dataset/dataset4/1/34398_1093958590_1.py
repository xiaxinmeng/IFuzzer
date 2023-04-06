def badkey(self, event):
    try:
        if ord(event.char) > 127:
            txt.insert("insert", unicode
(event.char,"cp1252"))
            return "break"
    except:
        pass