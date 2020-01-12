스플릿, 조인, 문자열 다루기
=============
스플릿
-------------
1) 빈공간
letters = 'abcd efghijkl mnopqrst uvwxyz' 에서
print(letters.split()) -> ['abcd', 'efghijkl', 'mnopqrst', 'uvwxyz'] (split 뒤에 아무것도 설정안하면 빈공간을 기준으로 스플릿함)

2) 특정문자
letters = 'abcd,efghijkl,mnopqrst,uvwxyz' 에서
letters_split= letters.split(',') ->['abcd', 'efghijkl', 'mnopqrst', 'uvwxyz'] (,를 기준으로 분해)

+ type(letters_split) = <class 'list'>
+ len(letters_split) = 4

조인
-------------
letters = 'abcd,efghijkl,mnopqrst,uvwxyz'	: letters는 콤마가있는 문자열(str)
letters_split = letters.split(',')			: letters_split(',')는 콤마로 만든 리스트(list)
letters_join= ' and '.join(letters_split) 		: letters_join은 letters_split를 ' and '로  합친 문자열

print(letters)		->abcd,efghijkl,mnopqrst,uvwxyz
print(letters_split)		->['abcd', 'efghijkl', 'mnopqrst', 'uvwxyz'] (리스트의 출력형태) 
print(letters_join)		->abcd and efghijkl and mnopqrst and uvwxyz (분해된 리스트사이에 and가 생기고 이어붙는 문자열)

문자열 다루기
-------------
1)길이
len(letters)		->29	(공백과 콤마를 합한 문자열의 길이)
len(letters_split)		->4	(리스트안의 개수)
len(letters_join)		->41	(합쳐진 문자열의 길이-공백포함)

2)문자 검색 관련 함수
letters.startswith('a')	->True	(첫 문자가 a인가?)
letters.endswith('z')		->True	(마지막 문자가 z인가?)
letters.find('k')		->11	(첫번째로 나오는 k가 나오는게 몇번째 인가?- 오프셋)
letters.rfind('k')		->11	(뒤에서 첫번째로 나오는 k가 몇번째인가?- 오프셋)
letters.count(',')		->3	(콤마가 몇번나오는가?)
letters.isalnum()		->False	(letters가 숫자로만 이루어 졌는가?)
letters.isalpha()		->False	(letters가 문자로만 이루어 졌는가?)

3)문자 변환
letters.strip(',')		->양끝에서 콤마시퀀스를 삭제
letters.capitalize()		->Abcd,efghijkl,mnopqrst,uvwxyz	(첫번째 단어 대문자로 변경)
letters.title()		->Abcd,Efghijkl,Mnopqrst,Uvwxyz	(모든 단어의 첫번째 글자 대문자로 변경) - 콤마나 공백을 기준으로 단어구별
letters.upper()		->ABCD,EFGHIJKL,MNOPQRST,UVWXYZ(모든 문자 대문자로 변경)
letters.lower()		->abcd,efghijkl,mnopqrst,uvwxyz	(모든 문자 소문자로 변경)
letters.swapcase()		->aBCD,EfGHIJKL,MNOPQRST,UVWXYZ	(대문자는 소문자로 소문자는 대문자로)
letters.center(40)		->   xxabcd,efghijkl,mnopqrst,uvwxyzxx    (40칸에서 중간에 문자열 배치)
letters.ljust(40)		->xxabcd,efghijkl,mnopqrst,uvwxyzxx       (40칸에서 왼쪽에 문자열 배치)
letters.rjust(40)		->       xxabcd,efghijkl,mnopqrst,uvwxyzxx(40칸에서 오른쪽에 문자열 배치)
letters.reaplace('x', '4')	->44abcd,efghijkl,mnopqrst,uvw4yz44	(앞의 문자를 뒤의 문자로 변환)
letters.reaplace('x', '4', 3)	->44abcd,efghijkl,mnopqrst,uvw4yzxx	(replace를 3회 실행)
