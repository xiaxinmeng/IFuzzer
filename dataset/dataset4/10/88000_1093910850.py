import io

with io.StringIO() as output:
    output.write('First line.\n')
    print('Second line.', file=output)

    # Retrieve file contents -- this will be
    # 'First line.\nSecond line.\n'
    contents = output.getvalue()