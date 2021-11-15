# if 문 문법
# a, b = 10, 10
# if a > b:
#     print("조건이 참이면 실행")
#     print("실행코드는 뛰어쓰기로 구분")

# # if문의 코드 블록은 뛰어쓰기 된곳까지

# elif a == b:
#     print("a b 가 같다")


# else:  # if문의 조건이 거짓이면 else 가 실행
#     print("if의 조건이 거짓일 때 실행")

# print("End")


# number = int(input("숫자 입력 : \n "))
# if number % 2 == 0:
#     print("짝수입니다")

# else:

#     print("홀수 입니다")

if height > 120:

    print("청룡열차를 탈 수 있습니다.")

    age = int(input("나이를 입력하세요 : \n"))

    if age < 12:
        print("요금은 5000원입니다")
    elif age <= 18:
        print("요금은 7000원 입니다")
    else:
        print("요금은 12000원 입니다.")

else:

    ("죄송하지만 이용할 수 없습니다.")
