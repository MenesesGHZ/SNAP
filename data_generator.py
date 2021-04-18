import numpy as np
import cv2 as cv
from graphs import save_image

IMAGE_SHAPE = (1080, 1920, 3)
PINK_CONTINUES = ((100,20,100),(255,105,180))
PINK_DISCRETE = (255,102,204) 
SEED_RANGE = (0, np.iinfo(np.int32).max)
RANGE_SIZE = {"main":(80,250),"scatter":(5,25)}
NOISE_COLORS = ((0,0,0),(0,0,255),(0,255,00),(255,0,0))
 
    
def generator(samples):
    # defining an empty dataset 
    w,h,c = IMAGE_SHAPE
    x_samples = np.zeros(shape=(w,h,c,samples))
    y_samples = x_samples.copy()    
    # figures and noises attributes
    fig_len,noises_len = len(FIGURES),len(NOISES)
    fig_list,noises_list = list(FIGURES.keys()), list(NOISES.keys())
    for i in range(samples):
        # selecting functions
        figure = FIGURES[fig_list[i % fig_len]]    
        noise = NOISES[noises_list[i % noises_len]]
        # making samples
        #x_samples[:,:,:,i], y_samples[:,:,:,i] = make_sample(figure,noise,PINK_DISCRETE)
        x,y = make_sample(figure,noise,PINK_DISCRETE) 
        save_image(x,"./data/generated/x/"+str(i)+".png")
        save_image(y,"./data/generated/y/"+str(i)+".png")
        
    #return x_samples,y_samples    


def make_sample(figure,noise,main_color,background_color=(255,255,255)):
    x = np.zeros(shape=IMAGE_SHAPE) + background_color
    y = x.copy()
    
    # adding figures with main_color to 'x' frame.
    for _ in range(np.random.randint(3,15)):
        x = figure(x,main_color,RANGE_SIZE["main"])

    # adding same frames's noise
    seed = np.random.randint(*SEED_RANGE)
    x = noise(x,seed)
    y = noise(y,seed)
    return x,y


# defining noise functions
def add_scatter_noise(image,seed):
    set_seed(seed)
    for i in range(np.random.randint(10,50)):
        color = NOISE_COLORS[np.random.randint(0,len(NOISE_COLORS))]
        image = add_circle(image,color,RANGE_SIZE["scatter"])
        image = add_rectangle(image,color,RANGE_SIZE["scatter"])
    return image

# defining figure functions
def add_circle(image,color,range_size):
    radius = np.random.randint(*range_size)
    coords = ( np.random.randint(0,IMAGE_SHAPE[1]), np.random.randint(0,IMAGE_SHAPE[0]) )
    return cv.circle(image,coords, radius, color, -1)

def add_rectangle(image,color,range_size):
    x,y = np.random.randint(*range_size,size=2) 
    start_p = ( np.random.randint(0,IMAGE_SHAPE[1]) - x , np.random.randint(0,IMAGE_SHAPE[0]) - y )
    end_p = (start_p[0] + x, start_p[1] + y )
    return cv.rectangle(image, start_p, end_p, color, -1)

def add_mix_figures(image,color,range_size):
    image = add_circle(image,color,range_size)
    image = add_rectangle(image,color,range_size)
    return image

# set numpy random seed
def set_seed(seed):
    np.random.seed(seed if seed else np.random.randint(*SEED_RANGE))

# get a random color `inside` of pink range
def get_inner_color():
    bottom_c, top_c = PINK_CONTINUES 
    r,g,b = [ np.random.randint(bottom_c[i],top_c[i]) for i in range(3) ]
    return (r,g,b)

# get a random color `outside` of pink range
def get_outer_color():
    i = np.random.randint(0,2)
    color_range = PINK_CONTINUES[i]
    color_limit = (i*254, i*254, i*254)
    r,g,b = [ sorted([color_limit[i],color_range[i]]) for i in range(3) ] 
    r,g,b = np.random.randint(*r), np.random.randint(*g), np.random.randint(*b)
    return (r,g,b)

FIGURES = {"rectangle":add_rectangle,
           "circle":add_circle,
           "mix":add_mix_figures}

NOISES = {"nothing":(lambda image,*args,**kwargs: image),
          "scatter":add_scatter_noise
          #"mix": add_mix_noise
          }
