# # Quiz.1

# station = "사당"
# print(station + " 행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station + " 행 열차가 들어오고 있습니다.")

# station = "인천공항"
# print(station + " 행 열차가 들어오고 있습니다.")

# print("================================================")

# # Quiz.2
# from random import *

# day = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")

# print("================================================")

# # Quiz.3

# url = "https://naver.com"
# str = url.replace("https://", "")

# str = str[: str.index(".")]

# result1 = str[:3]

# result2 = len(str)

# result3 = str.count("e")

# result4 = "!"

# print(f"생성된 비밀번호 : {result1}{result2}{result3}{result4}")

# print("================================================")

# # Quiz.4

# from random import *

# lst = []

# for i in range(1, 21):
#     lst.append(i)

# print(lst)
# shuffle(lst)
# print(lst)

# chicken = lst.pop()
# coffee = sample(lst, 3)

# print(f"chicken : {chicken}")
# print(f"coffee : {coffee}")

# print("================================================")

# # Quiz.5

# from random import *

# sumTime = 0
# count = 0

# for personCount in range(50):
#     driveTime = randint(5, 50)

#     if 5 <= driveTime <= 15:
#         sumTime += driveTime
#         if sumTime > 50:
#             sumTime -= driveTime
#             print(f"[ ] {personCount+1}번째 손님 (소요시간 : {driveTime}분)")
#         else:
#             count += 1
#             print(f"[O] {personCount+1}번째 손님 (소요시간 : {driveTime}분)")
#     else:
#         print(f"[ ] {personCount+1}번째 손님 (소요시간 : {driveTime}분)")

# print(f"총 탑승 승객 : {count} 명")

# print("================================================")

# Quiz.6

# def standardWeigt(height, gender):
#     while True:
#         if gender == "male":
#             BMI = int(int(height) * int(height) * 22 * 0.01) / 100
#             print(f"키 {height}cm 남자의 표준 체중은 {BMI}kg 입니다.")
#             break
#         elif gender == "female":
#             BMI = int(int(height) * int(height) * 22 * 0.01) / 100
#             print(f"키 {height}cm 여자의 표준 체중은 {BMI}kg 입니다.")
#             break
#         else:
#             gender = input("남자 : male, 여자 : female 값만 입력해주세요. ")


# inputHeight = input("키를 입력해주세요. >> ")
# inputGender = input("남자 : male, 여자 : female 값을 입력해주세요. >> ")

# standardWeigt(inputHeight, inputGender)

# print("================================================")

# Quiz.7

# for i in range(1, 51):
#     with open(f"{i}주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(f" - {i}주차 주간보고 -")
#         report_file.write(f"\n부서 : ")
#         report_file.write(f"\n이름 : ")
#         report_file.write(f"\n업무 요약 : ")

# print("================================================")

# Quiz.8


# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print(
#             self.location,
#             self.house_type,
#             self.deal_type,
#             self.price,
#             self.completion_year,
#         )


# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses = []
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print(f"총 {len(houses)}대의 매물이 있습니다.")

# for house in houses:
#     house.show_detail()

# print("================================================")


# Quiz.9
class SoldOutError(Exception):
    def __str__(self):
        msg = "재고가 소진되어 더이상 주문을 받지 않습니다."
        return msg


chicken = 10
waiting = 1
while True:
    try:
        print(f"[남은 치킨 : {chicken}]")
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order < 1 or (not isinstance(order, int)):
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print(f"[대기번호 {waiting}] {order}마리 주문이 완료됐습니다.")
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldOutError as err:
        print(err)
        break
