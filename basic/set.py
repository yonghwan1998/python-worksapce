my_set = {1, 2, 3, 3, 3}

print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)
print(java.intersection(python))

print("================================================")

print(java | python)
print(java.union(python))

print("================================================")

print(java - python)
print(java.difference(python))

print("================================================")

python.add("김태호")
print(python)

print("================================================")

java.remove("김태호")
print(java)
