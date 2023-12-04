print("Hello")
user_list = []
key_list = []
created_list = []

with open("users.txt", "r") as file:
    for line in file:
        line = line.split(", ")
        user = {}
        user["name"] = line[0]
        user["age"] = int(line[1])
        user["lastname"] = line[2].strip("\n")
        user_list.append(user)

# for i in range(1, 4):
#     user = {}
#     user["name"] = input(f"Please, enter the name {i}: ")
#     user["age"] = int(input(f"Please, enter the age{i}: "))
#     user["lastname"] = input(f"Please, enter the lastname{i}: ")
#     user_list.append(user)

for k in range(1, 3):
    key = input(f"Please, enter the key {k}: ")
    key_list.append(key)

res = [user_list[0]]

for user in user_list:
    if (user[key_list[0]] != res[0][key_list[0]]) or (user[key_list[1]] != res[0][key_list[1]]):
        res.append(user)

with open("result.txt", "w") as file_w:
    file_w.write(str(res))

print(res)





