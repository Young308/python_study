# while 반복문

# while True:
#     print(" 무한반복 ")

# count = 0
# while count < 3:
#     print('Try : ', count)
#     count += 1

# name = '  '
# while name != '팽수':
#     name = input('팽수를 입력하세요 : ')
# print("Thank You")


# from types import coroutine


# hit = 0
# while hit < 10:
#     hit + 1
#     if hit % 2 == 0:  # hit가 짝수이면 아래코드는 실행하지 않고 다시 조건으로 돌아간다.
#         continue
#     print(f'나무를 {hit}번 찍었습니다.')
#     if hit == 10:
#         print("나무 넘어갑니다.")


for n in [1, 2, 3]:
    print(n)

# []는 파이썬 리스트 타입 , 반복문 for 는 이 리스트 안의 내용을 반복한다.
for c in '홍길동':  # 문자열의 철자를 반복
    print(c)


# for 반복문과 자주쓰는 함수 range( 시작, 끝) 리턴값은 시작~끝-1

for n in range(3):
    print(n)

# 1~100까지 합은
total = 0
for x in range(1, 101):
    total += x

print(" 1에서 100까지 더한 값 : ", total)

# 구구단 2단을 출력

for i in range(1, 10):
    print()
    for j in range(1, 10):
        # print(f'2 X {i} = {2*i}')

     # 전체 구구단 출력 2중반복문

        print(f'{i} X {j} = {i*j}', end=" ")
