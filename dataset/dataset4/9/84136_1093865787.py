from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

parser1 = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser1.add_argument('--foo',
                        default='default_value_for_foo', required=False)
# this will not print the default value for foo. I think this is not the  most natural choice, given that the user has asked for ArgumentDefaultsHelpFormatter, but acceptable since the user didn't define help here. 

parser1.add_argument('--bar', help='',
                        default='default_value_for_bar', required=False)
# this will not print the default value for bar. Again, acceptable but I feel not the most natural. 

parser1.add_argument('--baz', help=' ',
                        default='default_value_for_baz', required=False)
# this will print the default value for baz. 


parser1.print_help()


parser2 = ArgumentParser()
parser2.add_argument('--baz', help=' ',
                        default='default_value_for_baz', required=False)

# this will break, which surprises me.
parser2.print_help()