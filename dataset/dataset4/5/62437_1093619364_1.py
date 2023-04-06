self.assertRaisesRegexp(ValueError, 'invalid literal for.*XYZ\'$',
                        int, 'XYZ')