import re
import numpy as np
import os
from matplotlib.image import imread
from PIL import Image
import random
from tqdm import tqdm


def draw_from_folder(input_path, output_path, brushes_path):
    brushes = [Image.open(os.path.join(brushes_path, brush_file))
               for brush_file in os.listdir(brushes_path)]
    for image_file in tqdm(os.listdir(input_path)):
        if image_file.endswith('jpg'):
            edges = imread(os.path.join(input_path, image_file))
            file_without_trail = re.sub(r"\.\w{1,10}$", "", image_file)
            new_name = f'{file_without_trail}_drawing.jpg'
            draw_from_edges(
                edges, brushes, os.path.join(output_path, new_name))


def draw_from_edges(edges: np.array, brushes, output_path):
    with Image.new('RGB', size=edges.shape, color='white') as output_img:
        for x in range(0, edges.shape[0]):
            for y in range(0, edges.shape[1]):
                if edges[x, y] == 255:
                    brush = random.choice(brushes)
                    # brush.putalpha(50)
                    output_img.paste(brush, (x, y), brush)
        output_img.save(output_path)
