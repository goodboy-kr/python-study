k = int(input())

num_list = list(map(int, input().split()))
new_list = []
last_list=[]


start=0
end=1
sumx=0
sumy=0

for i in range(k):
    if(i<k-1):
        if(num_list[i]*num_list[i+1]>0):
            end+=1
        else:
            sumx = sum(num_list[start:end])
            new_list.append(sumx)
            start=end
            end=start+1

    if(i == k-1):
        sumx= sum(num_list[start:])
        new_list.append(sumx)

if(new_list[0]<0):
    new_list.pop(0)
if(len(new_list)>0 and new_list[-1]<0):
    new_list.pop(-1)


for i in range(1, len(new_list), 2):
    if(new_list[i]+new_list[i-1] >0 and new_list[i+1] +new_list[i]>0):
        sumy=sum(new_list[i-1:i+2])
        new_list.pop(i)
        new_list.pop(i)
        new_list.pop



"""print("new list 입니다. 2번", new_list[:])
print("new list 최대값 입니다. 3번", new_list[-1])"""


if (len(new_list)==0):
    print(max(num_list))
else:
    print(max(new_list))
