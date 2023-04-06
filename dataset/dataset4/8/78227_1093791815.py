parent_parser = argparse.ArgumentParser(add_help=False)
main_parser = argparse.ArgumentParser(prog='app_cli')

service_subparsers = main_parser.add_subparsers(title="service",                                        dest="service_command", )

service_parser = service_subparsers.add_parser("-dr", help="sample help", parents=[parent_parser])

service_parser.add_argument("-old_host",help="my old host", dest="oldHost", required=False)

args = main_parser.parse_args()