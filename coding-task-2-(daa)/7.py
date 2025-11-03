import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])*2 + (p1[1] - p2[1])*2)
def brute_force(points):
    min_dist = math.inf
    pair = ()
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist
def strip_closest(strip, d_min):
    min_dist = d_min
    pair = ()
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                pair = (strip[i], strip[j])
    return pair, min_dist

def closest_pair(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)
    
    mid = n // 2
    mid_point = points[mid]
    left_pair, left_min = closest_pair(points[:mid])
    right_pair, right_min = closest_pair(points[mid:])
    if left_min < right_min:
        d_min = left_min
        best_pair = left_pair
    else:
        d_min = right_min
        best_pair = right_pair


    strip = [p for p in points if abs(p[0] - mid_point[0]) < d_min]
    strip_pair, strip_min = strip_closest(strip, d_min)
    if strip_min < d_min:
        return strip_pair, strip_min
    else:
        return best_pair, d_min
def find_closest_pair(points):
    points = sorted(points, key=lambda x: x[0])
    pair, dist = closest_pair(points)
    return pair, dist


#2D points
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
pair, min_distance = find_closest_pair(points)
print("Closest Pair of Points:", pair)
print("Minimum Distance:", round(min_distance, 4))