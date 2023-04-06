def _write_data(writer, data, is_attrib=False):
    "Writes datachars to writer."
    data = data.replace("&", "&amp;").replace("<", "&lt;")
    data = data.replace("\"", "&quot;").replace(">", "&gt;")
    if is_attrib: 
        data = data.replace("\r", "&#13;").replace("\n", "&#10;")
    writer.write(data)