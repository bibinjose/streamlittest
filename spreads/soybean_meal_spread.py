"""
#App to find patterns in Soybean Meal spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
color_selected=px.colors.qualitative.Alphabet
st.set_page_config(page_title=" Soybean Meal Spreads ",layout="wide")

SMF_H_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMF-H')
SMH_K_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMH-K')
SMK_N_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMK-N')
SMN_Q_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMN-Q')
SMQ_U_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMQ-U')
SMU_V_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMU-V')
SMV_Z_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMV-Z')
SMZ_F_df=pd.read_excel("soybean_meal_spread_data.xlsx",sheet_name='SMZ-F')


Soybean_Meal_spreads = { 
    'SMF-H': {
        'description':'Soybean Meal Jan-Mar',
        'data': SMF_H_df,
        'y1a1':['2023 SMF-H CLOSE','2022 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg'],
        'y2a1':['2023 SMF-H CLOSE','2022 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg'],
        'y3a1':['2023 SMF-H CLOSE','2022 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg'],
        'y1a2':['2023 SMF-H CLOSE','2022 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg','SMA10_SMF-H_Close_5yr',
                'SMA20_SMF-H_Close_5yr','SMA10_SMF-H_Close_10yr','SMA20_SMF-H_Close_10yr'],
        'y2a2':['2023 SMF-H CLOSE','2022 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg','SMA10_SMF-H_Close_5yr',
                'SMA20_SMF-H_Close_5yr','SMA10_SMF-H_Close_10yr','SMA20_SMF-H_Close_10yr'],
        'y3a2':['2023 SMF-H CLOSE','2022 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg'],
        'y1a3':['2018 SMF-H CLOSE','2019 SMF-H CLOSE','2020 SMF-H CLOSE','2021 SMF-H CLOSE',
                '2022 SMF-H CLOSE','2023 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg'],
        'y2a3':['2018 SMF-H CLOSE','2019 SMF-H CLOSE','2020 SMF-H CLOSE','2021 SMF-H CLOSE',
                '2022 SMF-H CLOSE','2023 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg'],
        'y3a3':['2018 SMF-H CLOSE','2019 SMF-H CLOSE','2020 SMF-H CLOSE','2021 SMF-H CLOSE',
                '2022 SMF-H CLOSE','2023 SMF-H CLOSE','SMF-H CLOSE 5 yr Avg','SMF-H CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMF-H VOLUME','2022 SMF-H VOLUME','SMF-H VOLUME 5 yr Avg','SMF-H VOLUME 10 yr Avg'],
        'y1b2':['2023 SMF-H VOLUME','2022 SMF-H VOLUME','SMF-H VOLUME 5 yr Avg','SMF-H VOLUME 10 yr Avg','SMA10_SMF-H_Vol_5yr',
                'SMA20_SMF-H_Vol_5yr','SMA10_SMF-H_Vol_10yr','SMA20_SMF-H_Vol_10yr'],
        'y1b3':['2018 SMF-H VOLUME','2019 SMF-H VOLUME','2020 SMF-H VOLUME','2021 SMF-H VOLUME',
                '2022 SMF-H VOLUME','2023 SMF-H VOLUME','SMF-H VOLUME 5 yr Avg','SMF-H VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMF OpenInt','2022 SMF OpenInt','SMF OpenInt 5 yr Avg','SMF OpenInt 10 yr Avg'],
        'y2b2':['2023 SMF OpenInt','2022 SMF OpenInt','SMF OpenInt 5 yr Avg','SMF OpenInt 10 yr Avg','SMA10_SMF_OpenInt_5yr',
                'SMA20_SMF_OpenInt_5yr','SMA10_SMF_OpenInt_10yr','SMA20_SMF_OpenInt_10yr'],
        'y2b3':['2018 SMF OpenInt','2019 SMF OpenInt','2020 SMF OpenInt','2021 SMF OpenInt',
                '2022 SMF OpenInt','2023 SMF OpenInt','SMF OpenInt 5 yr Avg','SMF OpenInt 10 yr Avg'],

        'y3b1':['2023 SMF-H OpenInt Ratio','2022 SMF-H OpenInt Ratio','SMF-H OpenInt Ratio 5 yr Avg','SMF-H OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMF-H OpenInt Ratio','2022 SMF-H OpenInt Ratio','SMF-H OpenInt Ratio 5 yr Avg','SMF-H OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMF-H OpenInt Ratio','2019 SMF-H OpenInt Ratio','2020 SMF-H OpenInt Ratio','2021 SMF-H OpenInt Ratio',
                '2022 SMF-H OpenInt Ratio','2023 SMF-H OpenInt Ratio','SMF-H OpenInt Ratio 5 yr Avg','SMF-H OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'SMH-K': {
        'description':'Soybean Meal Mar-May',
        'data': SMH_K_df,
        'y1a1':['2023 SMH-K CLOSE','2022 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg'],
        'y2a1':['2023 SMH-K CLOSE','2022 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg'],
        'y3a1':['2023 SMH-K CLOSE','2022 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg'],
        'y1a2':['2023 SMH-K CLOSE','2022 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg','SMA10_SMH-K_Close_5yr',
                'SMA20_SMH-K_Close_5yr','SMA10_SMH-K_Close_10yr','SMA20_SMH-K_Close_10yr'],
        'y2a2':['2023 SMH-K CLOSE','2022 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg','SMA10_SMH-K_Close_5yr',
                'SMA20_SMH-K_Close_5yr','SMA10_SMH-K_Close_10yr','SMA20_SMH-K_Close_10yr'],
        'y3a2':['2023 SMH-K CLOSE','2022 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg'],
        'y1a3':['2018 SMH-K CLOSE','2019 SMH-K CLOSE','2020 SMH-K CLOSE','2021 SMH-K CLOSE',
                '2022 SMH-K CLOSE','2023 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg'],
        'y2a3':['2018 SMH-K CLOSE','2019 SMH-K CLOSE','2020 SMH-K CLOSE','2021 SMH-K CLOSE',
                '2022 SMH-K CLOSE','2023 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg'],
        'y3a3':['2018 SMH-K CLOSE','2019 SMH-K CLOSE','2020 SMH-K CLOSE','2021 SMH-K CLOSE',
                '2022 SMH-K CLOSE','2023 SMH-K CLOSE','SMH-K CLOSE 5 yr Avg','SMH-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMH-K VOLUME','2022 SMH-K VOLUME','SMH-K VOLUME 5 yr Avg','SMH-K VOLUME 10 yr Avg'],
        'y1b2':['2023 SMH-K VOLUME','2022 SMH-K VOLUME','SMH-K VOLUME 5 yr Avg','SMH-K VOLUME 10 yr Avg','SMA10_SMH-K_Vol_5yr',
                'SMA20_SMH-K_Vol_5yr','SMA10_SMH-K_Vol_10yr','SMA20_SMH-K_Vol_10yr'],
        'y1b3':['2018 SMH-K VOLUME','2019 SMH-K VOLUME','2020 SMH-K VOLUME','2021 SMH-K VOLUME',
                '2022 SMH-K VOLUME','2023 SMH-K VOLUME','SMH-K VOLUME 5 yr Avg','SMH-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMH OpenInt','2022 SMH OpenInt','SMH OpenInt 5 yr Avg','SMH OpenInt 10 yr Avg'],
        'y2b2':['2023 SMH OpenInt','2022 SMH OpenInt','SMH OpenInt 5 yr Avg','SMH OpenInt 10 yr Avg','SMA10_SMH_OpenInt_5yr',
                'SMA20_SMH_OpenInt_5yr','SMA10_SMH_OpenInt_10yr','SMA20_SMH_OpenInt_10yr'],
        'y2b3':['2018 SMH OpenInt','2019 SMH OpenInt','2020 SMH OpenInt','2021 SMH OpenInt',
                '2022 SMH OpenInt','2023 SMH OpenInt','SMH OpenInt 5 yr Avg','SMH OpenInt 10 yr Avg'],

        'y3b1':['2023 SMH-K OpenInt Ratio','2022 SMH-K OpenInt Ratio','SMH-K OpenInt Ratio 5 yr Avg','SMH-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMH-K OpenInt Ratio','2022 SMH-K OpenInt Ratio','SMH-K OpenInt Ratio 5 yr Avg','SMH-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMH-K OpenInt Ratio','2019 SMH-K OpenInt Ratio','2020 SMH-K OpenInt Ratio','2021 SMH-K OpenInt Ratio',
                '2022 SMH-K OpenInt Ratio','2023 SMH-K OpenInt Ratio','SMH-K OpenInt Ratio 5 yr Avg','SMH-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
   'SMK-N': {
        'description':'Soybean Meal May-Jul',
        'data': SMK_N_df,
        'y1a1':['2023 SMK-N CLOSE','2022 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg'],
        'y2a1':['2023 SMK-N CLOSE','2022 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg'],
        'y3a1':['2023 SMK-N CLOSE','2022 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg'],
        'y1a2':['2023 SMK-N CLOSE','2022 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg','SMA10_SMK-N_Close_5yr',
                'SMA20_SMK-N_Close_5yr','SMA10_SMK-N_Close_10yr','SMA20_SMK-N_Close_10yr'],
        'y2a2':['2023 SMK-N CLOSE','2022 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg','SMA10_SMK-N_Close_5yr',
                'SMA20_SMK-N_Close_5yr','SMA10_SMK-N_Close_10yr','SMA20_SMK-N_Close_10yr'],
        'y3a2':['2023 SMK-N CLOSE','2022 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg'],
        'y1a3':['2018 SMK-N CLOSE','2019 SMK-N CLOSE','2020 SMK-N CLOSE','2021 SMK-N CLOSE',
                '2022 SMK-N CLOSE','2023 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg'],
        'y2a3':['2018 SMK-N CLOSE','2019 SMK-N CLOSE','2020 SMK-N CLOSE','2021 SMK-N CLOSE',
                '2022 SMK-N CLOSE','2023 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg'],
        'y3a3':['2018 SMK-N CLOSE','2019 SMK-N CLOSE','2020 SMK-N CLOSE','2021 SMK-N CLOSE',
                '2022 SMK-N CLOSE','2023 SMK-N CLOSE','SMK-N CLOSE 5 yr Avg','SMK-N CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMK-N VOLUME','2022 SMK-N VOLUME','SMK-N VOLUME 5 yr Avg','SMK-N VOLUME 10 yr Avg'],
        'y1b2':['2023 SMK-N VOLUME','2022 SMK-N VOLUME','SMK-N VOLUME 5 yr Avg','SMK-N VOLUME 10 yr Avg','SMA10_SMK-N_Vol_5yr',
                'SMA20_SMK-N_Vol_5yr','SMA10_SMK-N_Vol_10yr','SMA20_SMK-N_Vol_10yr'],
        'y1b3':['2018 SMK-N VOLUME','2019 SMK-N VOLUME','2020 SMK-N VOLUME','2021 SMK-N VOLUME',
                '2022 SMK-N VOLUME','2023 SMK-N VOLUME','SMK-N VOLUME 5 yr Avg','SMK-N VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMK OpenInt','2022 SMK OpenInt','SMK OpenInt 5 yr Avg','SMK OpenInt 10 yr Avg'],
        'y2b2':['2023 SMK OpenInt','2022 SMK OpenInt','SMK OpenInt 5 yr Avg','SMK OpenInt 10 yr Avg','SMA10_SMK_OpenInt_5yr',
                'SMA20_SMK_OpenInt_5yr','SMA10_SMK_OpenInt_10yr','SMA20_SMK_OpenInt_10yr'],
        'y2b3':['2018 SMK OpenInt','2019 SMK OpenInt','2020 SMK OpenInt','2021 SMK OpenInt',
                '2022 SMK OpenInt','2023 SMK OpenInt','SMK OpenInt 5 yr Avg','SMK OpenInt 10 yr Avg'],

        'y3b1':['2023 SMK-N OpenInt Ratio','2022 SMK-N OpenInt Ratio','SMK-N OpenInt Ratio 5 yr Avg','SMK-N OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMK-N OpenInt Ratio','2022 SMK-N OpenInt Ratio','SMK-N OpenInt Ratio 5 yr Avg','SMK-N OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMK-N OpenInt Ratio','2019 SMK-N OpenInt Ratio','2020 SMK-N OpenInt Ratio','2021 SMK-N OpenInt Ratio',
                '2022 SMK-N OpenInt Ratio','2023 SMK-N OpenInt Ratio','SMK-N OpenInt Ratio 5 yr Avg','SMK-N OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'SMN-Q': {
        'description':'Soybean Meal Jul-Aug',
        'data': SMN_Q_df,
        'y1a1':['2023 SMN-Q CLOSE','2022 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg'],
        'y2a1':['2023 SMN-Q CLOSE','2022 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg'],
        'y3a1':['2023 SMN-Q CLOSE','2022 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg'],
        'y1a2':['2023 SMN-Q CLOSE','2022 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg','SMA10_SMN-Q_Close_5yr',
                'SMA20_SMN-Q_Close_5yr','SMA10_SMN-Q_Close_10yr','SMA20_SMN-Q_Close_10yr'],
        'y2a2':['2023 SMN-Q CLOSE','2022 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg','SMA10_SMN-Q_Close_5yr',
                'SMA20_SMN-Q_Close_5yr','SMA10_SMN-Q_Close_10yr','SMA20_SMN-Q_Close_10yr'],
        'y3a2':['2023 SMN-Q CLOSE','2022 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg'],
        'y1a3':['2018 SMN-Q CLOSE','2019 SMN-Q CLOSE','2020 SMN-Q CLOSE','2021 SMN-Q CLOSE',
                '2022 SMN-Q CLOSE','2023 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg'],
        'y2a3':['2018 SMN-Q CLOSE','2019 SMN-Q CLOSE','2020 SMN-Q CLOSE','2021 SMN-Q CLOSE',
                '2022 SMN-Q CLOSE','2023 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg'],
        'y3a3':['2018 SMN-Q CLOSE','2019 SMN-Q CLOSE','2020 SMN-Q CLOSE','2021 SMN-Q CLOSE',
                '2022 SMN-Q CLOSE','2023 SMN-Q CLOSE','SMN-Q CLOSE 5 yr Avg','SMN-Q CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMN-Q VOLUME','2022 SMN-Q VOLUME','SMN-Q VOLUME 5 yr Avg','SMN-Q VOLUME 10 yr Avg'],
        'y1b2':['2023 SMN-Q VOLUME','2022 SMN-Q VOLUME','SMN-Q VOLUME 5 yr Avg','SMN-Q VOLUME 10 yr Avg','SMA10_SMN-Q_Vol_5yr',
                'SMA20_SMN-Q_Vol_5yr','SMA10_SMN-Q_Vol_10yr','SMA20_SMN-Q_Vol_10yr'],
        'y1b3':['2018 SMN-Q VOLUME','2019 SMN-Q VOLUME','2020 SMN-Q VOLUME','2021 SMN-Q VOLUME',
                '2022 SMN-Q VOLUME','2023 SMN-Q VOLUME','SMN-Q VOLUME 5 yr Avg','SMN-Q VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMN OpenInt','2022 SMN OpenInt','SMN OpenInt 5 yr Avg','SMN OpenInt 10 yr Avg'],
        'y2b2':['2023 SMN OpenInt','2022 SMN OpenInt','SMN OpenInt 5 yr Avg','SMN OpenInt 10 yr Avg','SMA10_SMN_OpenInt_5yr',
                'SMA20_SMN_OpenInt_5yr','SMA10_SMN_OpenInt_10yr','SMA20_SMN_OpenInt_10yr'],
        'y2b3':['2018 SMN OpenInt','2019 SMN OpenInt','2020 SMN OpenInt','2021 SMN OpenInt',
                '2022 SMN OpenInt','2023 SMN OpenInt','SMN OpenInt 5 yr Avg','SMN OpenInt 10 yr Avg'],

        'y3b1':['2023 SMN-Q OpenInt Ratio','2022 SMN-Q OpenInt Ratio','SMN-Q OpenInt Ratio 5 yr Avg','SMN-Q OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMN-Q OpenInt Ratio','2022 SMN-Q OpenInt Ratio','SMN-Q OpenInt Ratio 5 yr Avg','SMN-Q OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMN-Q OpenInt Ratio','2019 SMN-Q OpenInt Ratio','2020 SMN-Q OpenInt Ratio','2021 SMN-Q OpenInt Ratio',
                '2022 SMN-Q OpenInt Ratio','2023 SMN-Q OpenInt Ratio','SMN-Q OpenInt Ratio 5 yr Avg','SMN-Q OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },

       'SMQ-U': {
        'description':'Soybean Meal Aug-Sep',
        'data': SMQ_U_df,
        'y1a1':['2023 SMQ-U CLOSE','2022 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg'],
        'y2a1':['2023 SMQ-U CLOSE','2022 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg'],
        'y3a1':['2023 SMQ-U CLOSE','2022 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg'],
        'y1a2':['2023 SMQ-U CLOSE','2022 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg','SMA10_SMQ-U_Close_5yr',
                'SMA20_SMQ-U_Close_5yr','SMA10_SMQ-U_Close_10yr','SMA20_SMQ-U_Close_10yr'],
        'y2a2':['2023 SMQ-U CLOSE','2022 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg','SMA10_SMQ-U_Close_5yr',
                'SMA20_SMQ-U_Close_5yr','SMA10_SMQ-U_Close_10yr','SMA20_SMQ-U_Close_10yr'],
        'y3a2':['2023 SMQ-U CLOSE','2022 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg'],
        'y1a3':['2018 SMQ-U CLOSE','2019 SMQ-U CLOSE','2020 SMQ-U CLOSE','2021 SMQ-U CLOSE',
                '2022 SMQ-U CLOSE','2023 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg'],
        'y2a3':['2018 SMQ-U CLOSE','2019 SMQ-U CLOSE','2020 SMQ-U CLOSE','2021 SMQ-U CLOSE',
                '2022 SMQ-U CLOSE','2023 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg'],
        'y3a3':['2018 SMQ-U CLOSE','2019 SMQ-U CLOSE','2020 SMQ-U CLOSE','2021 SMQ-U CLOSE',
                '2022 SMQ-U CLOSE','2023 SMQ-U CLOSE','SMQ-U CLOSE 5 yr Avg','SMQ-U CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMQ-U VOLUME','2022 SMQ-U VOLUME','SMQ-U VOLUME 5 yr Avg','SMQ-U VOLUME 10 yr Avg'],
        'y1b2':['2023 SMQ-U VOLUME','2022 SMQ-U VOLUME','SMQ-U VOLUME 5 yr Avg','SMQ-U VOLUME 10 yr Avg','SMA10_SMQ-U_Vol_5yr',
                'SMA20_SMQ-U_Vol_5yr','SMA10_SMQ-U_Vol_10yr','SMA20_SMQ-U_Vol_10yr'],
        'y1b3':['2018 SMQ-U VOLUME','2019 SMQ-U VOLUME','2020 SMQ-U VOLUME','2021 SMQ-U VOLUME',
                '2022 SMQ-U VOLUME','2023 SMQ-U VOLUME','SMQ-U VOLUME 5 yr Avg','SMQ-U VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMQ OpenInt','2022 SMQ OpenInt','SMQ OpenInt 5 yr Avg','SMQ OpenInt 10 yr Avg'],
        'y2b2':['2023 SMQ OpenInt','2022 SMQ OpenInt','SMQ OpenInt 5 yr Avg','SMQ OpenInt 10 yr Avg','SMA10_SMQ_OpenInt_5yr',
                'SMA20_SMQ_OpenInt_5yr','SMA10_SMQ_OpenInt_10yr','SMA20_SMQ_OpenInt_10yr'],
        'y2b3':['2018 SMQ OpenInt','2019 SMQ OpenInt','2020 SMQ OpenInt','2021 SMQ OpenInt',
                '2022 SMQ OpenInt','2023 SMQ OpenInt','SMQ OpenInt 5 yr Avg','SMQ OpenInt 10 yr Avg'],

        'y3b1':['2023 SMQ-U OpenInt Ratio','2022 SMQ-U OpenInt Ratio','SMQ-U OpenInt Ratio 5 yr Avg','SMQ-U OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMQ-U OpenInt Ratio','2022 SMQ-U OpenInt Ratio','SMQ-U OpenInt Ratio 5 yr Avg','SMQ-U OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMQ-U OpenInt Ratio','2019 SMQ-U OpenInt Ratio','2020 SMQ-U OpenInt Ratio','2021 SMQ-U OpenInt Ratio',
                '2022 SMQ-U OpenInt Ratio','2023 SMQ-U OpenInt Ratio','SMQ-U OpenInt Ratio 5 yr Avg','SMQ-U OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
     'SMU-V': {
        'description':'Soybean Meal Sep-Oct',
        'data': SMU_V_df,
        'y1a1':['2023 SMU-V CLOSE','2022 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg'],
        'y2a1':['2023 SMU-V CLOSE','2022 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg'],
        'y3a1':['2023 SMU-V CLOSE','2022 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg'],
        'y1a2':['2023 SMU-V CLOSE','2022 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg','SMA10_SMU-V_Close_5yr',
                'SMA20_SMU-V_Close_5yr','SMA10_SMU-V_Close_10yr','SMA20_SMU-V_Close_10yr'],
        'y2a2':['2023 SMU-V CLOSE','2022 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg','SMA10_SMU-V_Close_5yr',
                'SMA20_SMU-V_Close_5yr','SMA10_SMU-V_Close_10yr','SMA20_SMU-V_Close_10yr'],
        'y3a2':['2023 SMU-V CLOSE','2022 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg'],
        'y1a3':['2018 SMU-V CLOSE','2019 SMU-V CLOSE','2020 SMU-V CLOSE','2021 SMU-V CLOSE',
                '2022 SMU-V CLOSE','2023 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg'],
        'y2a3':['2018 SMU-V CLOSE','2019 SMU-V CLOSE','2020 SMU-V CLOSE','2021 SMU-V CLOSE',
                '2022 SMU-V CLOSE','2023 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg'],
        'y3a3':['2018 SMU-V CLOSE','2019 SMU-V CLOSE','2020 SMU-V CLOSE','2021 SMU-V CLOSE',
                '2022 SMU-V CLOSE','2023 SMU-V CLOSE','SMU-V CLOSE 5 yr Avg','SMU-V CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMU-V VOLUME','2022 SMU-V VOLUME','SMU-V VOLUME 5 yr Avg','SMU-V VOLUME 10 yr Avg'],
        'y1b2':['2023 SMU-V VOLUME','2022 SMU-V VOLUME','SMU-V VOLUME 5 yr Avg','SMU-V VOLUME 10 yr Avg','SMA10_SMU-V_Vol_5yr',
                'SMA20_SMU-V_Vol_5yr','SMA10_SMU-V_Vol_10yr','SMA20_SMU-V_Vol_10yr'],
        'y1b3':['2018 SMU-V VOLUME','2019 SMU-V VOLUME','2020 SMU-V VOLUME','2021 SMU-V VOLUME',
                '2022 SMU-V VOLUME','2023 SMU-V VOLUME','SMU-V VOLUME 5 yr Avg','SMU-V VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMU OpenInt','2022 SMU OpenInt','SMU OpenInt 5 yr Avg','SMU OpenInt 10 yr Avg'],
        'y2b2':['2023 SMU OpenInt','2022 SMU OpenInt','SMU OpenInt 5 yr Avg','SMU OpenInt 10 yr Avg','SMA10_SMU_OpenInt_5yr',
                'SMA20_SMU_OpenInt_5yr','SMA10_SMU_OpenInt_10yr','SMA20_SMU_OpenInt_10yr'],
        'y2b3':['2018 SMU OpenInt','2019 SMU OpenInt','2020 SMU OpenInt','2021 SMU OpenInt',
                '2022 SMU OpenInt','2023 SMU OpenInt','SMU OpenInt 5 yr Avg','SMU OpenInt 10 yr Avg'],

        'y3b1':['2023 SMU-V OpenInt Ratio','2022 SMU-V OpenInt Ratio','SMU-V OpenInt Ratio 5 yr Avg','SMU-V OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMU-V OpenInt Ratio','2022 SMU-V OpenInt Ratio','SMU-V OpenInt Ratio 5 yr Avg','SMU-V OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMU-V OpenInt Ratio','2019 SMU-V OpenInt Ratio','2020 SMU-V OpenInt Ratio','2021 SMU-V OpenInt Ratio',
                '2022 SMU-V OpenInt Ratio','2023 SMU-V OpenInt Ratio','SMU-V OpenInt Ratio 5 yr Avg','SMU-V OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
     'SMV-Z': {
        'description':'Soybean Meal Oct-Dec',
        'data': SMV_Z_df,
        'y1a1':['2023 SMV-Z CLOSE','2022 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg'],
        'y2a1':['2023 SMV-Z CLOSE','2022 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg'],
        'y3a1':['2023 SMV-Z CLOSE','2022 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg'],
        'y1a2':['2023 SMV-Z CLOSE','2022 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg','SMA10_SMV-Z_Close_5yr',
                'SMA20_SMV-Z_Close_5yr','SMA10_SMV-Z_Close_10yr','SMA20_SMV-Z_Close_10yr'],
        'y2a2':['2023 SMV-Z CLOSE','2022 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg','SMA10_SMV-Z_Close_5yr',
                'SMA20_SMV-Z_Close_5yr','SMA10_SMV-Z_Close_10yr','SMA20_SMV-Z_Close_10yr'],
        'y3a2':['2023 SMV-Z CLOSE','2022 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg'],
        'y1a3':['2018 SMV-Z CLOSE','2019 SMV-Z CLOSE','2020 SMV-Z CLOSE','2021 SMV-Z CLOSE',
                '2022 SMV-Z CLOSE','2023 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg'],
        'y2a3':['2018 SMV-Z CLOSE','2019 SMV-Z CLOSE','2020 SMV-Z CLOSE','2021 SMV-Z CLOSE',
                '2022 SMV-Z CLOSE','2023 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg'],
        'y3a3':['2018 SMV-Z CLOSE','2019 SMV-Z CLOSE','2020 SMV-Z CLOSE','2021 SMV-Z CLOSE',
                '2022 SMV-Z CLOSE','2023 SMV-Z CLOSE','SMV-Z CLOSE 5 yr Avg','SMV-Z CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMV-Z VOLUME','2022 SMV-Z VOLUME','SMV-Z VOLUME 5 yr Avg','SMV-Z VOLUME 10 yr Avg'],
        'y1b2':['2023 SMV-Z VOLUME','2022 SMV-Z VOLUME','SMV-Z VOLUME 5 yr Avg','SMV-Z VOLUME 10 yr Avg','SMA10_SMV-Z_Vol_5yr',
                'SMA20_SMV-Z_Vol_5yr','SMA10_SMV-Z_Vol_10yr','SMA20_SMV-Z_Vol_10yr'],
        'y1b3':['2018 SMV-Z VOLUME','2019 SMV-Z VOLUME','2020 SMV-Z VOLUME','2021 SMV-Z VOLUME',
                '2022 SMV-Z VOLUME','2023 SMV-Z VOLUME','SMV-Z VOLUME 5 yr Avg','SMV-Z VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMV OpenInt','2022 SMV OpenInt','SMV OpenInt 5 yr Avg','SMV OpenInt 10 yr Avg'],
        'y2b2':['2023 SMV OpenInt','2022 SMV OpenInt','SMV OpenInt 5 yr Avg','SMV OpenInt 10 yr Avg','SMA10_SMV_OpenInt_5yr',
                'SMA20_SMV_OpenInt_5yr','SMA10_SMV_OpenInt_10yr','SMA20_SMV_OpenInt_10yr'],
        'y2b3':['2018 SMV OpenInt','2019 SMV OpenInt','2020 SMV OpenInt','2021 SMV OpenInt',
                '2022 SMV OpenInt','2023 SMV OpenInt','SMV OpenInt 5 yr Avg','SMV OpenInt 10 yr Avg'],

        'y3b1':['2023 SMV-Z OpenInt Ratio','2022 SMV-Z OpenInt Ratio','SMV-Z OpenInt Ratio 5 yr Avg','SMV-Z OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMV-Z OpenInt Ratio','2022 SMV-Z OpenInt Ratio','SMV-Z OpenInt Ratio 5 yr Avg','SMV-Z OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMV-Z OpenInt Ratio','2019 SMV-Z OpenInt Ratio','2020 SMV-Z OpenInt Ratio','2021 SMV-Z OpenInt Ratio',
                '2022 SMV-Z OpenInt Ratio','2023 SMV-Z OpenInt Ratio','SMV-Z OpenInt Ratio 5 yr Avg','SMV-Z OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
        'SMZ-F': {
        'description':'Soybean Meal Dec-Jan',
        'data': SMZ_F_df,
        'y1a1':['2023 SMZ-F CLOSE','2022 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg'],
        'y2a1':['2023 SMZ-F CLOSE','2022 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg'],
        'y3a1':['2023 SMZ-F CLOSE','2022 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg'],
        'y1a2':['2023 SMZ-F CLOSE','2022 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg','SMA10_SMZ-F_Close_5yr',
                'SMA20_SMZ-F_Close_5yr','SMA10_SMZ-F_Close_10yr','SMA20_SMZ-F_Close_10yr'],
        'y2a2':['2023 SMZ-F CLOSE','2022 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg','SMA10_SMZ-F_Close_5yr',
                'SMA20_SMZ-F_Close_5yr','SMA10_SMZ-F_Close_10yr','SMA20_SMZ-F_Close_10yr'],
        'y3a2':['2023 SMZ-F CLOSE','2022 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg'],
        'y1a3':['2018 SMZ-F CLOSE','2019 SMZ-F CLOSE','2020 SMZ-F CLOSE','2021 SMZ-F CLOSE',
                '2022 SMZ-F CLOSE','2023 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg'],
        'y2a3':['2018 SMZ-F CLOSE','2019 SMZ-F CLOSE','2020 SMZ-F CLOSE','2021 SMZ-F CLOSE',
                '2022 SMZ-F CLOSE','2023 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg'],
        'y3a3':['2018 SMZ-F CLOSE','2019 SMZ-F CLOSE','2020 SMZ-F CLOSE','2021 SMZ-F CLOSE',
                '2022 SMZ-F CLOSE','2023 SMZ-F CLOSE','SMZ-F CLOSE 5 yr Avg','SMZ-F CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SMZ-F VOLUME','2022 SMZ-F VOLUME','SMZ-F VOLUME 5 yr Avg','SMZ-F VOLUME 10 yr Avg'],
        'y1b2':['2023 SMZ-F VOLUME','2022 SMZ-F VOLUME','SMZ-F VOLUME 5 yr Avg','SMZ-F VOLUME 10 yr Avg','SMA10_SMZ-F_Vol_5yr',
                'SMA20_SMZ-F_Vol_5yr','SMA10_SMZ-F_Vol_10yr','SMA20_SMZ-F_Vol_10yr'],
        'y1b3':['2018 SMZ-F VOLUME','2019 SMZ-F VOLUME','2020 SMZ-F VOLUME','2021 SMZ-F VOLUME',
                '2022 SMZ-F VOLUME','2023 SMZ-F VOLUME','SMZ-F VOLUME 5 yr Avg','SMZ-F VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SMZ OpenInt','2022 SMZ OpenInt','SMZ OpenInt 5 yr Avg','SMZ OpenInt 10 yr Avg'],
        'y2b2':['2023 SMZ OpenInt','2022 SMZ OpenInt','SMZ OpenInt 5 yr Avg','SMZ OpenInt 10 yr Avg','SMA10_SMZ_OpenInt_5yr',
                'SMA20_SMZ_OpenInt_5yr','SMA10_SMZ_OpenInt_10yr','SMA20_SMZ_OpenInt_10yr'],
        'y2b3':['2018 SMZ OpenInt','2019 SMZ OpenInt','2020 SMZ OpenInt','2021 SMZ OpenInt',
                '2022 SMZ OpenInt','2023 SMZ OpenInt','SMZ OpenInt 5 yr Avg','SMZ OpenInt 10 yr Avg'],

        'y3b1':['2023 SMZ-F OpenInt Ratio','2022 SMZ-F OpenInt Ratio','SMZ-F OpenInt Ratio 5 yr Avg','SMZ-F OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SMZ-F OpenInt Ratio','2022 SMZ-F OpenInt Ratio','SMZ-F OpenInt Ratio 5 yr Avg','SMZ-F OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SMZ-F OpenInt Ratio','2019 SMZ-F OpenInt Ratio','2020 SMZ-F OpenInt Ratio','2021 SMZ-F OpenInt Ratio',
                '2022 SMZ-F OpenInt Ratio','2023 SMZ-F OpenInt Ratio','SMZ-F OpenInt Ratio 5 yr Avg','SMZ-F OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    }
    }



def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

        
titletxt='Price & Volume'
Subfig = make_subplots(specs=[[{"secondary_y": True}]])






with st.sidebar.container():
    spread = st.selectbox(
    'Select your spread',
    ('SMF-H','SMH-K','SMK-N','SMN-Q','SMQ-U','SMU-V','SMV-Z','SMZ-F'))

    st.write('Selected Spread:', Soybean_Meal_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=Soybean_Meal_spreads[spread]['y1a1']
    y1b=Soybean_Meal_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=Soybean_Meal_spreads[spread]['y1a2']
    y1b=Soybean_Meal_spreads[spread]['y1b2']

    
else:
    y1a=Soybean_Meal_spreads[spread]['y1a3']
    y1b=Soybean_Meal_spreads[spread]['y1b3']
    
fig = px.line(Soybean_Meal_spreads[spread]['data'], x=Soybean_Meal_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(Soybean_Meal_spreads[spread]['data'], x=Soybean_Meal_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

Subfig.add_traces(fig.data + fig2.data)
Subfig.layout.xaxis.title="Date"
Subfig.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig.layout.yaxis2.title="Spread Volume"
Subfig.layout.title=titletxt

Subfig.update_layout(
    title = Soybean_Meal_spreads[spread]['description']+"  Spread Price Vs Volume",
    xaxis_tickformat = '%b %d',
    colorway=color_selected

)


# recoloring is necessary otherwise lines from fig und fig2 would SMHare each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
Subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#Subfig.Show()

Subfig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)






#-------------------------------------------------------------------------------------------Subfig1--------------##########################********************************************


if selected_graph=='Latest and Historic Avg':
    y2a=Soybean_Meal_spreads[spread]['y2a1']
    y2b=Soybean_Meal_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=Soybean_Meal_spreads[spread]['y2a2']
    y2b=Soybean_Meal_spreads[spread]['y2b2']
    
    
else:
    y2a=Soybean_Meal_spreads[spread]['y2a3']
    y2b=Soybean_Meal_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
Subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(Soybean_Meal_spreads[spread]['data'], x=Soybean_Meal_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(Soybean_Meal_spreads[spread]['data'], x=Soybean_Meal_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

Subfig1.add_traces(fig1.data + fig12.data)
Subfig1.layout.xaxis.title="Date"
Subfig1.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig1.layout.yaxis2.title="Open Interest"
Subfig1.layout.title=titletxt1

Subfig1.update_layout(
    title = Soybean_Meal_spreads[spread]['description']+"  Spread Price Vs Open Interest",
    xaxis_tickformat = '%b %d',
    colorway=color_selected

)



# recoloring is necessary otherwise lines from fig und fig2 would SMHare each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
Subfig1.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#Subfig.Show()

Subfig1.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#----------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------Subfig2--------------##########################********************************************


if selected_graph=='Latest and Historic Avg':
    y3a=Soybean_Meal_spreads[spread]['y3a1']
    y3b=Soybean_Meal_spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=Soybean_Meal_spreads[spread]['y3a2']
    y3b=Soybean_Meal_spreads[spread]['y3b2']
    
    
else:
    y3a=Soybean_Meal_spreads[spread]['y3a3']
    y3b=Soybean_Meal_spreads[spread]['y3b3']

titletxt3='Price & Open Interest Ratio'
Subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(Soybean_Meal_spreads[spread]['data'], x=Soybean_Meal_spreads[spread]['x_value'], y=y3a, title=titletxt3)
fig12 = px.line(Soybean_Meal_spreads[spread]['data'], x=Soybean_Meal_spreads[spread]['x_value'], y=y3b, title=titletxt3)



fig12.update_traces(yaxis="y2")

Subfig2.add_traces(fig1.data + fig12.data)
Subfig2.layout.xaxis.title="Date"
Subfig2.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig2.layout.yaxis2.title="Open Interest Ratio"
Subfig2.layout.title=titletxt3

Subfig2.update_layout(
    title = Soybean_Meal_spreads[spread]['description']+"  Spread Price Vs Open Interest",
    xaxis_tickformat = '%b %d',
    colorway=color_selected

)



# recoloring is necessary otherwise lines from fig und fig2 would SMHare each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
Subfig2.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#Subfig.Show()

Subfig2.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#----------------------------------------------------------------------------------------------------------------


if selected_values=='Volume':
    Subfig.update_layout(height=650,width=1200)
    st.plotly_chart(Subfig,use_container_width = True,height=650,width=1200)
elif selected_values=='Open Interest':
    Subfig1.update_layout(height=650,width=1200)
    st.plotly_chart(Subfig1,use_container_width = True,height=650,width=1200)

else:
    Subfig2.update_layout(height=650,width=1200)
    st.plotly_chart(Subfig2,use_container_width = True,height=650,width=1200)
    
    

     



