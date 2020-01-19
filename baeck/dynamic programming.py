num = int(input())
count = 0
dynamic = []
dynamic.append(num)

while 1 not in dynamic:
    temparray = []
    count = count + 1
    for num in dynamic.copy():
        if (num % 3 == 0):
            temparray.append(int(num / 3))
        if (num % 2 == 0):
            temparray.append(int(num / 2))
        temparray.append(int(num - 1))
    dynamic = dynamic+temparray
    dynamic = list(set(dynamic))


print(count)