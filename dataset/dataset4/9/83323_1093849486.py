class Bla:
    resource = logging.resource.Resource(
        type="cloud_run_revision",
        labels={},
    )

    def _to_dict(self):
        return self.resource._to_dict()