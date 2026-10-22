import json
person={"first_name": "John", "last_name": "Doe", "age": 30, "hobbies": ["reading", "traveling", "swimming"], "hasChildren": True, "children": [{"name": "Jane", "age": 10}, {"name": "Mark", "age": 8}]}


personjson=json.dumps(person,indent=4,separators=(',',': '),sort_keys=True)
print(personjson)

with open('person.json','w') as f:
    json.dump(person,f,indent=4,)
with open('person.json','r') as f:
    personjson=f.read()
    person=json.loads(personjson)
print(person)