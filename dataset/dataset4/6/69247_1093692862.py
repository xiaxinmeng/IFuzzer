def enumtype(astring):
    try:
        return CustomEnumType[astring.upper()]
    except KeyError:
        msg = ', '.join([t.name.lower() for t in CustomEnumType])
        msg = 'CustomEnumType: use one of {%s}'%msg
        raise argparse.ArgumentTypeError(msg)