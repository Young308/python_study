# 여러개의 변수를 동시에 초기화
a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

# 예제 2~5

p = 10
print(p)

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

d = 12
e = 1.5
f = 'string'


print(type(d))
print(type(e))
print(type(f))

# a = input('a : ')
# b = input('b : ')

# a, b = b, a

# print('a : ' + a)
# print('b : ' + b)


# 긴문자열은 ''' or """(따옴표 3개)
var3 = '''
따옴표 3개는 끝나는 문장까지 모두를 문자열로 처리 한다 
------------------------------------------------
이 안에 뭐가오던지 상관이 없다 

'''
print(var3)

#문자열 + 연산

성 = '홍'
이름 = '길동'
name = 성 + ' ' + 이름
print(name)

# 타입 변화 : str () int () float()
print(type(int(str(100))))

# 예제
str1 = '\It\'s "kind of " sunny \n Have a nice Day!'
print(str1)

str2 = ''' 
다스베이더가 말했다 
"내가 니 애비다!"
그 말을 들은 루크는 '깜짝'놀랐다.
'''

# 1. 밴드 이름 만들기 프로그램 환영합니다
print("밴드 이름 만들기 프로그램에 환영합니다.")

# 2. 유저에가 태어난 도시를 물어봅니다.
city = input('태어난 도시가 어디인가요? \n')
# 3. 유저에게 애완동물의 이름을 물어봅니다.
petname = input('애완동물의 이름은 무엇인가요? \n')
# 4. 도시와 애완동물 이름을 조합하여 밴드이름을 만들어 출력합니다.
print('당신의 밴드 이름은 ? ' + city+' ' + petname)

# 힌트: 문자열에 \n을 붙이면 한줄 뛰웁니다. => 문자열 입력을 받을때 한줄 아래로 커서이동
