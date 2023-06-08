customer = "Me"
index = 5
while index >= 1:
    print(f"{customer}, coffee. {index} remain")
    index -= 1
    if index == 0:
        print("coffee no")

print("================================================")

customer = "You"
index = 1
while True:
    print(f"{customer}, coffee. {index} count")
    index += 1
    if index > 30:
        break

print("================================================")

customer = "You"
person = "Unknown"

while person != customer:
    print(f"{customer}, coffee prepared")
    person = input("Name? ")

print("================================================")

absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"end , {student}")
        break
    print(f"{student}, read book")
