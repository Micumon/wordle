from Surveyor import *


list_points = PointsList(path_list, points)

with open(path_result, "w") as file:
    file.write(str(list_points))
