# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print(f"{nums[0]} / {nums[1]} = {nums[2]}")
# except ValueError:
#     print("error...")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("Unkwon error...")
#     print(err)

print("================================================")

# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요.")

# print("================================================")


# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg


# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("error... 한자리 숫자만 입력하세요.")
#     print(err)


print("================================================")


class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값 : {num1}, {num2}")
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("error... 한자리 숫자만 입력하세요.")
    print(err)
finally:
    print("thanks")
