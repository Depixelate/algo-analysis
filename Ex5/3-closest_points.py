import math
import matplotlib.pyplot as plt
import random
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tuple(self):
        return (self.x, self.y)
    
    @staticmethod
    def dist(a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2
    
def closest_points(points):
    points_sorted_x = sorted(points, key = lambda p:p.x)
    points_sorted_y = sorted(points, key = lambda p:p.y)
    return closest_points_helper(points_sorted_x, points_sorted_y)

def closest_points_helper(points_x, points_y):
    if len(points_x) == 1:
        return None, None, math.inf
    if len(points_x) == 2:
        return points_x[0], points_x[1], Point.dist(points_x[0], points_x[1])

    left_x, right_x = points_x[:len(points_x)//2], points_x[len(points_x)//2:]
    boundary_x = (left_x[-1].x + right_x[0].x) / 2
    #plt.vlines(boundary_x, 0, 100)
    left_y, right_y = [point for point in points_y if point.x <= boundary_x], [point for point in points_y if point.x > boundary_x]

    left_p1, left_p2, left_d = closest_points_helper(left_x, left_y)
    right_p1, right_p2, right_d = closest_points_helper(right_x, right_y)

    p1, p2, d = (left_p1, left_p2, left_d) if left_d < right_d else (right_p1, right_p2, right_d)

    cross_y = [point for point in points_y if abs(point.x - boundary_x) < d]

    for i, point in enumerate(cross_y):
        for j in range(i+1, len(cross_y)):
            if cross_y[j].y - point.y >= d:
                break
            if (temp_d := Point.dist(point, cross_y[j])) < d:
                p1, p2, d = point, cross_y[j], temp_d

    return p1, p2, d

n = 100
points = [Point(random.uniform(0, 100), random.uniform(0, 100)) for i in range(n)]
start = time.perf_counter()
ap1, ap2, ad = None,  None, math.inf
for i, t1 in enumerate(points):
    for t2 in points[i+1:]:
        if((temp_d:=Point.dist(t1, t2)) < ad):
            ad = temp_d
            ap1 = t1
            ap2 = t2
print(f"{ad=}")
end = time.perf_counter()
print(f"{end - start = }")
plt.scatter(*zip(*[p.tuple() for p in points]), c='blue')
start = time.perf_counter()
p1, p2, d = closest_points(points)
print(f"{d=}")
end = time.perf_counter()
print(f"{end - start = }")
plt.scatter([p1.x, p2.x], [p1.y, p2.y], color = 'green')
plt.scatter([ap1.x,ap2.x], [ap1.y, ap2.y], color = 'red')
#plt.hlines(0, 0, 100)
plt.show()