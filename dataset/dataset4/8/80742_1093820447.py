parser = argparse.ArgumentParser()
# data
parser.add_argument('--data_type', type=str, default="ml_100k")
args = parser.parse_args()
download_dataset(args.data_type)
preprocess(args.data_type)