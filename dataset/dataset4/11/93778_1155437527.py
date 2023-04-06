
def erase_text():
    global text
    text = text[1:]
    c.itemconfigure(text_item, text=text)
    c["width"], c["height"] = c["width"], c["height"]
    if text:
        root.after(10, erase_text)
