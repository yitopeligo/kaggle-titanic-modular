import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.nonparametric.kde import KDEUnivariate
from statsmodels.nonparametric import smoothers_lowess
from pandas import Series, DataFrame
from patsy import dmatrices
from sklearn import datasets, svm
from KaggleAux import predict as ka # see github.com/agconti/kaggleaux for more details

        
class LogisticRegressor():
    
    def __init__(self):
        
        self.formula = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp  + C(Embarked)'
        self.results = {}
        
    def train(self, df):
        
        """Training function of Kaggle's Logistic Regression Model
        
        
        Saves the results into dictionary: results
        Scikit-Learn model into: sci_model
        
        ___
        
        Returns: None
        
        """
        
        # create a regression friendly dataframe using patsy's dmatrices function
        self.y, self.x = dmatrices(self.formula, data=df, return_type='dataframe')

        # instantiate our model
        self.sci_model = sm.Logit(self.y, self.x)

        # fit our model to the training data
        self.res = self.sci_model.fit()

        # save the result for outputing predictions later
        self.results['Logit'] = [self.res, self.formula]
        
    def plot_results(self):
        
        """Plots the results of Logit predictions and Logit Residuals"""
        
        # Plot Predictions Vs Actual
        plt.figure(figsize=(18,4));
        plt.subplot(121, axisbg="#DBDBDB")
        # generate predictions from our fitted model
        ypred = self.res.predict(self.x)
        plt.plot(self.x.index, ypred, 'bo', self.x.index, self.y, 'mo', alpha=.25);
        plt.grid(color='white', linestyle='dashed')
        plt.title('Logit predictions, Blue: \nFitted/predicted values: Red');

        # Residuals
        ax2 = plt.subplot(122, axisbg="#DBDBDB")
        plt.plot(self.res.resid_dev, 'r-')
        plt.grid(color='white', linestyle='dashed')
        ax2.set_xlim(-1, len(self.res.resid_dev))
        plt.title('Logit Residuals');