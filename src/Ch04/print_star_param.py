# 코드 4-5 : 매개변수를 가진 별표 출력 함수와 인자를 이용한 호출
## "으뜸 파이썬", p. 204

# 별표 출력을 매개변수 n번만큼 반복하는 프로그램
def print_star(n):
    for _ in range(n):
        print('************************')


print_star(4) # 별표 출력을 위해 4라는 인자 값을 준다.
