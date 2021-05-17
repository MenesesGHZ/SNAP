from data_generator import generator,load_dataset
from model import CAE
from pipeline import pipe
from graphs import show_image 

if __name__ == "__main__":
    #generator(100)
    (x_train,y_train),(x_test,y_test) = load_dataset(3)
    x_train = pipe.fit_transform(x_train)
 