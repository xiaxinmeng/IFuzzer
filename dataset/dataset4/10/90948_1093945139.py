import sys
import os
import ruamel.yaml

yaml = ruamel.yaml.YAML()
input_file = sys.argv[1]
output_yaml =  r"data_output.yaml"
output = open(output_yaml, 'w+')
with open(input_file, 'r') as f:
    data = yaml.load(f)
    ruamel.yaml.round_trip_dump(data, output)    