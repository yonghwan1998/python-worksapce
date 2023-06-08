print("waiting : 1")
print("waiting : 2")
print("waiting : 3")

print("================================================")

for waiting_no in [0, 1, 2, 3, 4]:
    print(f"waiting : {waiting_no}")

print("================================================")

for waiting_no in range(5):
    print(f"waiting : {waiting_no}")

print("================================================")

for waiting_no in range(1, 6):
    print(f"waiting : {waiting_no}")

print("================================================")

people = ["iron", "ttw", "tree"]

for customer in people:
    print(f"{customer}, coffee")

print("================================================")

students = [1, 2, 3, 4, 5]
print(students)

students = [i + 100 for i in students]
print(students)

students = ["Iron Man", "Thor", "I am Groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron Man", "Thor", "I am Groot"]
students = [i.upper() for i in students]
print(students)
