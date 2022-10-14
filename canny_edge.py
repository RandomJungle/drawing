import cv2
import os
import re

from tqdm import tqdm


def extract_edges(image_path, threshold1, threshold2):
    # the 0 means grayscale, remove it to get the color version
    gray = cv2.imread(image_path, 0)
    # Using the Canny filter to get contours
    edges = cv2.Canny(gray, threshold1, threshold2)
    return edges


def extract_edges_from_folder(input_path, output_path):
    # should start at 30 and can go up to 150 but lets start small
    for i in tqdm(range(30, 161, 20)):
        for j in range(30, 161, 20):
            for image_file in os.listdir(input_path):
                if image_file.endswith('png') or image_file.endswith('jpg'):
                    edges = extract_edges(os.path.join(input_path, image_file), i, j)
                    file_without_trail = re.sub(r"\.\w{1,10}$", "", image_file)
                    new_name = f'{file_without_trail}_edges_{i}_{j}.jpg'
                    cv2.imwrite(os.path.join(output_path, new_name), edges)


def invert_color(image_array):
    image_array[image_array == 0] = 254
    image_array[image_array == 255] = 0
    image_array[image_array == 254] = 255
    return image_array
