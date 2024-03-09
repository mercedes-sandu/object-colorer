import numpy as np
import matplotlib.pyplot as plt

MIN_RGB = 0
MAX_RGB = 255

ARRAYS_PATH = "arrays/"
OUTPUTS_PATH = "outputs/"

USE_COLORMAP = True
COLOR_R = 1.0
COLOR_G = 1.0
COLOR_B = 1.0

# to see all possible colormaps, visit: https://matplotlib.org/stable/users/explain/colors/colormaps.html
COLOR_MAP = "viridis"

# file_name = "cube.txt"
# file_name = "teddybear.txt"
# file_name = "smooth-sphere.txt"
# file_name = "pot.txt"
# file_name = "bunny.txt"
# file_name = "sphere.txt"
# file_name = "teapot.txt"
# file_name = "sphere-new.txt"
# file_name = "octahedron.txt"
# file_name = "heptagonal-prism.txt"
file_name = "icosahedron.txt"

def import_data(file_name):
    arrays = []

    with open(ARRAYS_PATH + file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue

            values = line.strip().split(",")
            if values[-1] == "":
                values.pop()

            try:
                float_values = [float(val) for val in values]
                arrays.append(float_values)
            except ValueError:
                continue

    return arrays

def calculate_centroid(vertices):
    centroid = np.mean(vertices, axis=0)
    return centroid

def calculate_direction(vertex, centroid):
    direction = vertex - centroid
    return direction / np.linalg.norm(direction)

def calculate_distance(vertex, centroid):
    distance = np.linalg.norm(vertex - centroid)
    return distance

def assign_color_based_on_direction(direction):
    angle = np.arctan2(direction[1], direction[0])
    normalized_angle = (angle + np.pi) / (2 * np.pi)
    
    cmap = plt.get_cmap(COLOR_MAP)
    color = cmap(normalized_angle)
    return color

def assign_one_color(r, g, b):
    return [r, g, b]

def write_data_with_rgb(array, rgb_array):
    with open(OUTPUTS_PATH + "colorized-" + file_name, "w") as file:
        for i in range(len(array)):
            if i == len(array) - 1:
                file.write(
                    str(array[i][0])
                    + ","
                    + str(array[i][1])
                    + ","
                    + str(array[i][2])
                    + ","
                    + "1.0,"
                    + str(rgb_array[i][0])
                    + ","
                    + str(rgb_array[i][1])
                    + ","
                    + str(rgb_array[i][2])
                )
            else:
                file.write(
                    str(array[i][0])
                    + ","
                    + str(array[i][1])
                    + ","
                    + str(array[i][2])
                    + ","
                    + "1.0,"
                    + str(rgb_array[i][0])
                    + ","
                    + str(rgb_array[i][1])
                    + ","
                    + str(rgb_array[i][2])
                    + ",\n"
                )

vertices = np.array(import_data(file_name))
centroid = calculate_centroid(vertices)

directions = [calculate_direction(vertex, centroid) for vertex in vertices]
distances = [calculate_distance(vertex, centroid) for vertex in vertices]
max_distances = max(distances)

colors = [assign_color_based_on_direction(direction) for direction in directions] if USE_COLORMAP else [assign_one_color(COLOR_R, COLOR_G, COLOR_B) for direction in directions]

write_data_with_rgb(vertices, colors)