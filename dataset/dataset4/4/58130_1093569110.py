all_args = [target.bin_path] + args.args
os.execv(target.bin_path, all_args)