 
strange = {"1":"one", 2:"ii"}
json.dumps(strange, sort_keys=True, key=str)
json.dumps(strange, sort_keys=str)
# {"1": "one", 2: "ii"}
