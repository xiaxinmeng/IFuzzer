cp=ConfigParser.ConfigParser()
cfgfile=os.path.join(curpath,'config.cfg')
cp.readfp(codecs.open(cfgfile, 'r','utf-8-sig'))