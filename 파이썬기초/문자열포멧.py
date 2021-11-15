#f - string

name = '홍길동'
age = 20
print(f'안녕하세요 {name}님 나이가 {age}살 이군요')

# 문자열.format()
welcome = '환영합니다.'
number = 20
base = '{}번 손님 {}'
# 첫번쨰 중괄호에는 첫번쨰 변수(num) 두번쨰 중괄호 (welcome) 두번째 변수가 들어가게 된다.
print('{}번손님{}'.format(number, welcome))

name = '허윤영'
color = 'skyblue'

print(f'{name} 님은 {color} 컬러를 좋아하는 사람입니다.')
print('{} 님은 {} 컬러를 좋아하는 사람입니다.'.format(name, color))


# 문자열 인덱스 : 문자열은 인덱스 번호를 사용가능

string1 = 'abcdefg'
print(string1[2])
print(string1[1:5])
print(string1[3:])
print(string1[:3])
print(string1[:])
#슬라이싱[시작인덱스:끝인덱스] [시작:끝:증감]
print(string1[::-1])

# 인덱스 번호로 값을 가저오는 것을 가능하지만 수정은 불가 하다. 문자열은 생성되면 불변한다.
