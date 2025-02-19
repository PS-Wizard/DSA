def minTimeToVisitAllPoints(points):
    counter = 0
    x1,y1 = points.pop()
    while points:
        x2,y2 = points.pop()
        counter += max(abs(x2-x1),abs(y2-y1))
        x1,y1 = x2,y2
    return counter

print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
