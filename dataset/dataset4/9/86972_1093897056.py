def f():
    x = (
            'PERL_MM_OPT', (
                f'INSTALL-BASE={shlex.quote(venv)} '
                f'wat'
            ),
    )