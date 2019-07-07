import json

json_str = '[{"username": "qix", "age": 18, "country": "china"}, {"username": "wushuang", "age": 20, "country": "china"}, {"username": "张三", "age": 18, "country": "china"}]'

persons = json.loads(json_str)
for person in persons:
    print(person)

with open('person.json', 'r', encoding='utf-8') as fp:
    persons = json.load(fp)
    for person in persons:
        print(person)