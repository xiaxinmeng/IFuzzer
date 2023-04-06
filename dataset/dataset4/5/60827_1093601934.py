import argparse

p = argparse.ArgumentParser()
p.add_argument('--foo',
               help=u'This is a very long help string.  ex: "--s3\u00A0s3://my.bucket/dir1/dir2"')
p.parse_args()