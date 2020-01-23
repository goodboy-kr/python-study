Third Class
=============
set
=============
1.set의 의미
-------------
셋이란 딕셔너리에서 키값만 존재하는 것과 같다. 따라서 순서는 없고 집합과 같은 형태로 사용 가능하다.

2.set의 변환
-------------
x=set(~~~) or x = {'a', 'b', 'c', ...}  
문자열, 리스트, 딕셔너리, 투플을 set(list)를 통해 셋으로 변경할 수 있다.  
셋에는 중복값이 들어갈 수 없으므로 set('letters')->{'l', 'e', 't', 'r', 's'} 가 된다.  
리스트나 투플 딕셔너리 모두 마찬가지이다.

3.set 활용
-------------
a= {1, 2, 3, 4},
b= {4, 5, 6, 7}  
교집합  
& , intersection  
a&b -> {4}  
a.intersection(b) -> {4}


합집합  
|(엔터 위에 있음), union  
a|b={1,2,3,4,5,6,7}  
a.union(b)={1,2,3,4,5,6,7}  


차집합  
'-' , difference  
a-b -> {1,2,3}  
a.difference(b) -> {1,2,3}  

대칭 차집합(aUb - anb)  
^, symmetric_difference  
a^b -> {1,2,3,5,6,7}  
a.symmetric_difference(b) -> {1,2,3,5,6,7}  

부분집합  
슈퍼셋 : 상위집합 (큰 집합)
서브셋 : 하위집합 (작은 집합) 
프로퍼 슈퍼셋 : 진부분집합

a = {1,2,3}
b = {1,2,3,4,5}  
서브셋  
a<=b -> True  
a.issubset(b) -> True  

프로퍼 서브셋  
a<b -> True  

슈퍼셋  
a>=b -> False  
a.issuperset(b) -> False  

프로퍼 슈퍼셋  
a>b -> False  

