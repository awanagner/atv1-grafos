mport matplotlib.pyplot as plt
import geopandas as gpd

import shapely
import shapely.geometry
import re

def readVertices(arquivo):
  V = []
  numvertices = int(arquivo.readline())

  for vert in range( numvertices):
    vertices = re.findall("(^\d*/?.\d*), (\d*/?.\d*)",  arq.readline())

    #print(vertices[0])

    V.append([float(vertices[0][0]), float(vertices[0][1])])
  return V

arq = open("map.txt", "r")
start_str = re.findall("(\d+)",  arq.readline())
start_int = [int(start_str[0]), int(start_str[1])]

print(start_int)
goal_int = [int(goal_str[0]), int(goal_str[1])]
goal_str = re.findall("(\d+)",  arq.readline())

print(goal_int)

obstacles = int(arq.readline())

V = []
for obs in range(0, obstacles):
    V.append(readVertices(arq))

shapely_poly = shapely.geometry.Polygon(V[1])

print(shapely_poly)

print(V)

p = gpd.GeoSeries(shapely_poly)
p.plot()
plt.show()
