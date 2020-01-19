world_size = list(map(int, input().split()))
stack = []
world = []
visited = []
count = 0

if sum(world_size[:]) == 0:
    exit()
else:
    for i in range(world_size[0]):
        tempmap = list(map(int, input().split()))
        world.append(tempmap)

def change(L):
    for i in range(len(L)):
        x= L[i][0]
        y= L[i][1]
        world[x][y]=0

def move(x, y):
    try:
        if world[x][y] == 1:
            visited.append([x, y])
            """if x<world_size[0]:"""
            if world[x + 1][y] == 1:
                visited.append([x + 1, y])
            if world[x + 1][y + 1] == 1:
                visited.append([x + 1, y + 1])
            if world[x + 1][y - 1] == 1:
                visited.append([x + 1, y - 1])
            """elif x>world_size[0]:"""
            if world[x - 1][y] == 1:
                visited.append([x - 1, y])
            if world[x - 1][y - 1] == 1:
                visited.append([x - 1, y - 1])
            if world[x - 1][y + 1] == 1:
                visited.append([x - 1, y + 1])
            """"""
            if world[x][y + 1] == 1:
                visited.append([x, y + 1])
            if world[x][y - 1] == 1:
                visited.append([x, y - 1])
            if len(visited)!=0:
                I = visited.pop(0)
                move(I[0], I[1])
            else:
                print("xxxxxxx")
        else:
            print('-------------')
            move(visited.pop(0))
        change(visited)
    except IndexError:
        print("yyyyyyyyyyy")




move(1, 4)
print("1번 실행")

move(2, 3)
print("2번 실행")

print('맵 :',world)
print('방문', visited)