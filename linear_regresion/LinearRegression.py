

import numpy as np
class LinearRegression:

    def __init__(self,lr=0.001, n_iterations=1000):
        self.lr = lr
        self.n_iterations= n_iterations
        self.weight = None
        self.bias = None

    def fit(self, X,y):
        n_samples, n_features =X.shape

        self.weight = np.zeros(n_features)
        self.bias = 0
         

        for _ in range(self.n_iterations): 
        ##y =wx+b
           y_pred = np.dot(X ,self.weight) + self.bias
 


           dw = (1/n_samples) * np.dot(X.T ,(y_pred - y))
           db = (1/n_samples) * np.sum(y_pred - y)

         ##update weight and bias

           self.weight =self.weight - self.lr * dw
           self.bias =self.bias - self.lr * db



    def predict(self,X):
        y_pred = np.dot(X ,self.weight) + self.bias
        return y_pred




        



    