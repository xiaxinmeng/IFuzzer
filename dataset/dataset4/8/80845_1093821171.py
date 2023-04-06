import argparse

def get_args(args=None):
	parser = argparse.ArgumentParser()
	subparser = parser.add_subparsers(dest='context')
	
	sub = subparser.add_parser('subsection', aliases=['s', 'sub', 'subsect'])
	
	return parser.parse_args(args)
	
def my_subsection_function(args):
	print('my subsection was called')
	
def invalid_context(args):
	print('my functon was not called <sadface>')

def main(args=get_args()):	
	return {
		'subsection': my_subsection_function
	}.get(args.context, invalid_context)(args)

if __name__ == "__main__":
	main()