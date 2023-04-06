class SandboxAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, nargs=0, **kwargs)

    def __call__(self, *args, **kwargs):
        cls.use()