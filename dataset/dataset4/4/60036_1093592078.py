############### begin sample #####################
import os
import argparse

def existing_filename(path):
    if not os.access(path, os.F_OK | os.R_OK):
        raise argparse.ArgumentTypeError("File '%s' does not exist or cannot be read." % path)
    return path

parser = argparse.ArgumentParser(description='Process a file.')
parser.add_argument('file', type=existing_filename, default='/some/weird/default',
                    help='A file to process.')

args = parser.parse_args()
print ("Will process file '%s' ..." % args.file)
############### end sample #####################