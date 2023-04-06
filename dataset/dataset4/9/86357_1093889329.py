import argparse

adict = {'a': [1,2,3], 'b': 'astring'}

parser = argparse.ArgumentParser()
parser.add_argument('-f', 
    type = lambda x: adict.get(x,x),
    choices = list(adict.values())
    )
parser.add_argument('-g', choices = adict)

args =  parser.parse_args()
print(args)
print(args.f, adict[args.g])