import math
from operator import add

print("Enter the coordinates of the point: ")
x = (int)
point=list(map(int,input().split(" ")))

axes = list(input("Enter axes about which to rotate(in x,y,z with spaces): ").split(" "))
for i in axes:
    new_points = []
    print("Rotation about " + i + "-axis(in degrees),enter in negative value for ClockWise rotation: ")
    degrees = math.radians(int(input()))
    if i=='x':
        new_points.append(point[0])
        new_points.append((point[1]*math.cos(degrees)) - point[2]*math.sin(degrees))
        new_points.append((point[1]*math.sin(degrees)) + point[2]*math.cos(degrees))
    if i=='y':
        new_points.append((point[0]*math.cos(degrees)) - point[2]*math.sin(degrees))
        new_points.append(point[1])
        new_points.append((point[0]*math.sin(degrees)) + point[2]*math.cos(degrees))
    if i=='z':
        new_points.append((point[0]*math.cos(degrees)) - point[1]*math.sin(degrees))
        new_points.append((point[0]*math.sin(degrees)) + point[1]*math.cos(degrees))
        new_points.append(point[2])

    point = new_points

trans = [int(input()) for i in range(3)]
final = list(map(add, point, trans)) 
print(final)
