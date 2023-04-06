import json
import sqlite3

# two unicode strings, the second one has four byte character in it
good_data = "réve illé"
bad_data = "réve🐍 illé"

# create simple json structures
good_data_json = json.dumps({"foo": good_data})
bad_data_json = json.dumps({"foo": bad_data})