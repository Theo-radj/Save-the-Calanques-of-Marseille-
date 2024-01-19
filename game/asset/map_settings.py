import random


def gener_map():
    map = [[0 for _ in range(20)] for _ in range(20)]
    for x in range (3):
        for i in range(20):
            for j in range(20):
                if map[(i+1)%20][(j+1)%20] == 2 or map[(i+1)%20][j] == 2 or map[i][(j+1)%20] == 2 or map[(i-1)%20][j] ==2 or map[(i-1)%20][(j-1)%20] or map[i][(j-1)%20] ==2:
                    chance = 600
                    print("chanceux")
                else:
                    chance = 992
                    print("malchanceux")
                if random.randint(0,1000) > chance:
                    map[i][j] = 2
    return map

