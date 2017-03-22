# gets the shortest grid path between 2 coordinates on a grid
def path(r1,c1,r2,c2):
    path = []
    xDist = c2-c1
    yDist = r2-r1
    for i in range(max(abs(xDist), abs(yDist))+1):
        square = [c1+(i*sign(xDist)),r1+(i*sign(yDist))]
        path.append(square)
    return path
