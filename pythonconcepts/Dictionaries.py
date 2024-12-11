info = {'name': 'Roshni', 'age': 18, 'eligible': True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")