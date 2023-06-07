subway = [10, 20, 30]

print(subway)

print(subway.index(10))

subway.append(40)
print(subway)

subway.insert(1, 55)
print(subway)

subway.pop()
print(subway.pop())

print(subway.count(10))

print("================================================")

num_list = [5, 2, 3, 1, 4]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

print("================================================")

num_list = [5, 2, 3, 1, 4]
mix_list = ["메뚜기", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)


print("================================================")
