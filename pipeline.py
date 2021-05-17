import tensorflow as tf
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

class Resizer(BaseEstimator, TransformerMixin):
    def __init__(self,scale_factor=0.5):
        self.scale_factor = scale_factor

    def fit(self, X, y=None):
        return self # nothing to do
    
    def transform(self, X, y=None):
        _,w,h,_ = X.shape
        target_size = (int(w*self.scale_factor),int(h*self.scale_factor))
        return tf.image.resize(X, target_size)


pipe = Pipeline([
        ('resizer',Resizer())
    ])




