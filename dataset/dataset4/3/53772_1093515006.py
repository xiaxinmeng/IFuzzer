optparser=OptionParser()
optparser.add_option("--share-dir",dest="share_dir",default="/usr/share")
options,args=optparser.parse_args()