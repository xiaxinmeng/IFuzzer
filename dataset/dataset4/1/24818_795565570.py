# currently this works
urllib.parse_qsl(b"qwerty")

# but after patch:
urllib.parse_qsl(b"qwerty")
# TypeError: Cannot mix str and non-str arguments