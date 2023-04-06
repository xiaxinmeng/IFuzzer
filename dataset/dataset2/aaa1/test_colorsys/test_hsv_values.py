import unittest
import colorsys
import test_colorsys

def test_hsv_values():
    values = [((0.0, 0.0, 0.0), (0, 0.0, 0.0)), ((0.0, 0.0, 1.0), (4.0 / 6.0, 1.0, 1.0)), ((0.0, 1.0, 0.0), (2.0 / 6.0, 1.0, 1.0)), ((0.0, 1.0, 1.0), (3.0 / 6.0, 1.0, 1.0)), ((1.0, 0.0, 0.0), (0, 1.0, 1.0)), ((1.0, 0.0, 1.0), (5.0 / 6.0, 1.0, 1.0)), ((1.0, 1.0, 0.0), (1.0 / 6.0, 1.0, 1.0)), ((1.0, 1.0, 1.0), (0, 0.0, 1.0)), ((0.5, 0.5, 0.5), (0, 0.0, 0.5))]
    for (rgb, hsv) in values:
        ColorsysTest.assertTripleEqual(hsv, colorsys.rgb_to_hsv(*rgb))
        ColorsysTest.assertTripleEqual(rgb, colorsys.hsv_to_rgb(*hsv))

ColorsysTest = test_colorsys.ColorsysTest()
test_hsv_values()
