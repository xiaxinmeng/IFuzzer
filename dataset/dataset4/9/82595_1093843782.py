# Sort nested dictionary by key
# using OrderedDict() + sorted()
from collections import OrderedDict
from operator import getitem
import json

# initializing dictionary
test_dict = {'3' : { 'roll' : 24, 'marks' : 17},
            '2' : {'roll' : 54, 'marks' : 12},
            '1' : { 'roll' : 12, 'marks' : 15}}

# printing original dict
print("The original dictionary : " + str(test_dict))

# using OrderedDict() + sorted()
# Sort nested dictionary by key
res = OrderedDict(sorted(test_dict.items(),
    key = lambda x: getitem(x[1], 'marks')))

print("The sorted dictionary by marks is : " + str(res))
# Output
# The sorted dictionary by marks is : OrderedDict([('2', {'roll': 54, 'marks': 12}), ('1', {'roll': 12, 'marks': 15}), ('3', {'roll': 24, 'marks': 17})])

res1 = json.dumps(res)