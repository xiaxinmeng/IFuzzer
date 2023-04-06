# test nan
for time_rnd, _ in ROUNDING_MODES:
    with self.assertRaises(ValueError):
        pytime_converter(float('nan'), time_rnd)