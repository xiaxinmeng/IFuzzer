import unittest
import colorsys
import test_colorsys

def test_yiq_values():
    values = [((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), ((0.0, 0.0, 1.0), (0.11, -0.3217, 0.3121)), ((0.0, 1.0, 0.0), (0.59, -0.2773, -0.5251)), ((0.0, 1.0, 1.0), (0.7, -0.599, -0.213)), ((1.0, 0.0, 0.0), (0.3, 0.599, 0.213)), ((1.0, 0.0, 1.0), (0.41, 0.2773, 0.5251)), ((1.0, 1.0, 0.0), (0.89, 0.3217, -0.3121)), ((1.0, 1.0, 1.0), (1.0, 0.0, 0.0)), ((0.5, 0.5, 0.5), (0.5, 0.0, 0.0))]
    for (rgb, yiq) in values:
        ColorsysTest.assertTripleEqual(yiq, colorsys.rgb_to_yiq(*rgb))
        ColorsysTest.assertTripleEqual(rgb, colorsys.yiq_to_rgb(*yiq))

ColorsysTest = test_colorsys.ColorsysTest()
test_yiq_values()
