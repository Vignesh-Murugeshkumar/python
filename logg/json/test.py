import json
class user:
    def __init__(self,name,age):
        self.name=name  
        self.age=age
user1=user("John",30)
def encode(obj):
    if isinstance(obj,user):
        return {"name":obj.name,"age":obj.age,obj.__class__.__name__:True }
    else:
        raise TypeError("Object of type user is not JSON serializable")

userjson=json.dumps(user1,indent=4, default=encode)
print(userjson)

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,user):
            return {"name":obj.name,"age":obj.age,obj.__class__.__name__:True }
        return JSONEncoder.default(self,obj)
userjson=json.dumps(user1,indent=4,cls=UserEncoder)
print(userjson)

def decode(obj):
    if user.__name__ in obj:
        return user(obj["name"],obj["age"])
    return obj
decodeduser=json.loads(userjson,object_hook=decode)
print(decodeduser.name)