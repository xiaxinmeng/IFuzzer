def toprettyxml(self, indent="\t", newl="\n", encoding=None):
    # indent = the indentation string to prepend, per level
    # newl = the newline string to append
    use_encoding = "utf-8" if encoding is None else encoding
    writer = codecs.getwriter(use_encoding)(io.BytesIO())
    if self.nodeType == Node.DOCUMENT_NODE:
        # Can pass encoding only to document, to put it into XML header
        self.writexml(writer, "", indent, newl, encoding)
    else:
        self.writexml(writer, "", indent, newl)
    if encoding is None:
        return writer.stream.getvalue().decode(use_encoding)
    else:
        return writer.stream.getvalue()