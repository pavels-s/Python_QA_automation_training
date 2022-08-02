import json

newDictionary = '{"Key1":"val1", "Key2":"Val2"}'
json_result = json.loads(newDictionary)

print(json_result)
