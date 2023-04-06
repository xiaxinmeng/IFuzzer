import token
_tok = next(tokenize.tokenize(io.BytesIO(b"").readline))
token.tok_name[_tok.type] = "BACKQUOTE"
for number, name in token.tok_name.items() :
    if not hasattr(token, name) :
        setattr(token, name, number)