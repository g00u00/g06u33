import json
dict_t = {"name": "John", "age": 30}
data = json.dumps(dict_t, ensure_ascii=False, sort_keys=True)
print(data)

with open("../tmp/json_file.json", "a") as write_file:
    write_file.write(data)
    write_file.write("\n")

with open("../tmp/json_file.json", mode='r', encoding="utf-8") as read_file:
    for line in read_file.readlines():
        print(line, end="")
        data = json.loads(line)
        print(data)
        for item in sorted(data):
            print(item, data[item], sep=":", end=", ")
        print() 
        print("data['age']: ", data['age']) 
