data = """<?xml version="1.0"?>
         <parent id="top"><child1 name="paul">Text goes here</child1>
         <child2 name="fred">More text</child2>
         </parent>"""
findFirstElementByName(data, "child2")   # Found
findFirstElementByName(data, "child3")   # Not found