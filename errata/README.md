# "으뜸 파이썬" 정오표
## *책 내용에 있는 오류를 정리한 페이지 입니다. 불편을 끼쳐드려 대단히 죄송합니다. 다음 인쇄 때 수정하여 반영하겠습니다.*

---
## 페이지 : 109
### 오탈자 : 제일 마지막줄 실행결과 
<pre>
90도 회전한 후 : (-0.1339745962155614+2.232050807568877j)
</pre>
수정 후
<pre>
30도 회전한 후 : (-0.1339745962155614+2.232050807568877j)
</pre>

## 페이지 : 126
### 오탈자 : 코드 3-7
<pre>
if (number % 3) == 0 and (number % 3) == 0:
</pre>
수정 후
<pre>
if (number % 3) == 0 and (number % 5) == 0:
</pre>

## 페이지 : 238
### 내용오류 : 실행결과
<pre>
Enter your name : Hong GilDong 
Hello Hong GilDong !
</pre>
* 다음과 같이 이름을 입력하는 부분이 줄바꿈 아래에 나타남
<pre>
Enter your name : 
Hong GilDong 
Hello Hong GilDong !
</pre>

## 페이지 : 278
### 오탈자 : 대화창 실습의 주석
<pre>
>>> n_list[1]    # 리스트의 두 번째 항목의 인덱스는 0이다. 
</pre>
* 수정내용 : 주석문을 다음과 같이 수정
<pre>
>>> n_list[1]    # 리스트의 두 번째 항목의 인덱스는 1이다. 
</pre>

## 페이지 : 279
### 대화창 실습
<pre>
>>> n_list = [11, 22, 33, 44, 55, 66]>>> n_list[-1]    # 리스트의 마지막 요소 값 
</pre>
* 수정내용 : 66]과 >>> 사이에 줄바꿈이 있습니다
<pre>
>>> n_list = [11, 22, 33, 44, 55, 66]
>>> n_list[-1]    # 리스트의 마지막 요소 값 
</pre>

## 페이지 : 307
### [그림 5-14]의 화살표 오류
<p align="center">
  <img src="../github-image/errata-fig-error.JPG" width=450px>
  <p> 화살표의 위치에서 발생한 오류
</p>
* 수정내용 : 아래 그림과 같이 수정
<p align="center">
  <img src="../github-image/errata-fig-fixed.JPG" width=460px>
  <p> 화살표의 위치를 수정한 내용
</p>
