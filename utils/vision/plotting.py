import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import io

def plot_image_with_faces(image_url, boxes):
    plt.rcParams["figure.figsize"] = (80,8)
    
    img_array = io.imread(image_url, format='jpg')
    fig,ax = plt.subplots(1)
    ax.imshow(img_array)
    
    for box in boxes:
        rect = patches.Rectangle((box.left,box.top),box.width,box.height,linewidth=2,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
    
    plt.show()

def plot_image_with_boxes(image_url, boxes):
    plt.rcParams["figure.figsize"] = (80,8)
    
    img_array = io.imread(image_url, format='jpg')
    fig,ax = plt.subplots(1)
    ax.imshow(img_array)
    
    for box in boxes:
        rect = patches.Rectangle((box.x,box.y),box.w,box.h,linewidth=2,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
    
    plt.show()