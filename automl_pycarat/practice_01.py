import pandas as pd
from palmerpenguins import load_penguins

# import pycaret
from  pycaret.classification import (
    setup, compare_models, save_model,
    load_model, predict_model)

# Load the data
penguins_df = load_penguins()

# Setup data & compare models
s = setup(data=penguins_df, target='species', session_id= 666)
best = compare_models()
save_model(best, 'penguins_best')


####################
# Inference
loaded_pipeline = load_model('penguins_best')
# Predict
infer_data = pd.DataFrame({'island': ['Biscoe'],
                         'bill_length_mm': [50.5],
                         'bill_depth_mm': [15.1],
                         'flipper_length_mm': [210],
                         'body_mass_g': [5000],
                         'sex': ['MALE'],
                         'year': [None]
                        })
new_pred = predict_model(loaded_pipeline, infer_data)
new_pred

# Predict on a sample of 5 rows
new_df = penguins_df.sample(5)
for index, row in new_df.iterrows() :
    df = pd.DataFrame(row).transpose()
    new = predict_model(loaded_pipeline, data=df)
    print("--------------------")
    print(new.iloc[:,0])