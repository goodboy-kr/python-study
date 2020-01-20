world_size = list(map(int, input().split()))
stack = []
world = []
visited = []
count = []
island = []

x = [1, 1, 1, 0, 0, -1, -1, -1]
y = [1, -1, 0, -1, 1, 1, -1, 0]

if sum(world_size[:]) == 0:
    exit()
else:
    for i in range(world_size[1]):
        tempmap = list(map(int, input().split()))
        world.append(tempmap)

for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j] == 1:
            island.append([i, j])


def move(start):                #start는 [x, y] 로 리스트면서 좌표다
    now = island.pop(0)
    add(now)


def add(where):                 #where는 현재 좌표 입력 [x,y]
    num=0
    for i in range(8):
        a =where[0]+x[i]
        b =where[1]+y[i]
        if([a, b] in island and [a,b] not in visited):
            island.remove([a,b])
            visited.append([a, b])
            print('visted입니다.', visited)
            print('island입니다.', island)
    while len(visited)!=0:
        add(visited.pop(0))
    num=num+1
    count.append(num)
    while len(island)!=0:
        move(island.pop(0))

"""            if k==l:
                num+=1
                count.append(num)
                visited.clear()
                move(island.pop())"""
"""add(visited.pop(0))"""



print('아일랜드', island)
move(1)
print(count)