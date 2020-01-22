import random
def cal():
    x=random.randint(0,9)
    y=random.randint(0,9)
    print(x,"더하기",y,"는? 종료는 -1")
    z= int(input())
    input_num(x,y,z)

def input_num(x,y,z):
    if z==-1:
        print("종료")
        exit()
    else:
        if z==x+y:
            print("천재 시네요")
        else:
            print("바보시네요")
    cal()

try:
    cal()
except ValueError:
    print("븅신이냐")
    exit()