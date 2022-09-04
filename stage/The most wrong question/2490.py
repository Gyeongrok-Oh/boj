_= 0
while _< 3:
    yut_play = list(map(int, input().split()))

    if yut_play.count(0) == 1:
        print('A')

    elif yut_play.count(0) == 2:
        print('B')

    elif yut_play.count(0) == 3:
        print('C')

    elif yut_play.count(0) == 4:
        print('D')

    elif yut_play.count(1) == 4:
        print('E')
    _+= 1