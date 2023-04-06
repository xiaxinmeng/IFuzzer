parser = argparse.ArgumentParser()
parser.add_argument('src_dir', type=is_valid_dir_path)
parser.add_argument('dest_dir', type=is_valid_dir_path)
args = parser.parse_args()