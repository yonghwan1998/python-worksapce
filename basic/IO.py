print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

print("================================================")
import sys

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

print("================================================")

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

print("================================================")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

print("================================================")

# answer = input("아무 값이나 입력하세요. : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

print("================================================")

print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

print("{0:_<+10}".format(500))

print("{0:,}".format(1000000000))
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

print("{0:^<+30,}".format(100000000000))

print("{0:f}".format(5 / 3))
print("{0:.2f}".format(5 / 3))

print("================================================")

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

print()

print("================================================")

import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

print("================================================")

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("Studying file")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
