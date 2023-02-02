"""
#App to find patterns in Soybean Meal spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
color_selected=px.colors.qualitative.Alphabet
st.set_page_config(page_title=" Soybean Spreads ",layout="wide")

SF_H_df=pd.read_excel("soybean_spread_data.xlsx",sheet_name='SF-H')
SH_K_df=pd.read_excel("soybean_spread_data.xlsx",sheet_name='SH-K')
SK_N_df=pd.read_excel("soybean_spread_data.xlsx",sheet_name='SK-N')
SN_Q_df=pd.read_excel("soybean_spread_data.xlsx",sheet_name='SN-Q')
SQ_U_df=pd.read_excel("soybean_spread_data.xlsx",sheet_name='SQ-U')
SU_X_df=pd.read_excel("soybean_spread_data.xlsx",sheet_name='SU-X')
SX_F_df=pd.read_excel("soybean_spread_data.xlsx",sheet_name='SX-F')



Soybean_spreads = { 
    'SF-H': {
        'description':'Soybean Jan-Mar',
        'data': SF_H_df,
        'y1a1':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y2a1':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y3a1':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y1a2':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg','SMA10_SF-H_Close_5yr',
                'SMA20_SF-H_Close_5yr','SMA10_SF-H_Close_10yr','SMA20_SF-H_Close_10yr'],
        'y2a2':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg','SMA10_SF-H_Close_5yr',
                'SMA20_SF-H_Close_5yr','SMA10_SF-H_Close_10yr','SMA20_SF-H_Close_10yr'],
        'y3a2':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y1a3':['2018 SF-H CLOSE','2019 SF-H CLOSE','2020 SF-H CLOSE','2021 SF-H CLOSE',
                '2022 SF-H CLOSE','2023 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y2a3':['2018 SF-H CLOSE','2019 SF-H CLOSE','2020 SF-H CLOSE','2021 SF-H CLOSE',
                '2022 SF-H CLOSE','2023 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y3a3':['2018 SF-H CLOSE','2019 SF-H CLOSE','2020 SF-H CLOSE','2021 SF-H CLOSE',
                '2022 SF-H CLOSE','2023 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SF-H VOLUME','2022 SF-H VOLUME','SF-H VOLUME 5 yr Avg','SF-H VOLUME 10 yr Avg'],
        'y1b2':['2023 SF-H VOLUME','2022 SF-H VOLUME','SF-H VOLUME 5 yr Avg','SF-H VOLUME 10 yr Avg','SMA10_SF-H_Vol_5yr',
                'SMA20_SF-H_Vol_5yr','SMA10_SF-H_Vol_10yr','SMA20_SF-H_Vol_10yr'],
        'y1b3':['2018 SF-H VOLUME','2019 SF-H VOLUME','2020 SF-H VOLUME','2021 SF-H VOLUME',
                '2022 SF-H VOLUME','2023 SF-H VOLUME','SF-H VOLUME 5 yr Avg','SF-H VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SF OpenInt','2022 SF OpenInt','SF OpenInt 5 yr Avg','SF OpenInt 10 yr Avg'],
        'y2b2':['2023 SF OpenInt','2022 SF OpenInt','SF OpenInt 5 yr Avg','SF OpenInt 10 yr Avg','SMA10_SF_OpenInt_5yr',
                'SMA20_SF_OpenInt_5yr','SMA10_SF_OpenInt_10yr','SMA20_SF_OpenInt_10yr'],
        'y2b3':['2018 SF OpenInt','2019 SF OpenInt','2020 SF OpenInt','2021 SF OpenInt',
                '2022 SF OpenInt','2023 SF OpenInt','SF OpenInt 5 yr Avg','SF OpenInt 10 yr Avg'],

        'y3b1':['2023 SF-H OpenInt Ratio','2022 SF-H OpenInt Ratio','SF-H OpenInt Ratio 5 yr Avg','SF-H OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SF-H OpenInt Ratio','2022 SF-H OpenInt Ratio','SF-H OpenInt Ratio 5 yr Avg','SF-H OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SF-H OpenInt Ratio','2019 SF-H OpenInt Ratio','2020 SF-H OpenInt Ratio','2021 SF-H OpenInt Ratio',
                '2022 SF-H OpenInt Ratio','2023 SF-H OpenInt Ratio','SF-H OpenInt Ratio 5 yr Avg','SF-H OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'SH-K': {
        'description':'Soybean Mar-May',
        'data': SH_K_df,
        'y1a1':['2023 SH-K CLOSE','2022 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y2a1':['2023 SH-K CLOSE','2022 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y3a1':['2023 SH-K CLOSE','2022 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y1a2':['2023 SH-K CLOSE','2022 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg','SMA10_SH-K_Close_5yr',
                'SMA20_SH-K_Close_5yr','SMA10_SH-K_Close_10yr','SMA20_SH-K_Close_10yr'],
        'y2a2':['2023 SH-K CLOSE','2022 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg','SMA10_SH-K_Close_5yr',
                'SMA20_SH-K_Close_5yr','SMA10_SH-K_Close_10yr','SMA20_SH-K_Close_10yr'],
        'y3a2':['2023 SH-K CLOSE','2022 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y1a3':['2018 SH-K CLOSE','2019 SH-K CLOSE','2020 SH-K CLOSE','2021 SH-K CLOSE',
                '2022 SH-K CLOSE','2023 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y2a3':['2018 SH-K CLOSE','2019 SH-K CLOSE','2020 SH-K CLOSE','2021 SH-K CLOSE',
                '2022 SH-K CLOSE','2023 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y3a3':['2018 SH-K CLOSE','2019 SH-K CLOSE','2020 SH-K CLOSE','2021 SH-K CLOSE',
                '2022 SH-K CLOSE','2023 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SH-K VOLUME','2022 SH-K VOLUME','SH-K VOLUME 5 yr Avg','SH-K VOLUME 10 yr Avg'],
        'y1b2':['2023 SH-K VOLUME','2022 SH-K VOLUME','SH-K VOLUME 5 yr Avg','SH-K VOLUME 10 yr Avg','SMA10_SH-K_Vol_5yr',
                'SMA20_SH-K_Vol_5yr','SMA10_SH-K_Vol_10yr','SMA20_SH-K_Vol_10yr'],
        'y1b3':['2018 SH-K VOLUME','2019 SH-K VOLUME','2020 SH-K VOLUME','2021 SH-K VOLUME',
                '2022 SH-K VOLUME','2023 SH-K VOLUME','SH-K VOLUME 5 yr Avg','SH-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SH OpenInt','2022 SH OpenInt','SH OpenInt 5 yr Avg','SH OpenInt 10 yr Avg'],
        'y2b2':['2023 SH OpenInt','2022 SH OpenInt','SH OpenInt 5 yr Avg','SH OpenInt 10 yr Avg','SMA10_SH_OpenInt_5yr',
                'SMA20_SH_OpenInt_5yr','SMA10_SH_OpenInt_10yr','SMA20_SH_OpenInt_10yr'],
        'y2b3':['2018 SH OpenInt','2019 SH OpenInt','2020 SH OpenInt','2021 SH OpenInt',
                '2022 SH OpenInt','2023 SH OpenInt','SH OpenInt 5 yr Avg','SH OpenInt 10 yr Avg'],

        'y3b1':['2023 SH-K OpenInt Ratio','2022 SH-K OpenInt Ratio','SH-K OpenInt Ratio 5 yr Avg','SH-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SH-K OpenInt Ratio','2022 SH-K OpenInt Ratio','SH-K OpenInt Ratio 5 yr Avg','SH-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SH-K OpenInt Ratio','2019 SH-K OpenInt Ratio','2020 SH-K OpenInt Ratio','2021 SH-K OpenInt Ratio',
                '2022 SH-K OpenInt Ratio','2023 SH-K OpenInt Ratio','SH-K OpenInt Ratio 5 yr Avg','SH-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
   'SK-N': {
        'description':'Soybean May-Jul',
        'data': SK_N_df,
        'y1a1':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y2a1':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y3a1':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y1a2':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg','SMA10_SK-N_Close_5yr',
                'SMA20_SK-N_Close_5yr','SMA10_SK-N_Close_10yr','SMA20_SK-N_Close_10yr'],
        'y2a2':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg','SMA10_SK-N_Close_5yr',
                'SMA20_SK-N_Close_5yr','SMA10_SK-N_Close_10yr','SMA20_SK-N_Close_10yr'],
        'y3a2':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y1a3':['2018 SK-N CLOSE','2019 SK-N CLOSE','2020 SK-N CLOSE','2021 SK-N CLOSE',
                '2022 SK-N CLOSE','2023 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y2a3':['2018 SK-N CLOSE','2019 SK-N CLOSE','2020 SK-N CLOSE','2021 SK-N CLOSE',
                '2022 SK-N CLOSE','2023 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y3a3':['2018 SK-N CLOSE','2019 SK-N CLOSE','2020 SK-N CLOSE','2021 SK-N CLOSE',
                '2022 SK-N CLOSE','2023 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SK-N VOLUME','2022 SK-N VOLUME','SK-N VOLUME 5 yr Avg','SK-N VOLUME 10 yr Avg'],
        'y1b2':['2023 SK-N VOLUME','2022 SK-N VOLUME','SK-N VOLUME 5 yr Avg','SK-N VOLUME 10 yr Avg','SMA10_SK-N_Vol_5yr',
                'SMA20_SK-N_Vol_5yr','SMA10_SK-N_Vol_10yr','SMA20_SK-N_Vol_10yr'],
        'y1b3':['2018 SK-N VOLUME','2019 SK-N VOLUME','2020 SK-N VOLUME','2021 SK-N VOLUME',
                '2022 SK-N VOLUME','2023 SK-N VOLUME','SK-N VOLUME 5 yr Avg','SK-N VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SK OpenInt','2022 SK OpenInt','SK OpenInt 5 yr Avg','SK OpenInt 10 yr Avg'],
        'y2b2':['2023 SK OpenInt','2022 SK OpenInt','SK OpenInt 5 yr Avg','SK OpenInt 10 yr Avg','SMA10_SK_OpenInt_5yr',
                'SMA20_SK_OpenInt_5yr','SMA10_SK_OpenInt_10yr','SMA20_SK_OpenInt_10yr'],
        'y2b3':['2018 SK OpenInt','2019 SK OpenInt','2020 SK OpenInt','2021 SK OpenInt',
                '2022 SK OpenInt','2023 SK OpenInt','SK OpenInt 5 yr Avg','SK OpenInt 10 yr Avg'],

        'y3b1':['2023 SK-N OpenInt Ratio','2022 SK-N OpenInt Ratio','SK-N OpenInt Ratio 5 yr Avg','SK-N OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SK-N OpenInt Ratio','2022 SK-N OpenInt Ratio','SK-N OpenInt Ratio 5 yr Avg','SK-N OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SK-N OpenInt Ratio','2019 SK-N OpenInt Ratio','2020 SK-N OpenInt Ratio','2021 SK-N OpenInt Ratio',
                '2022 SK-N OpenInt Ratio','2023 SK-N OpenInt Ratio','SK-N OpenInt Ratio 5 yr Avg','SK-N OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'SN-Q': {
        'description':'Soybean Jul-Aug',
        'data': SN_Q_df,
        'y1a1':['2023 SN-Q CLOSE','2022 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg'],
        'y2a1':['2023 SN-Q CLOSE','2022 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg'],
        'y3a1':['2023 SN-Q CLOSE','2022 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg'],
        'y1a2':['2023 SN-Q CLOSE','2022 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg','SMA10_SN-Q_Close_5yr',
                'SMA20_SN-Q_Close_5yr','SMA10_SN-Q_Close_10yr','SMA20_SN-Q_Close_10yr'],
        'y2a2':['2023 SN-Q CLOSE','2022 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg','SMA10_SN-Q_Close_5yr',
                'SMA20_SN-Q_Close_5yr','SMA10_SN-Q_Close_10yr','SMA20_SN-Q_Close_10yr'],
        'y3a2':['2023 SN-Q CLOSE','2022 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg'],
        'y1a3':['2018 SN-Q CLOSE','2019 SN-Q CLOSE','2020 SN-Q CLOSE','2021 SN-Q CLOSE',
                '2022 SN-Q CLOSE','2023 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg'],
        'y2a3':['2018 SN-Q CLOSE','2019 SN-Q CLOSE','2020 SN-Q CLOSE','2021 SN-Q CLOSE',
                '2022 SN-Q CLOSE','2023 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg'],
        'y3a3':['2018 SN-Q CLOSE','2019 SN-Q CLOSE','2020 SN-Q CLOSE','2021 SN-Q CLOSE',
                '2022 SN-Q CLOSE','2023 SN-Q CLOSE','SN-Q CLOSE 5 yr Avg','SN-Q CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SN-Q VOLUME','2022 SN-Q VOLUME','SN-Q VOLUME 5 yr Avg','SN-Q VOLUME 10 yr Avg'],
        'y1b2':['2023 SN-Q VOLUME','2022 SN-Q VOLUME','SN-Q VOLUME 5 yr Avg','SN-Q VOLUME 10 yr Avg','SMA10_SN-Q_Vol_5yr',
                'SMA20_SN-Q_Vol_5yr','SMA10_SN-Q_Vol_10yr','SMA20_SN-Q_Vol_10yr'],
        'y1b3':['2018 SN-Q VOLUME','2019 SN-Q VOLUME','2020 SN-Q VOLUME','2021 SN-Q VOLUME',
                '2022 SN-Q VOLUME','2023 SN-Q VOLUME','SN-Q VOLUME 5 yr Avg','SN-Q VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SN OpenInt','2022 SN OpenInt','SN OpenInt 5 yr Avg','SN OpenInt 10 yr Avg'],
        'y2b2':['2023 SN OpenInt','2022 SN OpenInt','SN OpenInt 5 yr Avg','SN OpenInt 10 yr Avg','SMA10_SN_OpenInt_5yr',
                'SMA20_SN_OpenInt_5yr','SMA10_SN_OpenInt_10yr','SMA20_SN_OpenInt_10yr'],
        'y2b3':['2018 SN OpenInt','2019 SN OpenInt','2020 SN OpenInt','2021 SN OpenInt',
                '2022 SN OpenInt','2023 SN OpenInt','SN OpenInt 5 yr Avg','SN OpenInt 10 yr Avg'],

        'y3b1':['2023 SN-Q OpenInt Ratio','2022 SN-Q OpenInt Ratio','SN-Q OpenInt Ratio 5 yr Avg','SN-Q OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SN-Q OpenInt Ratio','2022 SN-Q OpenInt Ratio','SN-Q OpenInt Ratio 5 yr Avg','SN-Q OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SN-Q OpenInt Ratio','2019 SN-Q OpenInt Ratio','2020 SN-Q OpenInt Ratio','2021 SN-Q OpenInt Ratio',
                '2022 SN-Q OpenInt Ratio','2023 SN-Q OpenInt Ratio','SN-Q OpenInt Ratio 5 yr Avg','SN-Q OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },

       'SQ-U': {
        'description':'Soybean Aug-Sep',
        'data': SQ_U_df,
        'y1a1':['2023 SQ-U CLOSE','2022 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg'],
        'y2a1':['2023 SQ-U CLOSE','2022 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg'],
        'y3a1':['2023 SQ-U CLOSE','2022 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg'],
        'y1a2':['2023 SQ-U CLOSE','2022 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg','SMA10_SQ-U_Close_5yr',
                'SMA20_SQ-U_Close_5yr','SMA10_SQ-U_Close_10yr','SMA20_SQ-U_Close_10yr'],
        'y2a2':['2023 SQ-U CLOSE','2022 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg','SMA10_SQ-U_Close_5yr',
                'SMA20_SQ-U_Close_5yr','SMA10_SQ-U_Close_10yr','SMA20_SQ-U_Close_10yr'],
        'y3a2':['2023 SQ-U CLOSE','2022 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg'],
        'y1a3':['2018 SQ-U CLOSE','2019 SQ-U CLOSE','2020 SQ-U CLOSE','2021 SQ-U CLOSE',
                '2022 SQ-U CLOSE','2023 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg'],
        'y2a3':['2018 SQ-U CLOSE','2019 SQ-U CLOSE','2020 SQ-U CLOSE','2021 SQ-U CLOSE',
                '2022 SQ-U CLOSE','2023 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg'],
        'y3a3':['2018 SQ-U CLOSE','2019 SQ-U CLOSE','2020 SQ-U CLOSE','2021 SQ-U CLOSE',
                '2022 SQ-U CLOSE','2023 SQ-U CLOSE','SQ-U CLOSE 5 yr Avg','SQ-U CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SQ-U VOLUME','2022 SQ-U VOLUME','SQ-U VOLUME 5 yr Avg','SQ-U VOLUME 10 yr Avg'],
        'y1b2':['2023 SQ-U VOLUME','2022 SQ-U VOLUME','SQ-U VOLUME 5 yr Avg','SQ-U VOLUME 10 yr Avg','SMA10_SQ-U_Vol_5yr',
                'SMA20_SQ-U_Vol_5yr','SMA10_SQ-U_Vol_10yr','SMA20_SQ-U_Vol_10yr'],
        'y1b3':['2018 SQ-U VOLUME','2019 SQ-U VOLUME','2020 SQ-U VOLUME','2021 SQ-U VOLUME',
                '2022 SQ-U VOLUME','2023 SQ-U VOLUME','SQ-U VOLUME 5 yr Avg','SQ-U VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SQ OpenInt','2022 SQ OpenInt','SQ OpenInt 5 yr Avg','SQ OpenInt 10 yr Avg'],
        'y2b2':['2023 SQ OpenInt','2022 SQ OpenInt','SQ OpenInt 5 yr Avg','SQ OpenInt 10 yr Avg','SMA10_SQ_OpenInt_5yr',
                'SMA20_SQ_OpenInt_5yr','SMA10_SQ_OpenInt_10yr','SMA20_SQ_OpenInt_10yr'],
        'y2b3':['2018 SQ OpenInt','2019 SQ OpenInt','2020 SQ OpenInt','2021 SQ OpenInt',
                '2022 SQ OpenInt','2023 SQ OpenInt','SQ OpenInt 5 yr Avg','SQ OpenInt 10 yr Avg'],

        'y3b1':['2023 SQ-U OpenInt Ratio','2022 SQ-U OpenInt Ratio','SQ-U OpenInt Ratio 5 yr Avg','SQ-U OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SQ-U OpenInt Ratio','2022 SQ-U OpenInt Ratio','SQ-U OpenInt Ratio 5 yr Avg','SQ-U OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SQ-U OpenInt Ratio','2019 SQ-U OpenInt Ratio','2020 SQ-U OpenInt Ratio','2021 SQ-U OpenInt Ratio',
                '2022 SQ-U OpenInt Ratio','2023 SQ-U OpenInt Ratio','SQ-U OpenInt Ratio 5 yr Avg','SQ-U OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
     'SU-X': {
        'description':'Soybean Sep-Oct',
        'data': SU_X_df,
        'y1a1':['2023 SU-X CLOSE','2022 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg'],
        'y2a1':['2023 SU-X CLOSE','2022 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg'],
        'y3a1':['2023 SU-X CLOSE','2022 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg'],
        'y1a2':['2023 SU-X CLOSE','2022 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg','SMA10_SU-X_Close_5yr',
                'SMA20_SU-X_Close_5yr','SMA10_SU-X_Close_10yr','SMA20_SU-X_Close_10yr'],
        'y2a2':['2023 SU-X CLOSE','2022 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg','SMA10_SU-X_Close_5yr',
                'SMA20_SU-X_Close_5yr','SMA10_SU-X_Close_10yr','SMA20_SU-X_Close_10yr'],
        'y3a2':['2023 SU-X CLOSE','2022 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg'],
        'y1a3':['2018 SU-X CLOSE','2019 SU-X CLOSE','2020 SU-X CLOSE','2021 SU-X CLOSE',
                '2022 SU-X CLOSE','2023 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg'],
        'y2a3':['2018 SU-X CLOSE','2019 SU-X CLOSE','2020 SU-X CLOSE','2021 SU-X CLOSE',
                '2022 SU-X CLOSE','2023 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg'],
        'y3a3':['2018 SU-X CLOSE','2019 SU-X CLOSE','2020 SU-X CLOSE','2021 SU-X CLOSE',
                '2022 SU-X CLOSE','2023 SU-X CLOSE','SU-X CLOSE 5 yr Avg','SU-X CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SU-X VOLUME','2022 SU-X VOLUME','SU-X VOLUME 5 yr Avg','SU-X VOLUME 10 yr Avg'],
        'y1b2':['2023 SU-X VOLUME','2022 SU-X VOLUME','SU-X VOLUME 5 yr Avg','SU-X VOLUME 10 yr Avg','SMA10_SU-X_Vol_5yr',
                'SMA20_SU-X_Vol_5yr','SMA10_SU-X_Vol_10yr','SMA20_SU-X_Vol_10yr'],
        'y1b3':['2018 SU-X VOLUME','2019 SU-X VOLUME','2020 SU-X VOLUME','2021 SU-X VOLUME',
                '2022 SU-X VOLUME','2023 SU-X VOLUME','SU-X VOLUME 5 yr Avg','SU-X VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SU OpenInt','2022 SU OpenInt','SU OpenInt 5 yr Avg','SU OpenInt 10 yr Avg'],
        'y2b2':['2023 SU OpenInt','2022 SU OpenInt','SU OpenInt 5 yr Avg','SU OpenInt 10 yr Avg','SMA10_SU_OpenInt_5yr',
                'SMA20_SU_OpenInt_5yr','SMA10_SU_OpenInt_10yr','SMA20_SU_OpenInt_10yr'],
        'y2b3':['2018 SU OpenInt','2019 SU OpenInt','2020 SU OpenInt','2021 SU OpenInt',
                '2022 SU OpenInt','2023 SU OpenInt','SU OpenInt 5 yr Avg','SU OpenInt 10 yr Avg'],

        'y3b1':['2023 SU-X OpenInt Ratio','2022 SU-X OpenInt Ratio','SU-X OpenInt Ratio 5 yr Avg','SU-X OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SU-X OpenInt Ratio','2022 SU-X OpenInt Ratio','SU-X OpenInt Ratio 5 yr Avg','SU-X OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SU-X OpenInt Ratio','2019 SU-X OpenInt Ratio','2020 SU-X OpenInt Ratio','2021 SU-X OpenInt Ratio',
                '2022 SU-X OpenInt Ratio','2023 SU-X OpenInt Ratio','SU-X OpenInt Ratio 5 yr Avg','SU-X OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
     'SX-F': {
        'description':'Soybean Oct-Dec',
        'data': SX_F_df,
        'y1a1':['2023 SX-F CLOSE','2022 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg'],
        'y2a1':['2023 SX-F CLOSE','2022 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg'],
        'y3a1':['2023 SX-F CLOSE','2022 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg'],
        'y1a2':['2023 SX-F CLOSE','2022 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg','SMA10_SX-F_Close_5yr',
                'SMA20_SX-F_Close_5yr','SMA10_SX-F_Close_10yr','SMA20_SX-F_Close_10yr'],
        'y2a2':['2023 SX-F CLOSE','2022 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg','SMA10_SX-F_Close_5yr',
                'SMA20_SX-F_Close_5yr','SMA10_SX-F_Close_10yr','SMA20_SX-F_Close_10yr'],
        'y3a2':['2023 SX-F CLOSE','2022 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg'],
        'y1a3':['2018 SX-F CLOSE','2019 SX-F CLOSE','2020 SX-F CLOSE','2021 SX-F CLOSE',
                '2022 SX-F CLOSE','2023 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg'],
        'y2a3':['2018 SX-F CLOSE','2019 SX-F CLOSE','2020 SX-F CLOSE','2021 SX-F CLOSE',
                '2022 SX-F CLOSE','2023 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg'],
        'y3a3':['2018 SX-F CLOSE','2019 SX-F CLOSE','2020 SX-F CLOSE','2021 SX-F CLOSE',
                '2022 SX-F CLOSE','2023 SX-F CLOSE','SX-F CLOSE 5 yr Avg','SX-F CLOSE 10 yr Avg'],

        
        'y1b1':['2023 SX-F VOLUME','2022 SX-F VOLUME','SX-F VOLUME 5 yr Avg','SX-F VOLUME 10 yr Avg'],
        'y1b2':['2023 SX-F VOLUME','2022 SX-F VOLUME','SX-F VOLUME 5 yr Avg','SX-F VOLUME 10 yr Avg','SMA10_SX-F_Vol_5yr',
                'SMA20_SX-F_Vol_5yr','SMA10_SX-F_Vol_10yr','SMA20_SX-F_Vol_10yr'],
        'y1b3':['2018 SX-F VOLUME','2019 SX-F VOLUME','2020 SX-F VOLUME','2021 SX-F VOLUME',
                '2022 SX-F VOLUME','2023 SX-F VOLUME','SX-F VOLUME 5 yr Avg','SX-F VOLUME 10 yr Avg'],
        
        'y2b1':['2023 SX OpenInt','2022 SX OpenInt','SX OpenInt 5 yr Avg','SX OpenInt 10 yr Avg'],
        'y2b2':['2023 SX OpenInt','2022 SX OpenInt','SX OpenInt 5 yr Avg','SX OpenInt 10 yr Avg','SMA10_SX_OpenInt_5yr',
                'SMA20_SX_OpenInt_5yr','SMA10_SX_OpenInt_10yr','SMA20_SX_OpenInt_10yr'],
        'y2b3':['2018 SX OpenInt','2019 SX OpenInt','2020 SX OpenInt','2021 SX OpenInt',
                '2022 SX OpenInt','2023 SX OpenInt','SX OpenInt 5 yr Avg','SX OpenInt 10 yr Avg'],

        'y3b1':['2023 SX-F OpenInt Ratio','2022 SX-F OpenInt Ratio','SX-F OpenInt Ratio 5 yr Avg','SX-F OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 SX-F OpenInt Ratio','2022 SX-F OpenInt Ratio','SX-F OpenInt Ratio 5 yr Avg','SX-F OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 SX-F OpenInt Ratio','2019 SX-F OpenInt Ratio','2020 SX-F OpenInt Ratio','2021 SX-F OpenInt Ratio',
                '2022 SX-F OpenInt Ratio','2023 SX-F OpenInt Ratio','SX-F OpenInt Ratio 5 yr Avg','SX-F OpenInt Ratio 10 yr Avg'],

        
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
    ('SF-H','SH-K','SK-N','SN-Q','SQ-U','SU-X','SX-F'))

    st.write('Selected Spread:', Soybean_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=Soybean_spreads[spread]['y1a1']
    y1b=Soybean_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=Soybean_spreads[spread]['y1a2']
    y1b=Soybean_spreads[spread]['y1b2']

    
else:
    y1a=Soybean_spreads[spread]['y1a3']
    y1b=Soybean_spreads[spread]['y1b3']
    
fig = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

Subfig.add_traces(fig.data + fig2.data)
Subfig.layout.xaxis.title="Date"
Subfig.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig.layout.yaxis2.title="Spread Volume"
Subfig.layout.title=titletxt

Subfig.update_layout(
    title = Soybean_spreads[spread]['description']+"  Spread Price Vs Volume",
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
    y2a=Soybean_spreads[spread]['y2a1']
    y2b=Soybean_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=Soybean_spreads[spread]['y2a2']
    y2b=Soybean_spreads[spread]['y2b2']
    
    
else:
    y2a=Soybean_spreads[spread]['y2a3']
    y2b=Soybean_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
Subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

Subfig1.add_traces(fig1.data + fig12.data)
Subfig1.layout.xaxis.title="Date"
Subfig1.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig1.layout.yaxis2.title="Open Interest"
Subfig1.layout.title=titletxt1

Subfig1.update_layout(
    title = Soybean_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    y3a=Soybean_spreads[spread]['y3a1']
    y3b=Soybean_spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=Soybean_spreads[spread]['y3a2']
    y3b=Soybean_spreads[spread]['y3b2']
    
    
else:
    y3a=Soybean_spreads[spread]['y3a3']
    y3b=Soybean_spreads[spread]['y3b3']

titletxt3='Price & Open Interest Ratio'
Subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y3a, title=titletxt3)
fig12 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y3b, title=titletxt3)



fig12.update_traces(yaxis="y2")

Subfig2.add_traces(fig1.data + fig12.data)
Subfig2.layout.xaxis.title="Date"
Subfig2.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig2.layout.yaxis2.title="Open Interest Ratio"
Subfig2.layout.title=titletxt3

Subfig2.update_layout(
    title = Soybean_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    
    

     



