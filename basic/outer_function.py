# glob

# import glob

# print(glob.glob("*.py"))

# print("================================================")

# os

# import os

# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제했습니다.")
# else:
#     os.mkdir(folder)
#     print(folder, "폴더를 생성했습니다.")

# print(os.listdir())

# print("================================================")

# time

# import time

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# print("================================================")

# datetime

import datetime

print("오늘 날짜는", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)
