import numpy as np

MIN_RGB = 0
MAX_RGB = 255

ARRAYS_PATH = "arrays/"
OUTPUTS_PATH = "outputs/"

file_name = "cube.txt"
# file_name = "teddybear.txt"
# file_name = "smooth-sphere.txt"
# file_name = "pot.txt"

def import_data(file_name):
    arrays = []
    unique_arrays = []

    with open(ARRAYS_PATH + file_name, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            
            values = line.strip().split(',')
            if values[-1] == '':
                values.pop()
            
            try:
                float_values = [float(val) for val in values]
                arrays.append(float_values)
            except ValueError:
                continue
            
            if float_values not in unique_arrays:
                unique_arrays.append(float_values)

    return arrays, unique_arrays

def center_of_mass(vector3):
    x = 0
    y = 0
    z = 0
    for i in range(len(vector3)):
        x += vector3[i][0]
        y += vector3[i][1]
        z += vector3[i][2]
    x /= len(vector3)
    y /= len(vector3)
    z /= len(vector3)
    return [x, y, z]

def get_random_midpoint():
    return np.random.uniform(MIN_RGB, MAX_RGB) / MAX_RGB

def distance_from_center(vector3, center):
    return np.sqrt((vector3[0] - center[0])**2 + (vector3[1] - center[1])**2 + (vector3[2] - center[2])**2) * np.sign(vector3[2] - center[2])

def colorize(distance, max_distance, random_midpoints):
    ratio = distance / max_distance
    return [ratio * (random_midpoints[0] * MAX_RGB) + (MAX_RGB - random_midpoints[0] * MAX_RGB), ratio * (random_midpoints[1] * MAX_RGB) + (MAX_RGB - random_midpoints[1] * MAX_RGB), ratio * (random_midpoints[2] * MAX_RGB) + (MAX_RGB - random_midpoints[2] * MAX_RGB)]

def write_data_with_rgb(array, rgb_array):
    with open(OUTPUTS_PATH + "colorized-" + file_name, 'w') as file:
        for i in range(len(array)):
            if i == len(array) - 1:
                file.write(str(array[i][0]) + ',' + str(array[i][1]) + ',' + str(array[i][2]) + ',' + "1.0," + str(rgb_array[i][0]) + ',' + str(rgb_array[i][1]) + ',' + str(rgb_array[i][2]))
            else:
                file.write(str(array[i][0]) + ',' + str(array[i][1]) + ',' + str(array[i][2]) + ',' + "1.0," + str(rgb_array[i][0]) + ',' + str(rgb_array[i][1]) + ',' + str(rgb_array[i][2]) + ',\n')

array, unique_array = import_data(file_name)
center = center_of_mass(unique_array)
distances_from_center = [distance_from_center(vector3, center) for vector3 in array]
max_distance = max(distances_from_center)
random_midpoints = [get_random_midpoint(), get_random_midpoint(), get_random_midpoint()]
print(random_midpoints)
rgb_array = [colorize(distance, max_distance, random_midpoints) for distance in distances_from_center]
write_data_with_rgb(array, rgb_array)