import matplotlib.pyplot as plt
from matplotlib.image import imsave

def show_image(image):
    plt.imshow(image/255)
    plt.show()

def save_image(image,path_name):
    imsave(path_name, image/255)
