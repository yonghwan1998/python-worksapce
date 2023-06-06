sentence1 = "나는 소년입니다."
print(sentence1)

sentence2 = "나는 소녀입니다."
print(sentence2)

sentence3 = """
나는 소년이고, 
쟤는 소녀에요"""
print(sentence3)

print("================================================")

number = "990101-1234567"
print("sex : " + number[7])
print("year : " + number[0:2])
print("month : " + number[2:4])
print("day : " + number[4:6])

print("front : " + number[:6])
print("back : " + number[7:])

print("reverse back : " + number[-7:])

print("================================================")

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
# print(python.index("Java"))
print(python.find("Java"))

print(python.count("n"))

print("================================================")

print("a" + "b")
print("a", "b")

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요" % "A")

print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("================================================")

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("================================================")

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

print("================================================")

age = 20
color = "빨간"

print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("================================================")

print("백문이 불여일견\n백견이 불여일타")
print("저는 'Bang' 입니다.")
print('저는 "Bang" 입니다.')
# print("저는 \"Bang\" 입니다.")

print("C:\Python\python-worksapce")
print("C:\\Python\\python-worksapce")

print("Red Apple\rPine")

print("Redd\b Apple")

print("Red\tApple")

print("================================================")

# Quiz.3

url = "https://naver.com"
str = url.replace("https://", "")

str = str[: str.index(".")]

result1 = str[:3]

result2 = len(str)

result3 = str.count("e")

result4 = "!"

print(f"생성된 비밀번호 : {result1}{result2}{result3}{result4}")
