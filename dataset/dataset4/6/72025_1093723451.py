import getpass
import grp
import pprint

pprint.pprint(getpass.getuser())
pprint.pprint([(g.gr_gid, g.gr_name) for g in grp.getgrall()])
pprint.pprint([(g.gr_gid, g.gr_name, g.gr_mem) for g in grp.getgrall() if getpass.getuser() in g.gr_mem])