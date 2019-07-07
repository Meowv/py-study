import json

persons = [
    {
        'username': 'qix',
        'age': 18,
        'country': 'china'
    },
    {
        'username': 'wushuang',
        'age': 20,
        'country': 'china'
    },
    {
        'username': '张三',
        'age': 18,
        'country': 'china'
    }
]

json_str = json.dumps(persons)
print(json_str)

with open('person.json', 'w', encoding='utf-8') as fp:
    # fp.write(json_str)
    json.dump(persons, fp, ensure_ascii=False)