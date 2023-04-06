
def test_get_clock_info(self):
        clocks = ['monotonic', 'perf_counter', 'process_time', 'time']

        for name in clocks:
            info = time.get_clock_info(name)

            #self.assertIsInstance(info, dict)
            self.assertIsInstance(info.implementation, str)
            self.assertNotEqual(info.implementation, '')
            self.assertIsInstance(info.monotonic, bool)
            self.assertIsInstance(info.resolution, float)
            # 0.0 < resolution <= 1.0
            self.assertGreater(info.resolution, 0.0)
            self.assertLessEqual(info.resolution, 1.0)
            self.assertIsInstance(info.adjustable, bool)
