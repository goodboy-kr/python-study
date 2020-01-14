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
list는 [] 괄호 안에 쓰고 첫번째 리스트 값을 0번 오프셋 이라고 한다.
1.오프셋으로 슬라이싱을 나타낼 수 있다.
  처음이 0번 오프셋, 마지막이 -1번 오프셋
  squares= [1, 4, 16, 25, 36, 49]
  squares[1:3]= 4, 16

2.letters['a', 'b', 'c', 'd', 'e', 'f', 'g']
  letters[2:5] =[]    ->letters의 2~4번 오프셋을 빈공간으로 만듬
  >>>letters=[a, b, f, g]
  letters[:]=[]       ->letters를 빈공간으로 만듬
  >>>letters=[]

3.list.append() 는 리스트의 끝에 함수를 추가한다.
  letters.append(x)
  >>>letters=[a, b, c, d, e, f, g, x]

4.list(str) 문자열을 리스트로 바꾼다.
  print(list('cat'))	-> ['c', 'a', 't']  문자열을 리스트로 바꾼후 출력한다.

5.str.split('') split할 문자열을 기준으로 리스트로 변환한다.
  birthday = '1/6/1952' 문자열을 리스트로 바꾸는 함수
  birthday.split('/')	->['1', '6', '1952']	(문자열을 리스트로 만듬)

6.리스트안에 리스트를 넣을수 있고 이중배열 처럼 나타낼 수 있다.
  a= ['x', 'y', 'z']
  b= [1, 2, 3]
  c=[a, b]
  c[0][2]= 'z'

출력
-------------
1.a, b =1, 3처럼 미지수 2개가 입력 가능
end 를 사용해서 출력끝에 쓴다. 
while a < 1000:
     print(a, end=',')
     a, b = b, a+b
     
     
2.변수를 출력하고 싶을때
name = 'Song'
sex = 'male'
print(f'이름은 {name}이고 성별은 {sex}입니다.')
>>>이름은 Song이고 성별은 male입니다.

  +)큰 따옴표 안에 작은 따옴표를 쓰는것을 이용해서 띄어쓰기나 이상한 문자를 넣을 수도 있다!!
  백준 https://www.acmicpc.net/problem/12606
  T = int(input())
  for i in range(1, T+1):
      ss = input().split()
      print(f'Case #{i}: {" ".join(reversed(ss))}')
