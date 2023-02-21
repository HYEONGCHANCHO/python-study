import json
demo ={
    "name":"Kim",
    "age":30,
    "city": "Seoul"
}
print(demo['name'])
result =json.dumps(demo)
print(result)
print(type(result))
print(result[:7])