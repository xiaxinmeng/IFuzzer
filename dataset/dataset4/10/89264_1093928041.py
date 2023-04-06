def exit_with_usage(code=1):
    print("Usage: {0} [{1}]".format(
        sys.argv[0], '|'.join('--'+opt for opt in valid_opts)), file=sys.stderr)
    sys.exit(code)