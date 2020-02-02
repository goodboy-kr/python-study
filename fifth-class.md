Fifth class
=============

함수
=============

1)함수를 파라미터로
-------------
def add(*args):    add함수선언  
  return sum(args)  


def cal(func, *args):  add함수를 변수로 받는다.  
  print(type(args))  
  return func(*args)  

x=cal(add, 15, 25, 10)  
print(x)  

-><class 'tuple'>  
50  

2)함수안에 함수(내부함수)
-------------
def outer(a,b):  
  def inner(c,d):  
    print('안에 있는거', c+d)  
    return c+d  
  print('밖에 있는 거', a+b)  
  
outer(4,7)  

->밖에 있는 거 11  
