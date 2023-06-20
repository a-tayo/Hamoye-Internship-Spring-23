# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:05:58 2023

@author: User
"""
import streamlit as st
import joblib
import pandas as pd
from 

# interface of Streamlit application
st.title("Prediction of succesul terrorist attacks")



# Load the model
model = joblib.load('path_to_your_model_file.joblib')

# Create a dictionary with variable options



variable_options = {
    'country_name': ['Iraq','Pakistan','Afghanistan','India','Colombia','Philippines','Peru','El Salvador','United Kingdom',
                     'Turkey','Somalia','Nigeria', 'Thailand','Yemen','Spain','Sri Lanka','United States']  
    'region_name': [],
    'Duration>24hrs': ['option1', 'option2', 'option3'],
    'city': ['option1', 'option2', 'option3'],
    'ismultiple': ['option1', 'option2', 'option3'],
    'attacktype': ['option1', 'option2', 'option3'],
    'targettype_name': ['option1', 'option2', 'option3'],
    'weapontype_name': ['option1', 'option2', 'option3'],
    'kid_is_hostage': ['option1', 'option2', 'option3'],
    'group_name': ['option1', 'option2', 'option3']
}

# Create a dictionary to store the selected values for each variable
selected_values = {}

# Create the dropdowns for variable selection
for variable, options in variable_options.items():
    selected_values[variable] = st.selectbox(f'Select {variable}', options)

# Encode the selected values
encoded_values = pd.DataFrame(selected_values, index=[0])

# Make predictions using the loaded model
prediction = model.predict(encoded_values)[0]

# Show the prediction result
if prediction == 1:
    st.write("The terrorist attack is predicted to be successful.")
else:
    st.write("The terrorist attack is predicted to be unsuccessful.")

