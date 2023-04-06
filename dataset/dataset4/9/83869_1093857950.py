GB = 1024**3
buf = b"\xFF" * 1024**2
with open('disk.img', 'wb') as f:
    f.seek(10 * GB)
    wrotten = 0
    while wrotten < 0o77777777777:
        wrotten += f.write(buf)
        f.flush()
        print(wrotten/0o77777777777 * 100, '%')
    f.seek(50 * GB - 1)
    f.write(b'\0')