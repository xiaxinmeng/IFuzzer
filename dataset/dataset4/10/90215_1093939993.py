def register_db_args(parser: argparse.ArgumentParser):
    grp = parser.add_argument_group('Database settings')
    grp.add_argument('--db-config', dest='db_config_file',
                     help='Config file containg all details including password')

    grp.add_argument('--db-host')
    grp.add_argument('--db-port')
    grp.add_argument('--db-user')

    xgrp = grp.add_argument_group()
    xgrp.add_argument('--db-password')
    xgrp.add_argument('--db-password-env')
    xgrp.add_argument('--db-password-file')