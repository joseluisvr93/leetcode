# Minimum Area
# Given a list of points described by their x and y coordinates on two dimensional plane,
# construct a square surrounding at least a given number of points within the area enclosed.
# That area should be minimal and the square mus meet the following conditions:
# 1. The x coordinates and y coordinates of the points should be integers.
# 2. The sides of the square should be parallel to the axes.
# 3. At least k of the given n points should lie strictly inside the square drawn.
#    Strictly inside means that they cannot lie on a side of the square.

def minAreaSquare(x,y,k):
    dist = {}
    points = []
    s = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            dist[s] = abs(x[i]-x[j])+abs(y[i]-y[j])
            s += 1
            points.append((i,j))
    dist = dict(sorted(dist.items(), key=lambda x: x[1]))
    points2 = set()
    for key in dist.keys():
        points2 = points2.union(set(points[key]))
        if len(points2) == k:
            break
    x = [x[i] for i in points2]
    y = [y[i] for i in points2]
    xsort = sorted(x)
    ysort = sorted(y)
    max_x = xsort[-1] - xsort[0]
    max_y = ysort[-1] - ysort[0]
    res = max(max_x, max_y)+2
    res = res * res
    return res

x = [-4,3,1]
y = [3,-1,-2]
k = 2
print(minAreaSquare(x,y,k))
