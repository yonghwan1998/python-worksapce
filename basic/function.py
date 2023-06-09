def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


print("================================================")


def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance+money}원입니다.")
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance-money}원입니다.")
        return balance + money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원입니다.")
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
print(balance)
balance = withdraw(balance, 2000)
print(balance)
balance = withdraw(balance, 500)
print(balance)

commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission}원이며, 잔액은 {balance}원입니다.")


print("================================================")


def profile(name, age, main_lang):
    print(f"이름 : {name}\t나이 : {age}\t 주 사용 언어 : {main_lang}")


profile("유재석", 20, "파이썬")
profile("김태호", 20, "자바")


def profile(name, age=17, main_lang="파이썬"):
    print(f"이름 : {name}\t나이 : {age}\t 주 사용 언어 : {main_lang}")


profile("유재석")
profile("김태호")


print("================================================")


def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="파이썬", age=20)
profile(name="김태호", age=25, main_lang="자바")


print("================================================")


def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

print("================================================")


def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")

print("================================================")

gun = 10


def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print(f"[함수 내부] 남은 총 : {gun}")


print(f"[함수 외부] 전체 총 : {gun}")
checkpoint(2)
print(f"[함수 외부] 남은 총 : {gun}")


def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print(f"[함수 내부] 남은 총 : {gun}")


print(f"[함수 외부] 전체 총 : {gun}")
checkpoint(2)
print(f"[함수 외부] 남은 총 : {gun}")

print("================================================")

gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(f"[함수 내부] 남은 총 : {gun}")


print(f"[함수 외부] 전체 총 : {gun}")
checkpoint(2)
print(f"[함수 외부] 남은 총 : {gun}")

print("================================================")

gun = 10


def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수 내부] 남은 총 : {gun}")
    return gun


print(f"[함수 외부] 전체 총 : {gun}")
gun = checkpoint_return(gun, 2)
print(f"[함수 외부] 남은 총 : {gun}")
