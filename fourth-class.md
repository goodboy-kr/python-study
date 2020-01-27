fourth class
=============
컴프리헨션
-------------
1)컴프리헨션은 하나 이상의 이터레이터로 파이썬 자료구조를 만드는 방법이다.  
쓰는 방법은 [표현식 for 항목 in 순회가능한 객채 if 조건]이다.  

예시)1~5숫자 리스트를 만들 때 다음과 같은 방법이 있다.  
a.list(range(1,6))  
b.num_list=[number for number in range(1,6)]  

짝수 리스트 만드는 법  
num_list=[number for number in range(1,6) if number%2==0]  
->[2, 4]


2)딕셔너리 컴프리헨션  
word = 'letters'  
letter_count = {x: word.count(x) for x in word}  
->{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

3)셋 컴프리헨션  
a_set = {x for x in range(1,6) if x%3 == 1}
->{1, 4}


None
-------------
1)Nonetype라는 타입이 있다.  
a = None  
print(type(a))-> NoneType  
2)None는 if 문에서 False처럼 처리된다.  
a=None  
if a:  
  print('안녕')  
else:  
  print('바이')  
->바이  

이럴때는 안녕이 출력된다.  
if a is None:  
  print('안녕')  
else:  
  print('바이')  
->안녕  

0, {}, [], set() 등은 None가 아니다.  





