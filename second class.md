Second Class
=============
if, for, range, break, continue, else
=============
자료형
-------------
a = ['a', 'b', '3']

b = {'a', 'b', 'c'}

c = ('a', 'b', 'c')

d = {'a' : 'b', 'c': 'd', 'e': 'f'}

print('a는',type(a))

print('b는',type(b))

print('c는',type(c))

print('d는',type(d))

a는 <class 'list'>

b는 <class 'set'>

c는 <class 'tuple'>

d는 <class 'dict'>

if문
-------------
x=int(input("숫자 입력 : "))
if x>0:
    print('x는 0보다 큽니다.')
elif x==0 :
    print('x는 0 입니다.')
else:
    print('x는 0보다 작습니다.')

for 문
-------------
1) 기본 출력
words = ['cat', 'window', 'defenestrate']
for x in words:
  print(x, len(w))
>>>cat 3
window 6
defenestrate 12
2) for 의미
파이썬에서 for 은 범위를 전부 순회할때까지 실행한다는 의미가 있다.
3) 이터레이터
이터레이터(iterator): 이터레이터는 리스트나 딕셔너리 투플 셋 문자열을 순서대로 꺼내서 처리하는 객체이다.

for element in [1,2,3]:
  print(element)
  
for element in (1,2,3):
  print(element)

for char in "123":
  print(char)

for element in {1,2,3}:
  print(element)
  
전부
1
2
3이 출력된다.

for key in {"a":1,"b":2,"c":3}:
  print(key)
a
b
c 가 출력된다.

4)추가내용
a = [[10, 20], [30, 40], [50, 60]]

for i in a:

    print("i는 ",i)
    
    for j in i:
        print('j는', j, end=' ')
        
    print()
    
출력:
i는  [10, 20]
j는 10 j는 20 
i는  [30, 40]
j는 30 j는 40 
i는  [50, 60]
j는 50 j는 60 

for i,j in a:
    print(i,j)

출력 : 
10 20
30 40
50 60

range
-------------
range(5) = (0,1,2,3,4)      0부터 5전까지 range안에 들어감

range(1,4) = (1,2,3)        끝에거 빼고 1,2,3 이 range안에 들어간다. and 처음에 0말고 -3같은 숫자도 입력가능

range(0, 100, 10) means 0부터 100까지 step은 10으로한다.
range(0, 100, 10) = (0, 10, 20, 30, 40, ...,90)


플러스알파
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

출력:
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]




