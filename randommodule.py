# 랜덤 모듈 불러오기

import random
import myModule as my


x = random.randint(0, 1)

if x == 1:
    print("앞면")
else:
    print("뒷면")

# 동전을 던졋을때 랜덤으로 앞 뒷면이 나오도록 코드 작성

# 내가 만든 모듈의 변수 pi를 불러옴
print(my.pi)


names_string = input("점심값 내기를 할 친구들 이름을 적습니다. 콤마로 분리해서 적어주세용 :  ")
name = names_string.split(",")

print(name)
print(len(name))

ran = random.randint(0, len(name))

print(f"오늘 커피는 {name[ran]} 쏜다")
