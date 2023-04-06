class MyEncoder(json.JSONEncoder):
    def default(self,obj):
        print("hi")
        if isinstance(obj,dict):
            print("it is dict!")
            return obj["name"]
        return json.JSONEncoder.default(self,obj)