import argparse

parser = argparse.ArgumentParser(
    description="Test program",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "--foo",
    help="Use the foo component.",
    action=argparse.BooleanOptionalAction,
    default=True,
)

args = parser.parse_args()