# 코드 2-15 : input() 함수를 통해 사용자의 입력받기
## "으뜸 파이썬", p. 104

name = input('이름을 입력하세요 : ')  # name은 문자열로 입력받음
print('이름 :', name)
age = int(input('나이를 입력하세요 : ')) # age는 문자열로 입력받아 int 형으로 변환
print('10년 후 나이 :', age + 10)   # 따라서 정수 덧셈 연산이 가능
