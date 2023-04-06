out.write('%s %s\n' % (m.hexdigest(), filename.encode(
        sys.getfilesystemencoding(),
    ).decode(sys.stdout.encoding)))