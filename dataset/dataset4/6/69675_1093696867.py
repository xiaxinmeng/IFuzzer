def handler(loop, context):
    print('Got error, exiting')
    loop.call_soon(sys.exit, 42)