menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

print("================================================")

# Quiz.4

from random import *

lst = []

for i in range(1, 21):
    lst.append(i)

print(lst)
shuffle(lst)
print(lst)

chicken = lst.pop()
coffee = sample(lst, 3)

print(f"chicken : {chicken}")
print(f"coffee : {coffee}")
