Second Class
=============
if, for, range, break, continue, else
=============
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
words = ['cat', 'window', 'defenestrate']
for x in words:
  print(x, len(w))
>>>cat 3
window 6
defenestrate 12

파이썬에서 for 은 범위를 전부 순회할때까지 실행한다는 의미가 있다.

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




