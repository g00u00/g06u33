import json
parameters_dictionary = {'x':1, 'y':2}
print(parameters_dictionary) 
element = "json_file"
json_str = json.dumps(parameters_dictionary)
print(json_str)
with open("../tmp/"+element+".json", "a", encoding="utf-8") as write_file:
    write_file.write(json_str)
    write_file.write("\n")

read_file = open ("../tmp/"+element+".json", mode='r', encoding="utf-8")
for line in read_file.readlines():
    data_dict = json.loads(line)
    print(data_dict) 
read_file.close()    