import re
list = []
n = int(input())
for i in range(n):
    info = str(input()).split(" ")
    name = info[0]
    email = info[1]
    if re.search(".+@gmail\.com$", email):
        list.append(name)
list.sort()
for name in list:
    print(name)