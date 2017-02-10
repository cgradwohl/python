def displayPathtoPrincess(n,grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 'm':
                marioY = i
                marioX = j
            if grid[i][j] == 'p':
                princessY = i
                princessX = j


    actions = []

    xDist = abs(marioX - princessX)
    while xDist>0:
        if marioX - princessX > 0:
            marioX = marioX - 1
            actions.append('LEFT')
            xDist = abs(marioX - princessX)
        else:
            marioX = marioX + 1
            actions.append('RIGHT')
            xDist = abs(marioX - princessX)

    yDist = abs(marioY - princessY)
    while yDist>0:
        if marioY - princessY > 0:
            marioY = marioY - 1
            actions.append('UP')
            yDist = abs(marioY - princessY)

        else:
            marioY = marioY + 1
            actions.append('DOWN')
            yDist = abs(marioY - princessY)

    for a in actions:
        print a


m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())




displayPathtoPrincess(m,grid)
