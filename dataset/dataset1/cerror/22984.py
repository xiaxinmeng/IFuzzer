import json
import sys
sys.setrecursionlimit(1000000000)
json.dumps(5j, check_circular=False, default=lambda o: [o])
