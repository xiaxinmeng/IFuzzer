f = open('filename')
f.seek(999999999999)    # ok
f.seek(12.0)            # ok
f.seek(999999999999.0)  # OverflowError