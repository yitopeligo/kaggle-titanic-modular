from models import LogisticRegressor
from data_handler import TitanicDataIngestor

#Read the data by initializing custom Ingestor
data_ingestor = TitanicDataIngestor("data/train.csv")

#Preprocessing the data
data_ingestor.preprocess()

#Initialize the Model and train
LogReg = LogisticRegressor()
LogReg.train(data_ingestor.df)