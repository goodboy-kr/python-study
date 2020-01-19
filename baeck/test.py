# f = open('Graph_4963.txt', 'r')

save_result = []


def func():
    while True:
        check_point = [(-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (1, -1), (-1, 1)]
        point_graph = []
        # width, height = list(map(int, f.readline().strip('\n').split(' '))) 
        width, height = list(map(int, input().split(' ')))
        map_link = []

        if (width == 0 and height == 0):
            return

        # 1이 들어간 좌표 추가
        for i_height in range(height):
            # map_data = list(map(int, f.readline().strip('\n').split(' ')))
            map_data = list(map(int, input().split(' ')))
            for i_width in range(width):
                if map_data[i_width] == 1:
                    point_graph.append((i_height, i_width))

        # 1이 들어간 좌표들이 연결되있는지 append
        for point in point_graph:
            x, y = point
            is_in = False
            if len(map_link) == 0:
                map_link.append(set([(x, y)]))
                continue

            for idx, link in enumerate(map_link.copy()):
                for c_x, c_y in check_point:
                    if (x + c_x, y + c_y) in list(link):
                        map_link[idx].add((x, y))
                        is_in = True

            if is_in == False:
                map_link.append(set([(x, y)]))

        current = 0
        if len(map_link) == 0:
            save_result.append('0')
        else:
            # 합집합
            while current < len(map_link):
                for idx, item in enumerate(map_link.copy()):
                    if idx != current and map_link[current] & item:
                        map_link[current] = map_link[current].union(item)
                        map_link.pop(idx)
                        break

                current = current + 1

            # print('-'*10, width,height,'-'*10)
            # for links in map_link:
            #     print(links)
            save_result.append(str(len(map_link)))


func()

for i in range(len(save_result)):
    print(save_result[i])
