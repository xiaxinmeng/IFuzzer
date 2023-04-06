_COLSPEC_RE = re.compile(textwrap.dedent(r'''
    ^
    (?:
        [[]
        (
            (?: [^\s\]] [^\]]* )?
            [^\s\]]
        )  # <label>
        []]
    )?
    ( \w+ )  # <field>
    (?:
        (?:
            :
            ( [<^>] )  # <align>
            ( \d+ )  # <width1>
        )
        |
        (?:
            (?:
                :
                ( \d+ )  # <width2>
            )?
            (?:
                :
                ( .*? )  # <fmt>
            )?
        )
    )?
    $
'''), re.VERBOSE)