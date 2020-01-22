import sys
sys.setrecursionlimit(10**6)    #재귀함수 깊이 제한 풀어주는 거
world_size = []
world = []
visited = []
count = []
island = []
num=0
x = [1, 1, 1, 0, 0, -1, -1, -1]
y = [1, -1, 0, -1, 1, 1, -1, 0]


def move():
    global num
    if len(island) == 0:
        count.append(num)
        num = 0
        world.clear()
        draw()
    else:
        now = island.pop(0)
        add(now)
        num = num + 1
    move()


def add(where):                 #where는 현재 좌표 입력 [x,y]
    for i in range(8):
        a =where[0]+x[i]
        b =where[1]+y[i]
        if([a, b] in island and [a,b] not in visited):
            island.remove([a, b])
            visited.append([a, b])
    while len(visited)!=0:
        add(visited.pop(0))


def draw():
    world_size=list(map(int, input().split()))
    if sum(world_size[:]) == 0:
        for i in count:
            print(i)
        exit()
    else:
        for i in range(world_size[1]):
            tempmap = list(map(int, input().split()))
            world.append(tempmap)
        for i in range(len(world)):
            for j in range(len(world[0])):
                if world[i][j] == 1:
                    island.append([i, j])
    move()


draw()