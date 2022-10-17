import json

def write(dictionary):
    with open("users.txt","w") as f:
        f.writelines(json.dumps(dictionary))

def read(file):
    file = open(file,"r")
    return json.loads(file.read())





users = read("users.txt")

users["anka"] = 'ko'

write(users)

print(read("users.txt"))

users = {"david":"apa"}