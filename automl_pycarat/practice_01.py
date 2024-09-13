import pandas as pd
from palmerpenguins import load_penguins

# import pycaret
from  pycaret.classification import (
    setup, compare_models, save_model,
    load_model, predict_model)

penguins_df = load_penguins()
s = setup(data=penguins_df, target='species', session_id= 666)
best = compare_models()
save_model(best, 'lightgbm')

loaded_pipeline = load_model('lightgbm')
new_data = pd.DataFrame({'island': ['Biscoe'],
                         'culmen_length_mm': [50.5],
                         'culmen_depth_mm': [15.1],
                         'flipper_length_mm': [210],
                         'body_mass_g': [5000],
                         'sex': ['MALE']
                        })
new_pred = predict_model(loaded_pipeline, new_data)

new_df = penguins_df.sample(5)
new_pred = predict_model(loaded_pipeline, new_df)