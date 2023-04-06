import pathlib

def main():
    pathlib.Path('tmp').touch()
    pathlib.Path('tmp/tmp_sub').mkdir(parents=True)

main()