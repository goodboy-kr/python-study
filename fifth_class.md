Fifth_class
=============
위치 인자
-------------  
1)위치인자 설명  
위치에 따른 인자값 불러오는 거 같은데  

def print_function(x, y, z):  
  print('첫번째:', x)  
  print('두번째:', y)  
  print('세번째:', z)  

print_function('안녕', 'ㅎㅎㅎ', '열공하자')  
->첫번째: 안녕
두번째: ㅎㅎㅎ
세번째: 열공하자  

2)위치인자 모으기  
def print_function(x, y, z, *rest):  
  print('첫번째:', x)  
  print('두번째:', y)  
  print('세번째:', z) 
  print('나머지:', rest)
  
print_function('a','b', 'c', 'd', 'e')  
->
첫번째: a  
두번째: b  
세번째: c  
나머지: ('d', 'e')  


키워드 인자  
-------------  
1)키워드 인자 예시1  
def menu(a,b,c):  
  return {'a' : a, 'b' : b, 'c' : c}    
x=menu('안녕', 'ㅎㅎㅎ', '열공하자')
print(x)  
->{'a': '안녕', 'b': 'ㅎㅎㅎ', 'c': '열공하자'}  

2)키워드 인자 예시2  
def menu(a,b,c):  
  return {'a' : a, 'b' : b, 'c' : c}  
x=menu('안녕', b = 'ㅎㅎ', c = '열공하자')  
print(x)  
->{'a': '안녕', 'b': 'ㅎㅎ', 'c': '열공하자'}  

3)키워드 인자 모으기  
'**'을 사용한다. 딕서너리가 들어간다.  
def print_function(**dic):  
  print('key:',dic)  
  
print_function(a = 'a값', b = 'b값', c = 'c값')  
->key: {'a': 'a값', 'b': 'b값', 'c': 'c값'}  



기본 매개 변수값 지정
-------------
함수에서 파라미터를 입력하지 않았을때 기본 파라미터를 설정 할 수 있다.  
def print_function(x, result = []):  
  print("첫번재 파라미터입니다.", x)  
  print("두번째 파라미터 입니다.", result)  

print_function('abc')  
print_function('efg', ['x','y','z'])  




