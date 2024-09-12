import pandas as pd
import pycaret
from  pycaret.classification import *
#from pycaret.classfication import *
# from palmerpenguins import load_penguins
# df = load_penguins()

df = pd.read_csv('penguins.csv')
s = setup(data=df, target='species', session_id= 123)

best = compare_models()
save_model(best, 'lightgbm')

loaded_pipeline = load_model('lightgbm')
predict_model(loaded_pipeline, df=new_df)

