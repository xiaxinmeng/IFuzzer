
import argparse

def main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-p", "--path", metavar="/var/www/html", 
            help="DocumentRoot path")
    group.add_argument("-r", "--reverse", metavar="http)s(://Host:Port",
            help="Reverse proxy address")

    parser.add_argument("--last-args")
    return parser.parse_args()

main()
