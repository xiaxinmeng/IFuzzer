buffer = io.Bytes()
with io.TextIOWrapper(buffer, encoding='utf8') as text_buffer:
    write_content_to(text_buffer)
    text_buffer.flush()
    text_buffer.detach()