def encode_7or8bit(msg):
    """Set the Content-Transfer-Encoding header to 7bit or 8bit."""
    orig = msg.get_payload(decode=True)
    if orig is None:
        # There's no payload.  For backwards compatibility we use 7bit
        msg['Content-Transfer-Encoding'] = '7bit'
        return
    # We play a trick to make this go fast.  If encoding/decode to ASCII
    # succeeds, we know the data must be 7bit, otherwise treat it as 8bit.
    try:
        if isinstance(orig, str):
            orig.encode('ascii')
        else:
            orig.decode('ascii')
    except UnicodeError:
        charset = msg.get_charset()