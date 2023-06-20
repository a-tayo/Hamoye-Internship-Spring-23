# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 23:05:58 2023

@author: User
"""
import streamlit as st
from joblib import load
import pandas as pd

# interface of Streamlit application
st.title("Prediction of succesul terrorist attacks")



# Load the model
model = load('model.joblib')

# Create a dictionary with variable options
country_options = []
city_options = []

def set_country_option():
    global country_options
    if region_name == 'Australasia & Oceania':
        country_options = ['Australia', 'Papua New Guinea', 'New Caledonia', 
                        'New Zealand', 'Fiji', 'French Polynesia', 
                        'Solomon Islands', 'Wallis and Futuna', 'New Hebrides']

def set_city_option():
    pass

col1, col2, col3, col4, col5 = st.columns(5)

region_name = col1.selectbox("Select Region: ", sorted(['South Asia', 'South America', 'Eastern Europe', 'Western Europe',
                                                'Sub-Saharan Africa', 'Central America & Caribbean',
                                                'Middle East & North Africa', 'Southeast Asia', 'North America',
                                                'Australasia & Oceania', 'Central Asia', 'East Asia']), 
                                                on_change=set_country_option)
country_name = col2.selectbox("Select Country: ", sorted(country_options), help="Select region first", on_change=set_city_option)
city = col3.selectbox("Select City: ", sorted(city_options), help="Select country first")
duration_24hrs =  col4.selectbox("Is the attack duration greater than 24hrs?", ['Yes', 'No'])
ismultiple = col5.selectbox("Is the attack a single or multiple attack?", ['Single', 'Multiple'])

attacktype = col1.selectbox("Select the ataack type", sorted(['Armed Assault', 'Hostage Taking (Kidnapping)', 'Assassination',
                                                        'Bombing/Explosion', 'Hijacking', 'Unknown',
                                                        'Facility/Infrastructure Attack',
                                                        'Hostage Taking (Barricade Incident)', 'Unarmed Assault']))
targettype_name = col2.selectbox("Select the target type", sorted(['Private Citizens & Property', 'Police', 'Government (Diplomatic)',
                                                            'Military', 'Transportation', 'Unknown', 'Utilities',
                                                            'Government (General)', 'Violent Political Party',
                                                            'Journalists & Media', 'Business', 'Terrorists/Non-State Militia',
                                                            'NGO', 'Educational Institution', 'Religious Figures/Institutions',
                                                            'Telecommunication', 'Airports & Aircraft', 'Maritime',
                                                            'Abortion Related', 'Other', 'Tourists', 'Food or Water Supply']))
weapontype_name = col3.selectbox("Select the weapon type", sorted(['Firearms', 'Explosives', 'Unknown', 'Incendiary', 'Melee',
                                                                'Vehicle (not to include vehicle-borne explosives, i.e., car or truck bombs)',
                                                                'Radiological', 'Chemical', 'Fake Weapons', 'Sabotage Equipment',
                                                                'Other', 'Biological']))
kid_is_hostage = col4.selectbox("Is a kid held hostage?", ['Yes', 'No'])
group_name =  col5.selectbox("What is the group name?", sorted(['Unknown', 'Taliban', 'Islamic State of Iraq and the Levant (ISIL)',
                                                    'Shining Path (SL)', 'Farabundo Marti National Liberation Front (FMLN)',
                                                    'Al-Shabaab', 'New People\'s Army (NPA)', 'Irish Republican Army (IRA)',
                                                    'Revolutionary Armed Forces of Colombia (FARC)', 'Boko Haram',
                                                    'Kurdistan Workers\' Party (PKK)', 'Basque Fatherland and Freedom (ETA)',
                                                    'Communist Party of India - Maoist (CPI-Maoist)',
                                                    'Liberation Tigers of Tamil Eelam (LTTE)', 'Maoists',
                                                    'National Liberation Army of Colombia (ELN)',
                                                    'Tehrik-i-Taliban Pakistan (TTP)', 'Palestinians',
                                                    'Houthi extremists (Ansar Allah)',
                                                    'Al-Qaida in the Arabian Peninsula (AQAP)',
                                                    'Nicaraguan Democratic Force (FDN)',
                                                    'Manuel Rodriguez Patriotic Front (FPMR)', 'Sikh Extremists',
                                                    'Al-Qaida in Iraq', 'Muslim extremists',
                                                    'African National Congress (South Africa)']))

# Encode the selected values
df_pred = pd.DataFrame([region_name, country_name, city, duration_24hrs,
                         ismultiple, attacktype, targettype_name,
                         weapontype_name, kid_is_hostage, group_name],
                         columns=['region_name', 'country_name', 'city', 'Duration>24hrs',
                         'ismultiple', 'attacktype', 'targettype_name',
                         'weapontype_name', 'kid_is_hostage', 'group_name'])

if st.button("Get Prediction"):
    # Make predictions using the loaded model
    prediction = model.predict_proba(df_pred)[:, 1]

    # Show the prediction result
    if prediction >= 0.5:
        st.write("There is a high chance of success with the given conditions: Caution is advised")
    else:
        st.write("The chance of success is low with the given conditions.")

