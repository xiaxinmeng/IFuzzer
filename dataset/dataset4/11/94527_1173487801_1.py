...
uni = _decode_uXXXX(s, end)
end += 5
if 0xd800 <= uni <= 0xdbff and s[end:end + 2] == '\\u':
    uni2 = _decode_uXXXX(s, end + 1)
    if 0xdc00 <= uni2 <= 0xdfff:
        uni = 0x10000 + (((uni - 0xd800) << 10) | (uni2 - 0xdc00))
        end += 6
...