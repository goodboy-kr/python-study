#first class 01/12
=============
숫자연산, 문자열, 리스트
=============
##숫자 연산
-------------
1. '+'
  flaot + int = flaot
  
2. '-'

3. '*'

4. '/'
  나눗셈은 항상 float를 반환
  ex)8/2=4.0
  
5. '%'
  모듈러 연산 : 나머지를 출력
  ex)8%3=2
  
6. '`**`'
  거듭제곱 : 제곱연산
  ex)2**4= 16
  
7. '//'
  소수부분 버리고 정수 나눗셈
  ex)15.5//3=5.0


##문자열
-------------
1. r사용법
  print("c : \name")    #\n이 줄바꾸기로 바뀐다.
  >>>c : 
     ame
  print(r "c : \name")  #문자가 그대로 출력 된다.
  >>>c : \name
2. """ string """
  삼중 따옴표는 여러줄을 문자열로 생각한다.
  ex)
  print("""\
  Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
>>>Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
3. 연속된 문자열
  연속된 문자열은 하나로 합쳐진다.
  print('hell' 'o wolrd')
  >>>hello wolrd
  print('hell' 'o world')
  >>>hello wolrd
  print('hell', 'o world')
  >>>hell o wolrd
4. 문자열 슬라이싱 " [ : ] "
  hello world가 들어있는 리스트가 있을때, 어디부터 어디까지 프린트 할지 (-1은 끝의 오프셋)
  print(list[:])
  >>>hello world
  print(list[0:4])
  >>>hel
  print(list[:5])
  >>>hell
  print(list[3:])
  >>>llo world
5.len() 함수는 길이 반환
  str="hello world"
  len(str)
  11      #띄어쓰기 포함
5.A 부터 Z까지 리스트 만들기 
  import string
  print(string.ascii_uppercase[:])

#second class 01/14
=============
리스트
-------------
1.오프셋으로 슬라이싱을 나타낼 수 있다.
  처음이 0번 오프셋, 마지막이 -1번 오프셋
  squares= [1, 4, 16, 25, 36, 49]
  squares[1:3]= 4, 16
2.

3.

4.

5.

6.


