def update_conf(conf_path):
    old = open(conf_path)
    tmp = tempfile.NamedTemporaryFile(prefix =
os.basename(conf_path), \
        dir = os.dirname(conf_path), delete = False)
    for l in old:
        tmp.write(l.replace('war', 'peace'))
    close(old)
    close(tmp)
    os.link(conf_path, conf_path + ".old")
    os.rename(tmp.name, conf_path)