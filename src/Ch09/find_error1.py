# 코드 9-2 : try-except 문을 사용한 예외처리와 예외의 종류를 출력하기

try:
    b = 2 / 0
    a = 1 + 'hundred'
except Exception as e:
    print('error :', e)
