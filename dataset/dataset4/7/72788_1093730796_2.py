class FoldAwareTzInfo(datetime.tzinfo):
    def fromutc(self, dt):
        dt_wall = super(FoldAwareTzInfo, self).fromutc(dt)

        is_fold = self._get_fold_status(dt, dt_wall)