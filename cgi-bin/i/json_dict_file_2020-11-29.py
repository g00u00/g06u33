import json
dict_t = {"010_name": "Фактор1", "020_значимость": 34,  "030_вероятность": 25,}
print(dict_t)
data = json.dumps(dict_t, ensure_ascii=False, sort_keys=True)
print(type(data))
print(data)

with open("./json_file.json", "a", encoding="utf-8") as write_file:
    write_file.write(data)
    write_file.write("\n")

names=list()

with open("./json_file.json", mode='r', encoding="utf-8") as read_file:
    print("")
    for line in read_file.readlines():
        print("")
        print(line, end="")
        data = json.loads(line)
        print(type(data))
        print(data)
        for item in sorted(data):
            print(item, data[item], sep=":", end=", ")
        print() 
        #print("data['010_name']: ", data['010_name']) 
