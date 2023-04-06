import unittest
import colorsys
import test_colorsys

def test_hls_values():
    values = [((0.0, 0.0, 0.0), (0, 0.0, 0.0)), ((0.0, 0.0, 1.0), (4.0 / 6.0, 0.5, 1.0)), ((0.0, 1.0, 0.0), (2.0 / 6.0, 0.5, 1.0)), ((0.0, 1.0, 1.0), (3.0 / 6.0, 0.5, 1.0)), ((1.0, 0.0, 0.0), (0, 0.5, 1.0)), ((1.0, 0.0, 1.0), (5.0 / 6.0, 0.5, 1.0)), ((1.0, 1.0, 0.0), (1.0 / 6.0, 0.5, 1.0)), ((1.0, 1.0, 1.0), (0, 1.0, 0.0)), ((0.5, 0.5, 0.5), (0, 0.5, 0.0))]
    for (rgb, hls) in values:
        ColorsysTest.assertTripleEqual(hls, colorsys.rgb_to_hls(*rgb))
        ColorsysTest.assertTripleEqual(rgb, colorsys.hls_to_rgb(*hls))

ColorsysTest = test_colorsys.ColorsysTest()
test_hls_values()
