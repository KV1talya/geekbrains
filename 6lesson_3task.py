import sys

hobby_file = open("hobby.csv", "r", encoding="utf-8")
users_file = open("users.csv", "r", encoding="utf-8")
result_file = open("result", "w", encoding="utf-8")

result = {}
users = []
hobby = []

for users_list in users_file.read().replace(",", " ").split("\n"):
    users.append(users_list)

for hobby_list in hobby_file.read().split("\n"):
    hobby.append(hobby_list)

if len(users) > len(hobby):
    for index in range(len(users)):
        try:
            result.update({users[index]: hobby[index]})
        except IndexError:
            result.update({users[index]: None})
elif len(users) < len(hobby):
    sys.exit(1)

print(result)
for data in result:
    result_file.write(f"{data}: {result.get(data)}\n")

