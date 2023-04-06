# run clean or build libraries if they don't exist
if 'clean' in sys.argv:
    try:
        os.remove(os.path.join(LIB_DIR, SOLPOSAM_LIB_FILE))
        os.remove(os.path.join(LIB_DIR, SPECTRL2_LIB_FILE))
    except OSError as err:
        sys.stderr.write('%s\n' % err)