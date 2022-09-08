import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.nonparametric.kde import KDEUnivariate
from statsmodels.nonparametric import smoothers_lowess
from pandas import Series, DataFrame

class TitanicDataIngestor():
    def __init__(self, datafile):
        
        self.df = pd.read_csv(datafile)
        
        
    def preprocess(self):
        
        #Drop NaN values
        self.df = self.df.drop(['Ticket','Cabin'], axis=1)
        self.df = self.df.dropna()    
        
        return self.df
        
    def plot_features(self):
        
        """Plots five different feature exploration of dataset"""
        
        # specifies the parameters of our graphs
        fig = plt.figure(figsize=(18,6), dpi=1600) 
        alpha=alpha_scatterplot = 0.2 
        alpha_bar_chart = 0.55

        # lets us plot many diffrent shaped graphs together 
        ax1 = plt.subplot2grid((2,3),(0,0))
        # plots a bar graph of those who surived vs those who did not.               
        self.df.Survived.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
        # this nicely sets the margins in matplotlib to deal with a recent bug 1.3.1
        ax1.set_xlim(-1, 2)
        # puts a title on our graph
        plt.title("Distribution of Survival, (1 = Survived)")    

        plt.subplot2grid((2,3),(0,1))
        plt.scatter(self.df.Survived, self.df.Age, alpha=alpha_scatterplot)
        # sets the y axis lable
        plt.ylabel("Age")
        # formats the grid line style of our graphs                          
        plt.grid(b=True, which='major', axis='y')  
        plt.title("Survival by Age,  (1 = Survived)")

        ax3 = plt.subplot2grid((2,3),(0,2))
        self.df.Pclass.value_counts().plot(kind="barh", alpha=alpha_bar_chart)
        ax3.set_ylim(-1, len(self.df.Pclass.value_counts()))
        plt.title("Class Distribution")

        plt.subplot2grid((2,3),(1,0), colspan=2)
        # plots a kernel density estimate of the subset of the 1st class passangers's age
        self.df.Age[df.Pclass == 1].plot(kind='kde')    
        self.df.Age[df.Pclass == 2].plot(kind='kde')
        self.df.Age[df.Pclass == 3].plot(kind='kde')
         # plots an axis lable
        plt.xlabel("Age")    
        plt.title("Age Distribution within classes")
        # sets our legend for our graph.
        plt.legend(('1st Class', '2nd Class','3rd Class'),loc='best') 

        ax5 = plt.subplot2grid((2,3),(1,2))
        self.df.Embarked.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
        ax5.set_xlim(-1, len(df.Embarked.value_counts()))
        # specifies the parameters of our graphs
        plt.title("Passengers per boarding location")