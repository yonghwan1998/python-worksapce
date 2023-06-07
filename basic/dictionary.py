content = {3: "메뚜기", 100: "호랑이"}
print(content[3])
print(content[100])

print(content.get(3))

# print(content[5])
print(content.get(5))
print(content.get(5, "사용 가능"))

print("================================================")

print(3 in content)
print(33 in content)

print("================================================")

content2 = {"A-3": "강아지", "B-100": "고양이"}
print(content2["A-3"])
print(content2["B-100"])

print(content2)
content2["A-3"] = "new dog"
content2["C-20"] = "도마뱀"
print(content2)

print("================================================")

del content2["A-3"]
print(content2)

print("================================================")

print(content2.keys())
print(content2.values())
print(content2.items())

print("================================================")

content2.clear()
print(content2)
