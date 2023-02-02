"""
#App to find patterns in HRW  spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
color_selected=px.colors.qualitative.Alphabet
st.set_page_config(page_title=" HRW Spreads ",layout="wide")

KWH_K_df=pd.read_excel("hard_red_winter_spread_data.xlsx",sheet_name='KWH-K')
KWK_N_df=pd.read_excel("hard_red_winter_spread_data.xlsx",sheet_name='KWK-N')
KWN_U_df=pd.read_excel("hard_red_winter_spread_data.xlsx",sheet_name='KWN-U')
KWU_Z_df=pd.read_excel("hard_red_winter_spread_data.xlsx",sheet_name='KWU-Z')
KWZ_H_df=pd.read_excel("hard_red_winter_spread_data.xlsx",sheet_name='KWZ-H')



HRW_spreads = { 
    'KWH-K': {
        'description':'HRW Jan-Mar',
        'data': KWH_K_df,
        'y1a1':['2023 KWH-K CLOSE','2022 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg'],
        'y2a1':['2023 KWH-K CLOSE','2022 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg'],
        'y3a1':['2023 KWH-K CLOSE','2022 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg'],
        'y1a2':['2023 KWH-K CLOSE','2022 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg','SMA10_KWH-K_Close_5yr',
                'SMA20_KWH-K_Close_5yr','SMA10_KWH-K_Close_10yr','SMA20_KWH-K_Close_10yr'],
        'y2a2':['2023 KWH-K CLOSE','2022 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg','SMA10_KWH-K_Close_5yr',
                'SMA20_KWH-K_Close_5yr','SMA10_KWH-K_Close_10yr','SMA20_KWH-K_Close_10yr'],
        'y3a2':['2023 KWH-K CLOSE','2022 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg'],
        'y1a3':['2018 KWH-K CLOSE','2019 KWH-K CLOSE','2020 KWH-K CLOSE','2021 KWH-K CLOSE',
                '2022 KWH-K CLOSE','2023 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg'],
        'y2a3':['2018 KWH-K CLOSE','2019 KWH-K CLOSE','2020 KWH-K CLOSE','2021 KWH-K CLOSE',
                '2022 KWH-K CLOSE','2023 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg'],
        'y3a3':['2018 KWH-K CLOSE','2019 KWH-K CLOSE','2020 KWH-K CLOSE','2021 KWH-K CLOSE',
                '2022 KWH-K CLOSE','2023 KWH-K CLOSE','KWH-K CLOSE 5 yr Avg','KWH-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 KWH-K VOLUME','2022 KWH-K VOLUME','KWH-K VOLUME 5 yr Avg','KWH-K VOLUME 10 yr Avg'],
        'y1b2':['2023 KWH-K VOLUME','2022 KWH-K VOLUME','KWH-K VOLUME 5 yr Avg','KWH-K VOLUME 10 yr Avg','SMA10_KWH-K_Vol_5yr',
                'SMA20_KWH-K_Vol_5yr','SMA10_KWH-K_Vol_10yr','SMA20_KWH-K_Vol_10yr'],
        'y1b3':['2018 KWH-K VOLUME','2019 KWH-K VOLUME','2020 KWH-K VOLUME','2021 KWH-K VOLUME',
                '2022 KWH-K VOLUME','2023 KWH-K VOLUME','KWH-K VOLUME 5 yr Avg','KWH-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 KWH OpenInt','2022 KWH OpenInt','KWH OpenInt 5 yr Avg','KWH OpenInt 10 yr Avg'],
        'y2b2':['2023 KWH OpenInt','2022 KWH OpenInt','KWH OpenInt 5 yr Avg','KWH OpenInt 10 yr Avg','SMA10_KWH_OpenInt_5yr',
                'SMA20_KWH_OpenInt_5yr','SMA10_KWH_OpenInt_10yr','SMA20_KWH_OpenInt_10yr'],
        'y2b3':['2018 KWH OpenInt','2019 KWH OpenInt','2020 KWH OpenInt','2021 KWH OpenInt',
                '2022 KWH OpenInt','2023 KWH OpenInt','KWH OpenInt 5 yr Avg','KWH OpenInt 10 yr Avg'],

        'y3b1':['2023 KWH-K OpenInt Ratio','2022 KWH-K OpenInt Ratio','KWH-K OpenInt Ratio 5 yr Avg','KWH-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 KWH-K OpenInt Ratio','2022 KWH-K OpenInt Ratio','KWH-K OpenInt Ratio 5 yr Avg','KWH-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 KWH-K OpenInt Ratio','2019 KWH-K OpenInt Ratio','2020 KWH-K OpenInt Ratio','2021 KWH-K OpenInt Ratio',
                '2022 KWH-K OpenInt Ratio','2023 KWH-K OpenInt Ratio','KWH-K OpenInt Ratio 5 yr Avg','KWH-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'KWK-N': {
        'description':'HRW Mar-May',
        'data': KWK_N_df,
        'y1a1':['2023 KWK-N CLOSE','2022 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg'],
        'y2a1':['2023 KWK-N CLOSE','2022 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg'],
        'y3a1':['2023 KWK-N CLOSE','2022 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg'],
        'y1a2':['2023 KWK-N CLOSE','2022 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg','SMA10_KWK-N_Close_5yr',
                'SMA20_KWK-N_Close_5yr','SMA10_KWK-N_Close_10yr','SMA20_KWK-N_Close_10yr'],
        'y2a2':['2023 KWK-N CLOSE','2022 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg','SMA10_KWK-N_Close_5yr',
                'SMA20_KWK-N_Close_5yr','SMA10_KWK-N_Close_10yr','SMA20_KWK-N_Close_10yr'],
        'y3a2':['2023 KWK-N CLOSE','2022 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg'],
        'y1a3':['2018 KWK-N CLOSE','2019 KWK-N CLOSE','2020 KWK-N CLOSE','2021 KWK-N CLOSE',
                '2022 KWK-N CLOSE','2023 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg'],
        'y2a3':['2018 KWK-N CLOSE','2019 KWK-N CLOSE','2020 KWK-N CLOSE','2021 KWK-N CLOSE',
                '2022 KWK-N CLOSE','2023 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg'],
        'y3a3':['2018 KWK-N CLOSE','2019 KWK-N CLOSE','2020 KWK-N CLOSE','2021 KWK-N CLOSE',
                '2022 KWK-N CLOSE','2023 KWK-N CLOSE','KWK-N CLOSE 5 yr Avg','KWK-N CLOSE 10 yr Avg'],

        
        'y1b1':['2023 KWK-N VOLUME','2022 KWK-N VOLUME','KWK-N VOLUME 5 yr Avg','KWK-N VOLUME 10 yr Avg'],
        'y1b2':['2023 KWK-N VOLUME','2022 KWK-N VOLUME','KWK-N VOLUME 5 yr Avg','KWK-N VOLUME 10 yr Avg','SMA10_KWK-N_Vol_5yr',
                'SMA20_KWK-N_Vol_5yr','SMA10_KWK-N_Vol_10yr','SMA20_KWK-N_Vol_10yr'],
        'y1b3':['2018 KWK-N VOLUME','2019 KWK-N VOLUME','2020 KWK-N VOLUME','2021 KWK-N VOLUME',
                '2022 KWK-N VOLUME','2023 KWK-N VOLUME','KWK-N VOLUME 5 yr Avg','KWK-N VOLUME 10 yr Avg'],
        
        'y2b1':['2023 KWK OpenInt','2022 KWK OpenInt','KWK OpenInt 5 yr Avg','KWK OpenInt 10 yr Avg'],
        'y2b2':['2023 KWK OpenInt','2022 KWK OpenInt','KWK OpenInt 5 yr Avg','KWK OpenInt 10 yr Avg','SMA10_KWK_OpenInt_5yr',
                'SMA20_KWK_OpenInt_5yr','SMA10_KWK_OpenInt_10yr','SMA20_KWK_OpenInt_10yr'],
        'y2b3':['2018 KWK OpenInt','2019 KWK OpenInt','2020 KWK OpenInt','2021 KWK OpenInt',
                '2022 KWK OpenInt','2023 KWK OpenInt','KWK OpenInt 5 yr Avg','KWK OpenInt 10 yr Avg'],

        'y3b1':['2023 KWK-N OpenInt Ratio','2022 KWK-N OpenInt Ratio','KWK-N OpenInt Ratio 5 yr Avg','KWK-N OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 KWK-N OpenInt Ratio','2022 KWK-N OpenInt Ratio','KWK-N OpenInt Ratio 5 yr Avg','KWK-N OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 KWK-N OpenInt Ratio','2019 KWK-N OpenInt Ratio','2020 KWK-N OpenInt Ratio','2021 KWK-N OpenInt Ratio',
                '2022 KWK-N OpenInt Ratio','2023 KWK-N OpenInt Ratio','KWK-N OpenInt Ratio 5 yr Avg','KWK-N OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
   'KWN-U': {
        'description':'HRW May-Jul',
        'data': KWN_U_df,
        'y1a1':['2023 KWN-U CLOSE','2022 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg'],
        'y2a1':['2023 KWN-U CLOSE','2022 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg'],
        'y3a1':['2023 KWN-U CLOSE','2022 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg'],
        'y1a2':['2023 KWN-U CLOSE','2022 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg','SMA10_KWN-U_Close_5yr',
                'SMA20_KWN-U_Close_5yr','SMA10_KWN-U_Close_10yr','SMA20_KWN-U_Close_10yr'],
        'y2a2':['2023 KWN-U CLOSE','2022 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg','SMA10_KWN-U_Close_5yr',
                'SMA20_KWN-U_Close_5yr','SMA10_KWN-U_Close_10yr','SMA20_KWN-U_Close_10yr'],
        'y3a2':['2023 KWN-U CLOSE','2022 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg'],
        'y1a3':['2018 KWN-U CLOSE','2019 KWN-U CLOSE','2020 KWN-U CLOSE','2021 KWN-U CLOSE',
                '2022 KWN-U CLOSE','2023 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg'],
        'y2a3':['2018 KWN-U CLOSE','2019 KWN-U CLOSE','2020 KWN-U CLOSE','2021 KWN-U CLOSE',
                '2022 KWN-U CLOSE','2023 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg'],
        'y3a3':['2018 KWN-U CLOSE','2019 KWN-U CLOSE','2020 KWN-U CLOSE','2021 KWN-U CLOSE',
                '2022 KWN-U CLOSE','2023 KWN-U CLOSE','KWN-U CLOSE 5 yr Avg','KWN-U CLOSE 10 yr Avg'],

        
        'y1b1':['2023 KWN-U VOLUME','2022 KWN-U VOLUME','KWN-U VOLUME 5 yr Avg','KWN-U VOLUME 10 yr Avg'],
        'y1b2':['2023 KWN-U VOLUME','2022 KWN-U VOLUME','KWN-U VOLUME 5 yr Avg','KWN-U VOLUME 10 yr Avg','SMA10_KWN-U_Vol_5yr',
                'SMA20_KWN-U_Vol_5yr','SMA10_KWN-U_Vol_10yr','SMA20_KWN-U_Vol_10yr'],
        'y1b3':['2018 KWN-U VOLUME','2019 KWN-U VOLUME','2020 KWN-U VOLUME','2021 KWN-U VOLUME',
                '2022 KWN-U VOLUME','2023 KWN-U VOLUME','KWN-U VOLUME 5 yr Avg','KWN-U VOLUME 10 yr Avg'],
        
        'y2b1':['2023 KWN OpenInt','2022 KWN OpenInt','KWN OpenInt 5 yr Avg','KWN OpenInt 10 yr Avg'],
        'y2b2':['2023 KWN OpenInt','2022 KWN OpenInt','KWN OpenInt 5 yr Avg','KWN OpenInt 10 yr Avg','SMA10_KWN_OpenInt_5yr',
                'SMA20_KWN_OpenInt_5yr','SMA10_KWN_OpenInt_10yr','SMA20_KWN_OpenInt_10yr'],
        'y2b3':['2018 KWN OpenInt','2019 KWN OpenInt','2020 KWN OpenInt','2021 KWN OpenInt',
                '2022 KWN OpenInt','2023 KWN OpenInt','KWN OpenInt 5 yr Avg','KWN OpenInt 10 yr Avg'],

        'y3b1':['2023 KWN-U OpenInt Ratio','2022 KWN-U OpenInt Ratio','KWN-U OpenInt Ratio 5 yr Avg','KWN-U OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 KWN-U OpenInt Ratio','2022 KWN-U OpenInt Ratio','KWN-U OpenInt Ratio 5 yr Avg','KWN-U OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 KWN-U OpenInt Ratio','2019 KWN-U OpenInt Ratio','2020 KWN-U OpenInt Ratio','2021 KWN-U OpenInt Ratio',
                '2022 KWN-U OpenInt Ratio','2023 KWN-U OpenInt Ratio','KWN-U OpenInt Ratio 5 yr Avg','KWN-U OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'KWU-Z': {
        'description':'HRW Jul-Aug',
        'data': KWU_Z_df,
        'y1a1':['2023 KWU-Z CLOSE','2022 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg'],
        'y2a1':['2023 KWU-Z CLOSE','2022 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg'],
        'y3a1':['2023 KWU-Z CLOSE','2022 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg'],
        'y1a2':['2023 KWU-Z CLOSE','2022 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg','SMA10_KWU-Z_Close_5yr',
                'SMA20_KWU-Z_Close_5yr','SMA10_KWU-Z_Close_10yr','SMA20_KWU-Z_Close_10yr'],
        'y2a2':['2023 KWU-Z CLOSE','2022 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg','SMA10_KWU-Z_Close_5yr',
                'SMA20_KWU-Z_Close_5yr','SMA10_KWU-Z_Close_10yr','SMA20_KWU-Z_Close_10yr'],
        'y3a2':['2023 KWU-Z CLOSE','2022 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg'],
        'y1a3':['2018 KWU-Z CLOSE','2019 KWU-Z CLOSE','2020 KWU-Z CLOSE','2021 KWU-Z CLOSE',
                '2022 KWU-Z CLOSE','2023 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg'],
        'y2a3':['2018 KWU-Z CLOSE','2019 KWU-Z CLOSE','2020 KWU-Z CLOSE','2021 KWU-Z CLOSE',
                '2022 KWU-Z CLOSE','2023 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg'],
        'y3a3':['2018 KWU-Z CLOSE','2019 KWU-Z CLOSE','2020 KWU-Z CLOSE','2021 KWU-Z CLOSE',
                '2022 KWU-Z CLOSE','2023 KWU-Z CLOSE','KWU-Z CLOSE 5 yr Avg','KWU-Z CLOSE 10 yr Avg'],

        
        'y1b1':['2023 KWU-Z VOLUME','2022 KWU-Z VOLUME','KWU-Z VOLUME 5 yr Avg','KWU-Z VOLUME 10 yr Avg'],
        'y1b2':['2023 KWU-Z VOLUME','2022 KWU-Z VOLUME','KWU-Z VOLUME 5 yr Avg','KWU-Z VOLUME 10 yr Avg','SMA10_KWU-Z_Vol_5yr',
                'SMA20_KWU-Z_Vol_5yr','SMA10_KWU-Z_Vol_10yr','SMA20_KWU-Z_Vol_10yr'],
        'y1b3':['2018 KWU-Z VOLUME','2019 KWU-Z VOLUME','2020 KWU-Z VOLUME','2021 KWU-Z VOLUME',
                '2022 KWU-Z VOLUME','2023 KWU-Z VOLUME','KWU-Z VOLUME 5 yr Avg','KWU-Z VOLUME 10 yr Avg'],
        
        'y2b1':['2023 KWU OpenInt','2022 KWU OpenInt','KWU OpenInt 5 yr Avg','KWU OpenInt 10 yr Avg'],
        'y2b2':['2023 KWU OpenInt','2022 KWU OpenInt','KWU OpenInt 5 yr Avg','KWU OpenInt 10 yr Avg','SMA10_KWU_OpenInt_5yr',
                'SMA20_KWU_OpenInt_5yr','SMA10_KWU_OpenInt_10yr','SMA20_KWU_OpenInt_10yr'],
        'y2b3':['2018 KWU OpenInt','2019 KWU OpenInt','2020 KWU OpenInt','2021 KWU OpenInt',
                '2022 KWU OpenInt','2023 KWU OpenInt','KWU OpenInt 5 yr Avg','KWU OpenInt 10 yr Avg'],

        'y3b1':['2023 KWU-Z OpenInt Ratio','2022 KWU-Z OpenInt Ratio','KWU-Z OpenInt Ratio 5 yr Avg','KWU-Z OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 KWU-Z OpenInt Ratio','2022 KWU-Z OpenInt Ratio','KWU-Z OpenInt Ratio 5 yr Avg','KWU-Z OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 KWU-Z OpenInt Ratio','2019 KWU-Z OpenInt Ratio','2020 KWU-Z OpenInt Ratio','2021 KWU-Z OpenInt Ratio',
                '2022 KWU-Z OpenInt Ratio','2023 KWU-Z OpenInt Ratio','KWU-Z OpenInt Ratio 5 yr Avg','KWU-Z OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },

       'KWZ-H': {
        'description':'HRW Aug-Sep',
        'data': KWZ_H_df,
        'y1a1':['2023 KWZ-H CLOSE','2022 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg'],
        'y2a1':['2023 KWZ-H CLOSE','2022 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg'],
        'y3a1':['2023 KWZ-H CLOSE','2022 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg'],
        'y1a2':['2023 KWZ-H CLOSE','2022 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg','SMA10_KWZ-H_Close_5yr',
                'SMA20_KWZ-H_Close_5yr','SMA10_KWZ-H_Close_10yr','SMA20_KWZ-H_Close_10yr'],
        'y2a2':['2023 KWZ-H CLOSE','2022 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg','SMA10_KWZ-H_Close_5yr',
                'SMA20_KWZ-H_Close_5yr','SMA10_KWZ-H_Close_10yr','SMA20_KWZ-H_Close_10yr'],
        'y3a2':['2023 KWZ-H CLOSE','2022 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg'],
        'y1a3':['2018 KWZ-H CLOSE','2019 KWZ-H CLOSE','2020 KWZ-H CLOSE','2021 KWZ-H CLOSE',
                '2022 KWZ-H CLOSE','2023 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg'],
        'y2a3':['2018 KWZ-H CLOSE','2019 KWZ-H CLOSE','2020 KWZ-H CLOSE','2021 KWZ-H CLOSE',
                '2022 KWZ-H CLOSE','2023 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg'],
        'y3a3':['2018 KWZ-H CLOSE','2019 KWZ-H CLOSE','2020 KWZ-H CLOSE','2021 KWZ-H CLOSE',
                '2022 KWZ-H CLOSE','2023 KWZ-H CLOSE','KWZ-H CLOSE 5 yr Avg','KWZ-H CLOSE 10 yr Avg'],

        
        'y1b1':['2023 KWZ-H VOLUME','2022 KWZ-H VOLUME','KWZ-H VOLUME 5 yr Avg','KWZ-H VOLUME 10 yr Avg'],
        'y1b2':['2023 KWZ-H VOLUME','2022 KWZ-H VOLUME','KWZ-H VOLUME 5 yr Avg','KWZ-H VOLUME 10 yr Avg','SMA10_KWZ-H_Vol_5yr',
                'SMA20_KWZ-H_Vol_5yr','SMA10_KWZ-H_Vol_10yr','SMA20_KWZ-H_Vol_10yr'],
        'y1b3':['2018 KWZ-H VOLUME','2019 KWZ-H VOLUME','2020 KWZ-H VOLUME','2021 KWZ-H VOLUME',
                '2022 KWZ-H VOLUME','2023 KWZ-H VOLUME','KWZ-H VOLUME 5 yr Avg','KWZ-H VOLUME 10 yr Avg'],
        
        'y2b1':['2023 KWZ OpenInt','2022 KWZ OpenInt','KWZ OpenInt 5 yr Avg','KWZ OpenInt 10 yr Avg'],
        'y2b2':['2023 KWZ OpenInt','2022 KWZ OpenInt','KWZ OpenInt 5 yr Avg','KWZ OpenInt 10 yr Avg','SMA10_KWZ_OpenInt_5yr',
                'SMA20_KWZ_OpenInt_5yr','SMA10_KWZ_OpenInt_10yr','SMA20_KWZ_OpenInt_10yr'],
        'y2b3':['2018 KWZ OpenInt','2019 KWZ OpenInt','2020 KWZ OpenInt','2021 KWZ OpenInt',
                '2022 KWZ OpenInt','2023 KWZ OpenInt','KWZ OpenInt 5 yr Avg','KWZ OpenInt 10 yr Avg'],

        'y3b1':['2023 KWZ-H OpenInt Ratio','2022 KWZ-H OpenInt Ratio','KWZ-H OpenInt Ratio 5 yr Avg','KWZ-H OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 KWZ-H OpenInt Ratio','2022 KWZ-H OpenInt Ratio','KWZ-H OpenInt Ratio 5 yr Avg','KWZ-H OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 KWZ-H OpenInt Ratio','2019 KWZ-H OpenInt Ratio','2020 KWZ-H OpenInt Ratio','2021 KWZ-H OpenInt Ratio',
                '2022 KWZ-H OpenInt Ratio','2023 KWZ-H OpenInt Ratio','KWZ-H OpenInt Ratio 5 yr Avg','KWZ-H OpenInt Ratio 10 yr Avg'],

        
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
    ('KWH-K','KWK-N','KWN-U','KWU-Z','KWZ-H'))

    st.write('Selected Spread:', HRW_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=HRW_spreads[spread]['y1a1']
    y1b=HRW_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=HRW_spreads[spread]['y1a2']
    y1b=HRW_spreads[spread]['y1b2']

    
else:
    y1a=HRW_spreads[spread]['y1a3']
    y1b=HRW_spreads[spread]['y1b3']
    
fig = px.line(HRW_spreads[spread]['data'], x=HRW_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(HRW_spreads[spread]['data'], x=HRW_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

Subfig.add_traces(fig.data + fig2.data)
Subfig.layout.xaxis.title="Date"
Subfig.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig.layout.yaxis2.title="Spread Volume"
Subfig.layout.title=titletxt

Subfig.update_layout(
    title = HRW_spreads[spread]['description']+"  Spread Price Vs Volume",
    xaxis_tickformat = '%b %d',
    colorway=color_selected

)


# recoloring is necessary otherwise lines from fig und fig2 would SHare each color
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
    y2a=HRW_spreads[spread]['y2a1']
    y2b=HRW_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=HRW_spreads[spread]['y2a2']
    y2b=HRW_spreads[spread]['y2b2']
    
    
else:
    y2a=HRW_spreads[spread]['y2a3']
    y2b=HRW_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
Subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(HRW_spreads[spread]['data'], x=HRW_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(HRW_spreads[spread]['data'], x=HRW_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

Subfig1.add_traces(fig1.data + fig12.data)
Subfig1.layout.xaxis.title="Date"
Subfig1.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig1.layout.yaxis2.title="Open Interest"
Subfig1.layout.title=titletxt1

Subfig1.update_layout(
    title = HRW_spreads[spread]['description']+"  Spread Price Vs Open Interest",
    xaxis_tickformat = '%b %d',
    colorway=color_selected

)



# recoloring is necessary otherwise lines from fig und fig2 would SHare each color
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
    y3a=HRW_spreads[spread]['y3a1']
    y3b=HRW_spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=HRW_spreads[spread]['y3a2']
    y3b=HRW_spreads[spread]['y3b2']
    
    
else:
    y3a=HRW_spreads[spread]['y3a3']
    y3b=HRW_spreads[spread]['y3b3']

titletxt3='Price & Open Interest Ratio'
Subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(HRW_spreads[spread]['data'], x=HRW_spreads[spread]['x_value'], y=y3a, title=titletxt3)
fig12 = px.line(HRW_spreads[spread]['data'], x=HRW_spreads[spread]['x_value'], y=y3b, title=titletxt3)



fig12.update_traces(yaxis="y2")

Subfig2.add_traces(fig1.data + fig12.data)
Subfig2.layout.xaxis.title="Date"
Subfig2.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig2.layout.yaxis2.title="Open Interest Ratio"
Subfig2.layout.title=titletxt3

Subfig2.update_layout(
    title = HRW_spreads[spread]['description']+"  Spread Price Vs Open Interest",
    xaxis_tickformat = '%b %d',
    colorway=color_selected

)



# recoloring is necessary otherwise lines from fig und fig2 would SHare each color
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
    
    

     



