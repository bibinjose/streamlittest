"""
#App to find patterns in RBOB spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
color_selected=px.colors.qualitative.Alphabet
st.set_page_config(page_title=" RBOB Spreads ",layout="wide")


#specific spreads

RBF_J_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBF-J')
RBG_K_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBG-K')
RBF_K_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBF-K')
RBG_J_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBG-J')


#Regular Spreads
RBF_G_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBF-G')
RBG_H_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBG-H')
RBH_J_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBH-J')
RBJ_K_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBJ-K')
RBK_M_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBK-M')
RBM_N_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBM-N')
RBN_Q_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBN-Q')
RBQ_U_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBQ-U')
RBU_V_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBU-V')
RBV_X_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBV-X')
RBX_Z_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBX-Z')
RBZ_F_df=pd.read_excel("rbob_spread.xlsx",sheet_name='RBZ-F')



RBOB_Spreads = { 
    'RBF-J': {
        'description':'RBOB Jan-Apr',
        'data': RBF_J_df,
        'y1a1':['2023 RBF-J CLOSE','2022 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg'],
        'y2a1':['2023 RBF-J CLOSE','2022 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg'],
        'y3a1':['2023 RBF-J CLOSE','2022 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg'],
        'y1a2':['2023 RBF-J CLOSE','2022 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg','SMA10_RBF-J_Close_5yr',
                'SMA20_RBF-J_Close_5yr','SMA10_RBF-J_Close_10yr','SMA20_RBF-J_Close_10yr'],
        'y2a2':['2023 RBF-J CLOSE','2022 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg','SMA10_RBF-J_Close_5yr',
                'SMA20_RBF-J_Close_5yr','SMA10_RBF-J_Close_10yr','SMA20_RBF-J_Close_10yr'],
        'y3a2':['2023 RBF-J CLOSE','2022 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg'],
        'y1a3':['2018 RBF-J CLOSE','2019 RBF-J CLOSE','2020 RBF-J CLOSE','2021 RBF-J CLOSE',
                '2022 RBF-J CLOSE','2023 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg'],
        'y2a3':['2018 RBF-J CLOSE','2019 RBF-J CLOSE','2020 RBF-J CLOSE','2021 RBF-J CLOSE',
                '2022 RBF-J CLOSE','2023 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg'],
        'y3a3':['2018 RBF-J CLOSE','2019 RBF-J CLOSE','2020 RBF-J CLOSE','2021 RBF-J CLOSE',
                '2022 RBF-J CLOSE','2023 RBF-J CLOSE','RBF-J CLOSE 5 yr Avg','RBF-J CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBF-J VOLUME','2022 RBF-J VOLUME','RBF-J VOLUME 5 yr Avg','RBF-J VOLUME 10 yr Avg'],
        'y1b2':['2023 RBF-J VOLUME','2022 RBF-J VOLUME','RBF-J VOLUME 5 yr Avg','RBF-J VOLUME 10 yr Avg','SMA10_RBF-J_Vol_5yr',
                'SMA20_RBF-J_Vol_5yr','SMA10_RBF-J_Vol_10yr','SMA20_RBF-J_Vol_10yr'],
        'y1b3':['2018 RBF-J VOLUME','2019 RBF-J VOLUME','2020 RBF-J VOLUME','2021 RBF-J VOLUME',
                '2022 RBF-J VOLUME','2023 RBF-J VOLUME','RBF-J VOLUME 5 yr Avg','RBF-J VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg'],
        'y2b2':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg','SMA10_RBF_OpenInt_5yr',
                'SMA20_RBF_OpenInt_5yr','SMA10_RBF_OpenInt_10yr','SMA20_RBF_OpenInt_10yr'],
        'y2b3':['2018 RBF OpenInt','2019 RBF OpenInt','2020 RBF OpenInt','2021 RBF OpenInt',
                '2022 RBF OpenInt','2023 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg'],

        'y3b1':['2023 RBF-J OpenInt Ratio','2022 RBF-J OpenInt Ratio','RBF-J OpenInt Ratio 5 yr Avg','RBF-J OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBF-J OpenInt Ratio','2022 RBF-J OpenInt Ratio','RBF-J OpenInt Ratio 5 yr Avg','RBF-J OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBF-J OpenInt Ratio','2019 RBF-J OpenInt Ratio','2020 RBF-J OpenInt Ratio','2021 RBF-J OpenInt Ratio',
                '2022 RBF-J OpenInt Ratio','2023 RBF-J OpenInt Ratio','RBF-J OpenInt Ratio 5 yr Avg','RBF-J OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'RBG-K': {
        'description':'RBOB Feb-May',
        'data': RBG_K_df,
        'y1a1':['2023 RBG-K CLOSE','2022 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg'],
        'y2a1':['2023 RBG-K CLOSE','2022 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg'],
        'y3a1':['2023 RBG-K CLOSE','2022 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg'],
        'y1a2':['2023 RBG-K CLOSE','2022 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg','SMA10_RBG-K_Close_5yr',
                'SMA20_RBG-K_Close_5yr','SMA10_RBG-K_Close_10yr','SMA20_RBG-K_Close_10yr'],
        'y2a2':['2023 RBG-K CLOSE','2022 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg','SMA10_RBG-K_Close_5yr',
                'SMA20_RBG-K_Close_5yr','SMA10_RBG-K_Close_10yr','SMA20_RBG-K_Close_10yr'],
        'y3a2':['2023 RBG-K CLOSE','2022 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg'],
        'y1a3':['2018 RBG-K CLOSE','2019 RBG-K CLOSE','2020 RBG-K CLOSE','2021 RBG-K CLOSE',
                '2022 RBG-K CLOSE','2023 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg'],
        'y2a3':['2018 RBG-K CLOSE','2019 RBG-K CLOSE','2020 RBG-K CLOSE','2021 RBG-K CLOSE',
                '2022 RBG-K CLOSE','2023 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg'],
        'y3a3':['2018 RBG-K CLOSE','2019 RBG-K CLOSE','2020 RBG-K CLOSE','2021 RBG-K CLOSE',
                '2022 RBG-K CLOSE','2023 RBG-K CLOSE','RBG-K CLOSE 5 yr Avg','RBG-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBG-K VOLUME','2022 RBG-K VOLUME','RBG-K VOLUME 5 yr Avg','RBG-K VOLUME 10 yr Avg'],
        'y1b2':['2023 RBG-K VOLUME','2022 RBG-K VOLUME','RBG-K VOLUME 5 yr Avg','RBG-K VOLUME 10 yr Avg','SMA10_RBG-K_Vol_5yr',
                'SMA20_RBG-K_Vol_5yr','SMA10_RBG-K_Vol_10yr','SMA20_RBG-K_Vol_10yr'],
        'y1b3':['2018 RBG-K VOLUME','2019 RBG-K VOLUME','2020 RBG-K VOLUME','2021 RBG-K VOLUME',
                '2022 RBG-K VOLUME','2023 RBG-K VOLUME','RBG-K VOLUME 5 yr Avg','RBG-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg'],
        'y2b2':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg','SMA10_RBG_OpenInt_5yr',
                'SMA20_RBG_OpenInt_5yr','SMA10_RBG_OpenInt_10yr','SMA20_RBG_OpenInt_10yr'],
        'y2b3':['2018 RBG OpenInt','2019 RBG OpenInt','2020 RBG OpenInt','2021 RBG OpenInt',
                '2022 RBG OpenInt','2023 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg'],

        'y3b1':['2023 RBG-K OpenInt Ratio','2022 RBG-K OpenInt Ratio','RBG-K OpenInt Ratio 5 yr Avg','RBG-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBG-K OpenInt Ratio','2022 RBG-K OpenInt Ratio','RBG-K OpenInt Ratio 5 yr Avg','RBG-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBG-K OpenInt Ratio','2019 RBG-K OpenInt Ratio','2020 RBG-K OpenInt Ratio','2021 RBG-K OpenInt Ratio',
                '2022 RBG-K OpenInt Ratio','2023 RBG-K OpenInt Ratio','RBG-K OpenInt Ratio 5 yr Avg','RBG-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBF-K': {
        'description':'RBOB Jan-May',
        'data': RBF_K_df,
        'y1a1':['2023 RBF-K CLOSE','2022 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg'],
        'y2a1':['2023 RBF-K CLOSE','2022 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg'],
        'y3a1':['2023 RBF-K CLOSE','2022 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg'],
        'y1a2':['2023 RBF-K CLOSE','2022 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg','SMA10_RBF-K_Close_5yr',
                'SMA20_RBF-K_Close_5yr','SMA10_RBF-K_Close_10yr','SMA20_RBF-K_Close_10yr'],
        'y2a2':['2023 RBF-K CLOSE','2022 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg','SMA10_RBF-K_Close_5yr',
                'SMA20_RBF-K_Close_5yr','SMA10_RBF-K_Close_10yr','SMA20_RBF-K_Close_10yr'],
        'y3a2':['2023 RBF-K CLOSE','2022 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg'],
        'y1a3':['2018 RBF-K CLOSE','2019 RBF-K CLOSE','2020 RBF-K CLOSE','2021 RBF-K CLOSE',
                '2022 RBF-K CLOSE','2023 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg'],
        'y2a3':['2018 RBF-K CLOSE','2019 RBF-K CLOSE','2020 RBF-K CLOSE','2021 RBF-K CLOSE',
                '2022 RBF-K CLOSE','2023 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg'],
        'y3a3':['2018 RBF-K CLOSE','2019 RBF-K CLOSE','2020 RBF-K CLOSE','2021 RBF-K CLOSE',
                '2022 RBF-K CLOSE','2023 RBF-K CLOSE','RBF-K CLOSE 5 yr Avg','RBF-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBF-K VOLUME','2022 RBF-K VOLUME','RBF-K VOLUME 5 yr Avg','RBF-K VOLUME 10 yr Avg'],
        'y1b2':['2023 RBF-K VOLUME','2022 RBF-K VOLUME','RBF-K VOLUME 5 yr Avg','RBF-K VOLUME 10 yr Avg','SMA10_RBF-K_Vol_5yr',
                'SMA20_RBF-K_Vol_5yr','SMA10_RBF-K_Vol_10yr','SMA20_RBF-K_Vol_10yr'],
        'y1b3':['2018 RBF-K VOLUME','2019 RBF-K VOLUME','2020 RBF-K VOLUME','2021 RBF-K VOLUME',
                '2022 RBF-K VOLUME','2023 RBF-K VOLUME','RBF-K VOLUME 5 yr Avg','RBF-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg'],
        'y2b2':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg','SMA10_RBF_OpenInt_5yr',
                'SMA20_RBF_OpenInt_5yr','SMA10_RBF_OpenInt_10yr','SMA20_RBF_OpenInt_10yr'],
        'y2b3':['2018 RBF OpenInt','2019 RBF OpenInt','2020 RBF OpenInt','2021 RBF OpenInt',
                '2022 RBF OpenInt','2023 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg'],

        'y3b1':['2023 RBF-K OpenInt Ratio','2022 RBF-K OpenInt Ratio','RBF-K OpenInt Ratio 5 yr Avg','RBF-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBF-K OpenInt Ratio','2022 RBF-K OpenInt Ratio','RBF-K OpenInt Ratio 5 yr Avg','RBF-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBF-K OpenInt Ratio','2019 RBF-K OpenInt Ratio','2020 RBF-K OpenInt Ratio','2021 RBF-K OpenInt Ratio',
                '2022 RBF-K OpenInt Ratio','2023 RBF-K OpenInt Ratio','RBF-K OpenInt Ratio 5 yr Avg','RBF-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBG-J': {
        'description':'RBOB Feb-Apr',
        'data': RBG_J_df,
        'y1a1':['2023 RBG-J CLOSE','2022 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg'],
        'y2a1':['2023 RBG-J CLOSE','2022 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg'],
        'y3a1':['2023 RBG-J CLOSE','2022 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg'],
        'y1a2':['2023 RBG-J CLOSE','2022 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg','SMA10_RBG-J_Close_5yr',
                'SMA20_RBG-J_Close_5yr','SMA10_RBG-J_Close_10yr','SMA20_RBG-J_Close_10yr'],
        'y2a2':['2023 RBG-J CLOSE','2022 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg','SMA10_RBG-J_Close_5yr',
                'SMA20_RBG-J_Close_5yr','SMA10_RBG-J_Close_10yr','SMA20_RBG-J_Close_10yr'],
        'y3a2':['2023 RBG-J CLOSE','2022 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg'],
        'y1a3':['2018 RBG-J CLOSE','2019 RBG-J CLOSE','2020 RBG-J CLOSE','2021 RBG-J CLOSE',
                '2022 RBG-J CLOSE','2023 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg'],
        'y2a3':['2018 RBG-J CLOSE','2019 RBG-J CLOSE','2020 RBG-J CLOSE','2021 RBG-J CLOSE',
                '2022 RBG-J CLOSE','2023 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg'],
        'y3a3':['2018 RBG-J CLOSE','2019 RBG-J CLOSE','2020 RBG-J CLOSE','2021 RBG-J CLOSE',
                '2022 RBG-J CLOSE','2023 RBG-J CLOSE','RBG-J CLOSE 5 yr Avg','RBG-J CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBG-J VOLUME','2022 RBG-J VOLUME','RBG-J VOLUME 5 yr Avg','RBG-J VOLUME 10 yr Avg'],
        'y1b2':['2023 RBG-J VOLUME','2022 RBG-J VOLUME','RBG-J VOLUME 5 yr Avg','RBG-J VOLUME 10 yr Avg','SMA10_RBG-J_Vol_5yr',
                'SMA20_RBG-J_Vol_5yr','SMA10_RBG-J_Vol_10yr','SMA20_RBG-J_Vol_10yr'],
        'y1b3':['2018 RBG-J VOLUME','2019 RBG-J VOLUME','2020 RBG-J VOLUME','2021 RBG-J VOLUME',
                '2022 RBG-J VOLUME','2023 RBG-J VOLUME','RBG-J VOLUME 5 yr Avg','RBG-J VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg'],
        'y2b2':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg','SMA10_RBG_OpenInt_5yr',
                'SMA20_RBG_OpenInt_5yr','SMA10_RBG_OpenInt_10yr','SMA20_RBG_OpenInt_10yr'],
        'y2b3':['2018 RBG OpenInt','2019 RBG OpenInt','2020 RBG OpenInt','2021 RBG OpenInt',
                '2022 RBG OpenInt','2023 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg'],

        'y3b1':['2023 RBG-J OpenInt Ratio','2022 RBG-J OpenInt Ratio','RBG-J OpenInt Ratio 5 yr Avg','RBG-J OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBG-J OpenInt Ratio','2022 RBG-J OpenInt Ratio','RBG-J OpenInt Ratio 5 yr Avg','RBG-J OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBG-J OpenInt Ratio','2019 RBG-J OpenInt Ratio','2020 RBG-J OpenInt Ratio','2021 RBG-J OpenInt Ratio',
                '2022 RBG-J OpenInt Ratio','2023 RBG-J OpenInt Ratio','RBG-J OpenInt Ratio 5 yr Avg','RBG-J OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBF-G': {
        'description':'RBOB Jan-Feb',
        'data': RBF_G_df,
        'y1a1':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y2a1':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y3a1':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y1a2':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg','SMA10_RBF-G_Close_5yr',
                'SMA20_RBF-G_Close_5yr','SMA10_RBF-G_Close_10yr','SMA20_RBF-G_Close_10yr'],
        'y2a2':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg','SMA10_RBF-G_Close_5yr',
                'SMA20_RBF-G_Close_5yr','SMA10_RBF-G_Close_10yr','SMA20_RBF-G_Close_10yr'],
        'y3a2':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y1a3':['2018 RBF-G CLOSE','2019 RBF-G CLOSE','2020 RBF-G CLOSE','2021 RBF-G CLOSE',
                '2022 RBF-G CLOSE','2023 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y2a3':['2018 RBF-G CLOSE','2019 RBF-G CLOSE','2020 RBF-G CLOSE','2021 RBF-G CLOSE',
                '2022 RBF-G CLOSE','2023 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y3a3':['2018 RBF-G CLOSE','2019 RBF-G CLOSE','2020 RBF-G CLOSE','2021 RBF-G CLOSE',
                '2022 RBF-G CLOSE','2023 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBF-G VOLUME','2022 RBF-G VOLUME','RBF-G VOLUME 5 yr Avg','RBF-G VOLUME 10 yr Avg'],
        'y1b2':['2023 RBF-G VOLUME','2022 RBF-G VOLUME','RBF-G VOLUME 5 yr Avg','RBF-G VOLUME 10 yr Avg','SMA10_RBF-G_Vol_5yr',
                'SMA20_RBF-G_Vol_5yr','SMA10_RBF-G_Vol_10yr','SMA20_RBF-G_Vol_10yr'],
        'y1b3':['2018 RBF-G VOLUME','2019 RBF-G VOLUME','2020 RBF-G VOLUME','2021 RBF-G VOLUME',
                '2022 RBF-G VOLUME','2023 RBF-G VOLUME','RBF-G VOLUME 5 yr Avg','RBF-G VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg'],
        'y2b2':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg','SMA10_RBF_OpenInt_5yr',
                'SMA20_RBF_OpenInt_5yr','SMA10_RBF_OpenInt_10yr','SMA20_RBF_OpenInt_10yr'],
        'y2b3':['2018 RBF OpenInt','2019 RBF OpenInt','2020 RBF OpenInt','2021 RBF OpenInt',
                '2022 RBF OpenInt','2023 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg'],

        'y3b1':['2023 RBF-G OpenInt Ratio','2022 RBF-G OpenInt Ratio','RBF-G OpenInt Ratio 5 yr Avg','RBF-G OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBF-G OpenInt Ratio','2022 RBF-G OpenInt Ratio','RBF-G OpenInt Ratio 5 yr Avg','RBF-G OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBF-G OpenInt Ratio','2019 RBF-G OpenInt Ratio','2020 RBF-G OpenInt Ratio','2021 RBF-G OpenInt Ratio',
                '2022 RBF-G OpenInt Ratio','2023 RBF-G OpenInt Ratio','RBF-G OpenInt Ratio 5 yr Avg','RBF-G OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBG-H': {
        'description':'RBOB Feb-Mar',
        'data': RBG_H_df,
        'y1a1':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y2a1':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y3a1':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y1a2':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg','SMA10_RBG-H_Close_5yr',
                'SMA20_RBG-H_Close_5yr','SMA10_RBG-H_Close_10yr','SMA20_RBG-H_Close_10yr'],
        'y2a2':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg','SMA10_RBG-H_Close_5yr',
                'SMA20_RBG-H_Close_5yr','SMA10_RBG-H_Close_10yr','SMA20_RBG-H_Close_10yr'],
        'y3a2':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y1a3':['2018 RBG-H CLOSE','2019 RBG-H CLOSE','2020 RBG-H CLOSE','2021 RBG-H CLOSE',
                '2022 RBG-H CLOSE','2023 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y2a3':['2018 RBG-H CLOSE','2019 RBG-H CLOSE','2020 RBG-H CLOSE','2021 RBG-H CLOSE',
                '2022 RBG-H CLOSE','2023 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y3a3':['2018 RBG-H CLOSE','2019 RBG-H CLOSE','2020 RBG-H CLOSE','2021 RBG-H CLOSE',
                '2022 RBG-H CLOSE','2023 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBG-H VOLUME','2022 RBG-H VOLUME','RBG-H VOLUME 5 yr Avg','RBG-H VOLUME 10 yr Avg'],
        'y1b2':['2023 RBG-H VOLUME','2022 RBG-H VOLUME','RBG-H VOLUME 5 yr Avg','RBG-H VOLUME 10 yr Avg','SMA10_RBG-H_Vol_5yr',
                'SMA20_RBG-H_Vol_5yr','SMA10_RBG-H_Vol_10yr','SMA20_RBG-H_Vol_10yr'],
        'y1b3':['2018 RBG-H VOLUME','2019 RBG-H VOLUME','2020 RBG-H VOLUME','2021 RBG-H VOLUME',
                '2022 RBG-H VOLUME','2023 RBG-H VOLUME','RBG-H VOLUME 5 yr Avg','RBG-H VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg'],
        'y2b2':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg','SMA10_RBG_OpenInt_5yr',
                'SMA20_RBG_OpenInt_5yr','SMA10_RBG_OpenInt_10yr','SMA20_RBG_OpenInt_10yr'],
        'y2b3':['2018 RBG OpenInt','2019 RBG OpenInt','2020 RBG OpenInt','2021 RBG OpenInt',
                '2022 RBG OpenInt','2023 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg'],

        'y3b1':['2023 RBG-H OpenInt Ratio','2022 RBG-H OpenInt Ratio','RBG-H OpenInt Ratio 5 yr Avg','RBG-H OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBG-H OpenInt Ratio','2022 RBG-H OpenInt Ratio','RBG-H OpenInt Ratio 5 yr Avg','RBG-H OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBG-H OpenInt Ratio','2019 RBG-H OpenInt Ratio','2020 RBG-H OpenInt Ratio','2021 RBG-H OpenInt Ratio',
                '2022 RBG-H OpenInt Ratio','2023 RBG-H OpenInt Ratio','RBG-H OpenInt Ratio 5 yr Avg','RBG-H OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBH-J': {
        'description':'RBOB Mar-Apr',
        'data': RBH_J_df,
        'y1a1':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y2a1':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y3a1':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y1a2':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg','SMA10_RBH-J_Close_5yr',
                'SMA20_RBH-J_Close_5yr','SMA10_RBH-J_Close_10yr','SMA20_RBH-J_Close_10yr'],
        'y2a2':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg','SMA10_RBH-J_Close_5yr',
                'SMA20_RBH-J_Close_5yr','SMA10_RBH-J_Close_10yr','SMA20_RBH-J_Close_10yr'],
        'y3a2':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y1a3':['2018 RBH-J CLOSE','2019 RBH-J CLOSE','2020 RBH-J CLOSE','2021 RBH-J CLOSE',
                '2022 RBH-J CLOSE','2023 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y2a3':['2018 RBH-J CLOSE','2019 RBH-J CLOSE','2020 RBH-J CLOSE','2021 RBH-J CLOSE',
                '2022 RBH-J CLOSE','2023 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y3a3':['2018 RBH-J CLOSE','2019 RBH-J CLOSE','2020 RBH-J CLOSE','2021 RBH-J CLOSE',
                '2022 RBH-J CLOSE','2023 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBH-J VOLUME','2022 RBH-J VOLUME','RBH-J VOLUME 5 yr Avg','RBH-J VOLUME 10 yr Avg'],
        'y1b2':['2023 RBH-J VOLUME','2022 RBH-J VOLUME','RBH-J VOLUME 5 yr Avg','RBH-J VOLUME 10 yr Avg','SMA10_RBH-J_Vol_5yr',
                'SMA20_RBH-J_Vol_5yr','SMA10_RBH-J_Vol_10yr','SMA20_RBH-J_Vol_10yr'],
        'y1b3':['2018 RBH-J VOLUME','2019 RBH-J VOLUME','2020 RBH-J VOLUME','2021 RBH-J VOLUME',
                '2022 RBH-J VOLUME','2023 RBH-J VOLUME','RBH-J VOLUME 5 yr Avg','RBH-J VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBH OpenInt','2022 RBH OpenInt','RBH OpenInt 5 yr Avg','RBH OpenInt 10 yr Avg'],
        'y2b2':['2023 RBH OpenInt','2022 RBH OpenInt','RBH OpenInt 5 yr Avg','RBH OpenInt 10 yr Avg','SMA10_RBH_OpenInt_5yr',
                'SMA20_RBH_OpenInt_5yr','SMA10_RBH_OpenInt_10yr','SMA20_RBH_OpenInt_10yr'],
        'y2b3':['2018 RBH OpenInt','2019 RBH OpenInt','2020 RBH OpenInt','2021 RBH OpenInt',
                '2022 RBH OpenInt','2023 RBH OpenInt','RBH OpenInt 5 yr Avg','RBH OpenInt 10 yr Avg'],

        'y3b1':['2023 RBH-J OpenInt Ratio','2022 RBH-J OpenInt Ratio','RBH-J OpenInt Ratio 5 yr Avg','RBH-J OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBH-J OpenInt Ratio','2022 RBH-J OpenInt Ratio','RBH-J OpenInt Ratio 5 yr Avg','RBH-J OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBH-J OpenInt Ratio','2019 RBH-J OpenInt Ratio','2020 RBH-J OpenInt Ratio','2021 RBH-J OpenInt Ratio',
                '2022 RBH-J OpenInt Ratio','2023 RBH-J OpenInt Ratio','RBH-J OpenInt Ratio 5 yr Avg','RBH-J OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    
    'RBJ-K': {
        'description':'RBOB Apr-May',
        'data': RBJ_K_df,
        'y1a1':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y2a1':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y3a1':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y1a2':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg','SMA10_RBJ-K_Close_5yr',
                'SMA20_RBJ-K_Close_5yr','SMA10_RBJ-K_Close_10yr','SMA20_RBJ-K_Close_10yr'],
        'y2a2':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg','SMA10_RBJ-K_Close_5yr',
                'SMA20_RBJ-K_Close_5yr','SMA10_RBJ-K_Close_10yr','SMA20_RBJ-K_Close_10yr'],
        'y3a2':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y1a3':['2018 RBJ-K CLOSE','2019 RBJ-K CLOSE','2020 RBJ-K CLOSE','2021 RBJ-K CLOSE',
                '2022 RBJ-K CLOSE','2023 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y2a3':['2018 RBJ-K CLOSE','2019 RBJ-K CLOSE','2020 RBJ-K CLOSE','2021 RBJ-K CLOSE',
                '2022 RBJ-K CLOSE','2023 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y3a3':['2018 RBJ-K CLOSE','2019 RBJ-K CLOSE','2020 RBJ-K CLOSE','2021 RBJ-K CLOSE',
                '2022 RBJ-K CLOSE','2023 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBJ-K VOLUME','2022 RBJ-K VOLUME','RBJ-K VOLUME 5 yr Avg','RBJ-K VOLUME 10 yr Avg'],
        'y1b2':['2023 RBJ-K VOLUME','2022 RBJ-K VOLUME','RBJ-K VOLUME 5 yr Avg','RBJ-K VOLUME 10 yr Avg','SMA10_RBJ-K_Vol_5yr',
                'SMA20_RBJ-K_Vol_5yr','SMA10_RBJ-K_Vol_10yr','SMA20_RBJ-K_Vol_10yr'],
        'y1b3':['2018 RBJ-K VOLUME','2019 RBJ-K VOLUME','2020 RBJ-K VOLUME','2021 RBJ-K VOLUME',
                '2022 RBJ-K VOLUME','2023 RBJ-K VOLUME','RBJ-K VOLUME 5 yr Avg','RBJ-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBJ OpenInt','2022 RBJ OpenInt','RBJ OpenInt 5 yr Avg','RBJ OpenInt 10 yr Avg'],
        'y2b2':['2023 RBJ OpenInt','2022 RBJ OpenInt','RBJ OpenInt 5 yr Avg','RBJ OpenInt 10 yr Avg','SMA10_RBJ_OpenInt_5yr',
                'SMA20_RBJ_OpenInt_5yr','SMA10_RBJ_OpenInt_10yr','SMA20_RBJ_OpenInt_10yr'],
        'y2b3':['2018 RBJ OpenInt','2019 RBJ OpenInt','2020 RBJ OpenInt','2021 RBJ OpenInt',
                '2022 RBJ OpenInt','2023 RBJ OpenInt','RBJ OpenInt 5 yr Avg','RBJ OpenInt 10 yr Avg'],

        'y3b1':['2023 RBJ-K OpenInt Ratio','2022 RBJ-K OpenInt Ratio','RBJ-K OpenInt Ratio 5 yr Avg','RBJ-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBJ-K OpenInt Ratio','2022 RBJ-K OpenInt Ratio','RBJ-K OpenInt Ratio 5 yr Avg','RBJ-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBJ-K OpenInt Ratio','2019 RBJ-K OpenInt Ratio','2020 RBJ-K OpenInt Ratio','2021 RBJ-K OpenInt Ratio',
                '2022 RBJ-K OpenInt Ratio','2023 RBJ-K OpenInt Ratio','RBJ-K OpenInt Ratio 5 yr Avg','RBJ-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBK-M': {
        'description':'RBOB May-Jun',
        'data': RBK_M_df,
        'y1a1':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y2a1':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y3a1':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y1a2':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg','SMA10_RBK-M_Close_5yr',
                'SMA20_RBK-M_Close_5yr','SMA10_RBK-M_Close_10yr','SMA20_RBK-M_Close_10yr'],
        'y2a2':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg','SMA10_RBK-M_Close_5yr',
                'SMA20_RBK-M_Close_5yr','SMA10_RBK-M_Close_10yr','SMA20_RBK-M_Close_10yr'],
        'y3a2':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y1a3':['2018 RBK-M CLOSE','2019 RBK-M CLOSE','2020 RBK-M CLOSE','2021 RBK-M CLOSE',
                '2022 RBK-M CLOSE','2023 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y2a3':['2018 RBK-M CLOSE','2019 RBK-M CLOSE','2020 RBK-M CLOSE','2021 RBK-M CLOSE',
                '2022 RBK-M CLOSE','2023 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y3a3':['2018 RBK-M CLOSE','2019 RBK-M CLOSE','2020 RBK-M CLOSE','2021 RBK-M CLOSE',
                '2022 RBK-M CLOSE','2023 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBK-M VOLUME','2022 RBK-M VOLUME','RBK-M VOLUME 5 yr Avg','RBK-M VOLUME 10 yr Avg'],
        'y1b2':['2023 RBK-M VOLUME','2022 RBK-M VOLUME','RBK-M VOLUME 5 yr Avg','RBK-M VOLUME 10 yr Avg','SMA10_RBK-M_Vol_5yr',
                'SMA20_RBK-M_Vol_5yr','SMA10_RBK-M_Vol_10yr','SMA20_RBK-M_Vol_10yr'],
        'y1b3':['2018 RBK-M VOLUME','2019 RBK-M VOLUME','2020 RBK-M VOLUME','2021 RBK-M VOLUME',
                '2022 RBK-M VOLUME','2023 RBK-M VOLUME','RBK-M VOLUME 5 yr Avg','RBK-M VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBK OpenInt','2022 RBK OpenInt','RBK OpenInt 5 yr Avg','RBK OpenInt 10 yr Avg'],
        'y2b2':['2023 RBK OpenInt','2022 RBK OpenInt','RBK OpenInt 5 yr Avg','RBK OpenInt 10 yr Avg','SMA10_RBK_OpenInt_5yr',
                'SMA20_RBK_OpenInt_5yr','SMA10_RBK_OpenInt_10yr','SMA20_RBK_OpenInt_10yr'],
        'y2b3':['2018 RBK OpenInt','2019 RBK OpenInt','2020 RBK OpenInt','2021 RBK OpenInt',
                '2022 RBK OpenInt','2023 RBK OpenInt','RBK OpenInt 5 yr Avg','RBK OpenInt 10 yr Avg'],

        'y3b1':['2023 RBK-M OpenInt Ratio','2022 RBK-M OpenInt Ratio','RBK-M OpenInt Ratio 5 yr Avg','RBK-M OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBK-M OpenInt Ratio','2022 RBK-M OpenInt Ratio','RBK-M OpenInt Ratio 5 yr Avg','RBK-M OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBK-M OpenInt Ratio','2019 RBK-M OpenInt Ratio','2020 RBK-M OpenInt Ratio','2021 RBK-M OpenInt Ratio',
                '2022 RBK-M OpenInt Ratio','2023 RBK-M OpenInt Ratio','RBK-M OpenInt Ratio 5 yr Avg','RBK-M OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBM-N': {
        'description':'RBOB Jun-Jul',
        'data': RBM_N_df,
        'y1a1':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y2a1':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y3a1':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y1a2':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg','SMA10_RBM-N_Close_5yr',
                'SMA20_RBM-N_Close_5yr','SMA10_RBM-N_Close_10yr','SMA20_RBM-N_Close_10yr'],
        'y2a2':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg','SMA10_RBM-N_Close_5yr',
                'SMA20_RBM-N_Close_5yr','SMA10_RBM-N_Close_10yr','SMA20_RBM-N_Close_10yr'],
        'y3a2':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y1a3':['2018 RBM-N CLOSE','2019 RBM-N CLOSE','2020 RBM-N CLOSE','2021 RBM-N CLOSE',
                '2022 RBM-N CLOSE','2023 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y2a3':['2018 RBM-N CLOSE','2019 RBM-N CLOSE','2020 RBM-N CLOSE','2021 RBM-N CLOSE',
                '2022 RBM-N CLOSE','2023 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y3a3':['2018 RBM-N CLOSE','2019 RBM-N CLOSE','2020 RBM-N CLOSE','2021 RBM-N CLOSE',
                '2022 RBM-N CLOSE','2023 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBM-N VOLUME','2022 RBM-N VOLUME','RBM-N VOLUME 5 yr Avg','RBM-N VOLUME 10 yr Avg'],
        'y1b2':['2023 RBM-N VOLUME','2022 RBM-N VOLUME','RBM-N VOLUME 5 yr Avg','RBM-N VOLUME 10 yr Avg','SMA10_RBM-N_Vol_5yr',
                'SMA20_RBM-N_Vol_5yr','SMA10_RBM-N_Vol_10yr','SMA20_RBM-N_Vol_10yr'],
        'y1b3':['2018 RBM-N VOLUME','2019 RBM-N VOLUME','2020 RBM-N VOLUME','2021 RBM-N VOLUME',
                '2022 RBM-N VOLUME','2023 RBM-N VOLUME','RBM-N VOLUME 5 yr Avg','RBM-N VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBM OpenInt','2022 RBM OpenInt','RBM OpenInt 5 yr Avg','RBM OpenInt 10 yr Avg'],
        'y2b2':['2023 RBM OpenInt','2022 RBM OpenInt','RBM OpenInt 5 yr Avg','RBM OpenInt 10 yr Avg','SMA10_RBM_OpenInt_5yr',
                'SMA20_RBM_OpenInt_5yr','SMA10_RBM_OpenInt_10yr','SMA20_RBM_OpenInt_10yr'],
        'y2b3':['2018 RBM OpenInt','2019 RBM OpenInt','2020 RBM OpenInt','2021 RBM OpenInt',
                '2022 RBM OpenInt','2023 RBM OpenInt','RBM OpenInt 5 yr Avg','RBM OpenInt 10 yr Avg'],

        'y3b1':['2023 RBM-N OpenInt Ratio','2022 RBM-N OpenInt Ratio','RBM-N OpenInt Ratio 5 yr Avg','RBM-N OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBM-N OpenInt Ratio','2022 RBM-N OpenInt Ratio','RBM-N OpenInt Ratio 5 yr Avg','RBM-N OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBM-N OpenInt Ratio','2019 RBM-N OpenInt Ratio','2020 RBM-N OpenInt Ratio','2021 RBM-N OpenInt Ratio',
                '2022 RBM-N OpenInt Ratio','2023 RBM-N OpenInt Ratio','RBM-N OpenInt Ratio 5 yr Avg','RBM-N OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'RBN-Q': {
        'description':'RBOB Jul-Aug',
        'data': RBN_Q_df,
        'y1a1':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y2a1':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y3a1':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y1a2':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg','SMA10_RBN-Q_Close_5yr',
                'SMA20_RBN-Q_Close_5yr','SMA10_RBN-Q_Close_10yr','SMA20_RBN-Q_Close_10yr'],
        'y2a2':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg','SMA10_RBN-Q_Close_5yr',
                'SMA20_RBN-Q_Close_5yr','SMA10_RBN-Q_Close_10yr','SMA20_RBN-Q_Close_10yr'],
        'y3a2':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y1a3':['2018 RBN-Q CLOSE','2019 RBN-Q CLOSE','2020 RBN-Q CLOSE','2021 RBN-Q CLOSE',
                '2022 RBN-Q CLOSE','2023 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y2a3':['2018 RBN-Q CLOSE','2019 RBN-Q CLOSE','2020 RBN-Q CLOSE','2021 RBN-Q CLOSE',
                '2022 RBN-Q CLOSE','2023 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y3a3':['2018 RBN-Q CLOSE','2019 RBN-Q CLOSE','2020 RBN-Q CLOSE','2021 RBN-Q CLOSE',
                '2022 RBN-Q CLOSE','2023 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBN-Q VOLUME','2022 RBN-Q VOLUME','RBN-Q VOLUME 5 yr Avg','RBN-Q VOLUME 10 yr Avg'],
        'y1b2':['2023 RBN-Q VOLUME','2022 RBN-Q VOLUME','RBN-Q VOLUME 5 yr Avg','RBN-Q VOLUME 10 yr Avg','SMA10_RBN-Q_Vol_5yr',
                'SMA20_RBN-Q_Vol_5yr','SMA10_RBN-Q_Vol_10yr','SMA20_RBN-Q_Vol_10yr'],
        'y1b3':['2018 RBN-Q VOLUME','2019 RBN-Q VOLUME','2020 RBN-Q VOLUME','2021 RBN-Q VOLUME',
                '2022 RBN-Q VOLUME','2023 RBN-Q VOLUME','RBN-Q VOLUME 5 yr Avg','RBN-Q VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBN OpenInt','2022 RBN OpenInt','RBN OpenInt 5 yr Avg','RBN OpenInt 10 yr Avg'],
        'y2b2':['2023 RBN OpenInt','2022 RBN OpenInt','RBN OpenInt 5 yr Avg','RBN OpenInt 10 yr Avg','SMA10_RBN_OpenInt_5yr',
                'SMA20_RBN_OpenInt_5yr','SMA10_RBN_OpenInt_10yr','SMA20_RBN_OpenInt_10yr'],
        'y2b3':['2018 RBN OpenInt','2019 RBN OpenInt','2020 RBN OpenInt','2021 RBN OpenInt',
                '2022 RBN OpenInt','2023 RBN OpenInt','RBN OpenInt 5 yr Avg','RBN OpenInt 10 yr Avg'],

        'y3b1':['2023 RBN-Q OpenInt Ratio','2022 RBN-Q OpenInt Ratio','RBN-Q OpenInt Ratio 5 yr Avg','RBN-Q OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBN-Q OpenInt Ratio','2022 RBN-Q OpenInt Ratio','RBN-Q OpenInt Ratio 5 yr Avg','RBN-Q OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBN-Q OpenInt Ratio','2019 RBN-Q OpenInt Ratio','2020 RBN-Q OpenInt Ratio','2021 RBN-Q OpenInt Ratio',
                '2022 RBN-Q OpenInt Ratio','2023 RBN-Q OpenInt Ratio','RBN-Q OpenInt Ratio 5 yr Avg','RBN-Q OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBQ-U': {
        'description':'RBOB Aug-Sep',
        'data': RBQ_U_df,
        'y1a1':['2023 RBQ-U CLOSE','2022 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg'],
        'y2a1':['2023 RBQ-U CLOSE','2022 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg'],
        'y3a1':['2023 RBQ-U CLOSE','2022 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg'],
        'y1a2':['2023 RBQ-U CLOSE','2022 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg','SMA10_RBQ-U_Close_5yr',
                'SMA20_RBQ-U_Close_5yr','SMA10_RBQ-U_Close_10yr','SMA20_RBQ-U_Close_10yr'],
        'y2a2':['2023 RBQ-U CLOSE','2022 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg','SMA10_RBQ-U_Close_5yr',
                'SMA20_RBQ-U_Close_5yr','SMA10_RBQ-U_Close_10yr','SMA20_RBQ-U_Close_10yr'],
        'y3a2':['2023 RBQ-U CLOSE','2022 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg'],
        'y1a3':['2018 RBQ-U CLOSE','2019 RBQ-U CLOSE','2020 RBQ-U CLOSE','2021 RBQ-U CLOSE',
                '2022 RBQ-U CLOSE','2023 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg'],
        'y2a3':['2018 RBQ-U CLOSE','2019 RBQ-U CLOSE','2020 RBQ-U CLOSE','2021 RBQ-U CLOSE',
                '2022 RBQ-U CLOSE','2023 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg'],
        'y3a3':['2018 RBQ-U CLOSE','2019 RBQ-U CLOSE','2020 RBQ-U CLOSE','2021 RBQ-U CLOSE',
                '2022 RBQ-U CLOSE','2023 RBQ-U CLOSE','RBQ-U CLOSE 5 yr Avg','RBQ-U CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBQ-U VOLUME','2022 RBQ-U VOLUME','RBQ-U VOLUME 5 yr Avg','RBQ-U VOLUME 10 yr Avg'],
        'y1b2':['2023 RBQ-U VOLUME','2022 RBQ-U VOLUME','RBQ-U VOLUME 5 yr Avg','RBQ-U VOLUME 10 yr Avg','SMA10_RBQ-U_Vol_5yr',
                'SMA20_RBQ-U_Vol_5yr','SMA10_RBQ-U_Vol_10yr','SMA20_RBQ-U_Vol_10yr'],
        'y1b3':['2018 RBQ-U VOLUME','2019 RBQ-U VOLUME','2020 RBQ-U VOLUME','2021 RBQ-U VOLUME',
                '2022 RBQ-U VOLUME','2023 RBQ-U VOLUME','RBQ-U VOLUME 5 yr Avg','RBQ-U VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBQ OpenInt','2022 RBQ OpenInt','RBQ OpenInt 5 yr Avg','RBQ OpenInt 10 yr Avg'],
        'y2b2':['2023 RBQ OpenInt','2022 RBQ OpenInt','RBQ OpenInt 5 yr Avg','RBQ OpenInt 10 yr Avg','SMA10_RBQ_OpenInt_5yr',
                'SMA20_RBQ_OpenInt_5yr','SMA10_RBQ_OpenInt_10yr','SMA20_RBQ_OpenInt_10yr'],
        'y2b3':['2018 RBQ OpenInt','2019 RBQ OpenInt','2020 RBQ OpenInt','2021 RBQ OpenInt',
                '2022 RBQ OpenInt','2023 RBQ OpenInt','RBQ OpenInt 5 yr Avg','RBQ OpenInt 10 yr Avg'],

        'y3b1':['2023 RBQ-U OpenInt Ratio','2022 RBQ-U OpenInt Ratio','RBQ-U OpenInt Ratio 5 yr Avg','RBQ-U OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBQ-U OpenInt Ratio','2022 RBQ-U OpenInt Ratio','RBQ-U OpenInt Ratio 5 yr Avg','RBQ-U OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBQ-U OpenInt Ratio','2019 RBQ-U OpenInt Ratio','2020 RBQ-U OpenInt Ratio','2021 RBQ-U OpenInt Ratio',
                '2022 RBQ-U OpenInt Ratio','2023 RBQ-U OpenInt Ratio','RBQ-U OpenInt Ratio 5 yr Avg','RBQ-U OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBU-V': {
        'description':'RBOB Sep-Oct',
        'data': RBU_V_df,
        'y1a1':['2023 RBU-V CLOSE','2022 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg'],
        'y2a1':['2023 RBU-V CLOSE','2022 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg'],
        'y3a1':['2023 RBU-V CLOSE','2022 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg'],
        'y1a2':['2023 RBU-V CLOSE','2022 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg','SMA10_RBU-V_Close_5yr',
                'SMA20_RBU-V_Close_5yr','SMA10_RBU-V_Close_10yr','SMA20_RBU-V_Close_10yr'],
        'y2a2':['2023 RBU-V CLOSE','2022 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg','SMA10_RBU-V_Close_5yr',
                'SMA20_RBU-V_Close_5yr','SMA10_RBU-V_Close_10yr','SMA20_RBU-V_Close_10yr'],
        'y3a2':['2023 RBU-V CLOSE','2022 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg'],
        'y1a3':['2018 RBU-V CLOSE','2019 RBU-V CLOSE','2020 RBU-V CLOSE','2021 RBU-V CLOSE',
                '2022 RBU-V CLOSE','2023 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg'],
        'y2a3':['2018 RBU-V CLOSE','2019 RBU-V CLOSE','2020 RBU-V CLOSE','2021 RBU-V CLOSE',
                '2022 RBU-V CLOSE','2023 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg'],
        'y3a3':['2018 RBU-V CLOSE','2019 RBU-V CLOSE','2020 RBU-V CLOSE','2021 RBU-V CLOSE',
                '2022 RBU-V CLOSE','2023 RBU-V CLOSE','RBU-V CLOSE 5 yr Avg','RBU-V CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBU-V VOLUME','2022 RBU-V VOLUME','RBU-V VOLUME 5 yr Avg','RBU-V VOLUME 10 yr Avg'],
        'y1b2':['2023 RBU-V VOLUME','2022 RBU-V VOLUME','RBU-V VOLUME 5 yr Avg','RBU-V VOLUME 10 yr Avg','SMA10_RBU-V_Vol_5yr',
                'SMA20_RBU-V_Vol_5yr','SMA10_RBU-V_Vol_10yr','SMA20_RBU-V_Vol_10yr'],
        'y1b3':['2018 RBU-V VOLUME','2019 RBU-V VOLUME','2020 RBU-V VOLUME','2021 RBU-V VOLUME',
                '2022 RBU-V VOLUME','2023 RBU-V VOLUME','RBU-V VOLUME 5 yr Avg','RBU-V VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBU OpenInt','2022 RBU OpenInt','RBU OpenInt 5 yr Avg','RBU OpenInt 10 yr Avg'],
        'y2b2':['2023 RBU OpenInt','2022 RBU OpenInt','RBU OpenInt 5 yr Avg','RBU OpenInt 10 yr Avg','SMA10_RBU_OpenInt_5yr',
                'SMA20_RBU_OpenInt_5yr','SMA10_RBU_OpenInt_10yr','SMA20_RBU_OpenInt_10yr'],
        'y2b3':['2018 RBU OpenInt','2019 RBU OpenInt','2020 RBU OpenInt','2021 RBU OpenInt',
                '2022 RBU OpenInt','2023 RBU OpenInt','RBU OpenInt 5 yr Avg','RBU OpenInt 10 yr Avg'],

        'y3b1':['2023 RBU-V OpenInt Ratio','2022 RBU-V OpenInt Ratio','RBU-V OpenInt Ratio 5 yr Avg','RBU-V OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBU-V OpenInt Ratio','2022 RBU-V OpenInt Ratio','RBU-V OpenInt Ratio 5 yr Avg','RBU-V OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBU-V OpenInt Ratio','2019 RBU-V OpenInt Ratio','2020 RBU-V OpenInt Ratio','2021 RBU-V OpenInt Ratio',
                '2022 RBU-V OpenInt Ratio','2023 RBU-V OpenInt Ratio','RBU-V OpenInt Ratio 5 yr Avg','RBU-V OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'RBV-X': {
        'description':'RBOB Oct-Nov',
        'data': RBV_X_df,
        'y1a1':['2023 RBV-X CLOSE','2022 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg'],
        'y2a1':['2023 RBV-X CLOSE','2022 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg'],
        'y3a1':['2023 RBV-X CLOSE','2022 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg'],
        'y1a2':['2023 RBV-X CLOSE','2022 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg','SMA10_RBV-X_Close_5yr',
                'SMA20_RBV-X_Close_5yr','SMA10_RBV-X_Close_10yr','SMA20_RBV-X_Close_10yr'],
        'y2a2':['2023 RBV-X CLOSE','2022 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg','SMA10_RBV-X_Close_5yr',
                'SMA20_RBV-X_Close_5yr','SMA10_RBV-X_Close_10yr','SMA20_RBV-X_Close_10yr'],
        'y3a2':['2023 RBV-X CLOSE','2022 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg'],
        'y1a3':['2018 RBV-X CLOSE','2019 RBV-X CLOSE','2020 RBV-X CLOSE','2021 RBV-X CLOSE',
                '2022 RBV-X CLOSE','2023 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg'],
        'y2a3':['2018 RBV-X CLOSE','2019 RBV-X CLOSE','2020 RBV-X CLOSE','2021 RBV-X CLOSE',
                '2022 RBV-X CLOSE','2023 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg'],
        'y3a3':['2018 RBV-X CLOSE','2019 RBV-X CLOSE','2020 RBV-X CLOSE','2021 RBV-X CLOSE',
                '2022 RBV-X CLOSE','2023 RBV-X CLOSE','RBV-X CLOSE 5 yr Avg','RBV-X CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBV-X VOLUME','2022 RBV-X VOLUME','RBV-X VOLUME 5 yr Avg','RBV-X VOLUME 10 yr Avg'],
        'y1b2':['2023 RBV-X VOLUME','2022 RBV-X VOLUME','RBV-X VOLUME 5 yr Avg','RBV-X VOLUME 10 yr Avg','SMA10_RBV-X_Vol_5yr',
                'SMA20_RBV-X_Vol_5yr','SMA10_RBV-X_Vol_10yr','SMA20_RBV-X_Vol_10yr'],
        'y1b3':['2018 RBV-X VOLUME','2019 RBV-X VOLUME','2020 RBV-X VOLUME','2021 RBV-X VOLUME',
                '2022 RBV-X VOLUME','2023 RBV-X VOLUME','RBV-X VOLUME 5 yr Avg','RBV-X VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBV OpenInt','2022 RBV OpenInt','RBV OpenInt 5 yr Avg','RBV OpenInt 10 yr Avg'],
        'y2b2':['2023 RBV OpenInt','2022 RBV OpenInt','RBV OpenInt 5 yr Avg','RBV OpenInt 10 yr Avg','SMA10_RBV_OpenInt_5yr',
                'SMA20_RBV_OpenInt_5yr','SMA10_RBV_OpenInt_10yr','SMA20_RBV_OpenInt_10yr'],
        'y2b3':['2018 RBV OpenInt','2019 RBV OpenInt','2020 RBV OpenInt','2021 RBV OpenInt',
                '2022 RBV OpenInt','2023 RBV OpenInt','RBV OpenInt 5 yr Avg','RBV OpenInt 10 yr Avg'],

        'y3b1':['2023 RBV-X OpenInt Ratio','2022 RBV-X OpenInt Ratio','RBV-X OpenInt Ratio 5 yr Avg','RBV-X OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBV-X OpenInt Ratio','2022 RBV-X OpenInt Ratio','RBV-X OpenInt Ratio 5 yr Avg','RBV-X OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBV-X OpenInt Ratio','2019 RBV-X OpenInt Ratio','2020 RBV-X OpenInt Ratio','2021 RBV-X OpenInt Ratio',
                '2022 RBV-X OpenInt Ratio','2023 RBV-X OpenInt Ratio','RBV-X OpenInt Ratio 5 yr Avg','RBV-X OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    
    'RBX-Z': {
        'description':'RBOB Nov-Dec',
        'data': RBX_Z_df,
        'y1a1':['2023 RBX-Z CLOSE','2022 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg'],
        'y2a1':['2023 RBX-Z CLOSE','2022 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg'],
        'y3a1':['2023 RBX-Z CLOSE','2022 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg'],
        'y1a2':['2023 RBX-Z CLOSE','2022 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg','SMA10_RBX-Z_Close_5yr',
                'SMA20_RBX-Z_Close_5yr','SMA10_RBX-Z_Close_10yr','SMA20_RBX-Z_Close_10yr'],
        'y2a2':['2023 RBX-Z CLOSE','2022 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg','SMA10_RBX-Z_Close_5yr',
                'SMA20_RBX-Z_Close_5yr','SMA10_RBX-Z_Close_10yr','SMA20_RBX-Z_Close_10yr'],
        'y3a2':['2023 RBX-Z CLOSE','2022 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg'],
        'y1a3':['2018 RBX-Z CLOSE','2019 RBX-Z CLOSE','2020 RBX-Z CLOSE','2021 RBX-Z CLOSE',
                '2022 RBX-Z CLOSE','2023 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg'],
        'y2a3':['2018 RBX-Z CLOSE','2019 RBX-Z CLOSE','2020 RBX-Z CLOSE','2021 RBX-Z CLOSE',
                '2022 RBX-Z CLOSE','2023 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg'],
        'y3a3':['2018 RBX-Z CLOSE','2019 RBX-Z CLOSE','2020 RBX-Z CLOSE','2021 RBX-Z CLOSE',
                '2022 RBX-Z CLOSE','2023 RBX-Z CLOSE','RBX-Z CLOSE 5 yr Avg','RBX-Z CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBX-Z VOLUME','2022 RBX-Z VOLUME','RBX-Z VOLUME 5 yr Avg','RBX-Z VOLUME 10 yr Avg'],
        'y1b2':['2023 RBX-Z VOLUME','2022 RBX-Z VOLUME','RBX-Z VOLUME 5 yr Avg','RBX-Z VOLUME 10 yr Avg','SMA10_RBX-Z_Vol_5yr',
                'SMA20_RBX-Z_Vol_5yr','SMA10_RBX-Z_Vol_10yr','SMA20_RBX-Z_Vol_10yr'],
        'y1b3':['2018 RBX-Z VOLUME','2019 RBX-Z VOLUME','2020 RBX-Z VOLUME','2021 RBX-Z VOLUME',
                '2022 RBX-Z VOLUME','2023 RBX-Z VOLUME','RBX-Z VOLUME 5 yr Avg','RBX-Z VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBX OpenInt','2022 RBX OpenInt','RBX OpenInt 5 yr Avg','RBX OpenInt 10 yr Avg'],
        'y2b2':['2023 RBX OpenInt','2022 RBX OpenInt','RBX OpenInt 5 yr Avg','RBX OpenInt 10 yr Avg','SMA10_RBX_OpenInt_5yr',
                'SMA20_RBX_OpenInt_5yr','SMA10_RBX_OpenInt_10yr','SMA20_RBX_OpenInt_10yr'],
        'y2b3':['2018 RBX OpenInt','2019 RBX OpenInt','2020 RBX OpenInt','2021 RBX OpenInt',
                '2022 RBX OpenInt','2023 RBX OpenInt','RBX OpenInt 5 yr Avg','RBX OpenInt 10 yr Avg'],

        'y3b1':['2023 RBX-Z OpenInt Ratio','2022 RBX-Z OpenInt Ratio','RBX-Z OpenInt Ratio 5 yr Avg','RBX-Z OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBX-Z OpenInt Ratio','2022 RBX-Z OpenInt Ratio','RBX-Z OpenInt Ratio 5 yr Avg','RBX-Z OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBX-Z OpenInt Ratio','2019 RBX-Z OpenInt Ratio','2020 RBX-Z OpenInt Ratio','2021 RBX-Z OpenInt Ratio',
                '2022 RBX-Z OpenInt Ratio','2023 RBX-Z OpenInt Ratio','RBX-Z OpenInt Ratio 5 yr Avg','RBX-Z OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    
    'RBZ-F': {
        'description':'RBOB Dec-Jan',
        'data': RBZ_F_df,
        'y1a1':['2023 RBZ-F CLOSE','2022 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg'],
        'y2a1':['2023 RBZ-F CLOSE','2022 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg'],
        'y3a1':['2023 RBZ-F CLOSE','2022 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg'],
        'y1a2':['2023 RBZ-F CLOSE','2022 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg','SMA10_RBZ-F_Close_5yr',
                'SMA20_RBZ-F_Close_5yr','SMA10_RBZ-F_Close_10yr','SMA20_RBZ-F_Close_10yr'],
        'y2a2':['2023 RBZ-F CLOSE','2022 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg','SMA10_RBZ-F_Close_5yr',
                'SMA20_RBZ-F_Close_5yr','SMA10_RBZ-F_Close_10yr','SMA20_RBZ-F_Close_10yr'],
        'y3a2':['2023 RBZ-F CLOSE','2022 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg'],
        'y1a3':['2018 RBZ-F CLOSE','2019 RBZ-F CLOSE','2020 RBZ-F CLOSE','2021 RBZ-F CLOSE',
                '2022 RBZ-F CLOSE','2023 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg'],
        'y2a3':['2018 RBZ-F CLOSE','2019 RBZ-F CLOSE','2020 RBZ-F CLOSE','2021 RBZ-F CLOSE',
                '2022 RBZ-F CLOSE','2023 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg'],
        'y3a3':['2018 RBZ-F CLOSE','2019 RBZ-F CLOSE','2020 RBZ-F CLOSE','2021 RBZ-F CLOSE',
                '2022 RBZ-F CLOSE','2023 RBZ-F CLOSE','RBZ-F CLOSE 5 yr Avg','RBZ-F CLOSE 10 yr Avg'],

        
        'y1b1':['2023 RBZ-F VOLUME','2022 RBZ-F VOLUME','RBZ-F VOLUME 5 yr Avg','RBZ-F VOLUME 10 yr Avg'],
        'y1b2':['2023 RBZ-F VOLUME','2022 RBZ-F VOLUME','RBZ-F VOLUME 5 yr Avg','RBZ-F VOLUME 10 yr Avg','SMA10_RBZ-F_Vol_5yr',
                'SMA20_RBZ-F_Vol_5yr','SMA10_RBZ-F_Vol_10yr','SMA20_RBZ-F_Vol_10yr'],
        'y1b3':['2018 RBZ-F VOLUME','2019 RBZ-F VOLUME','2020 RBZ-F VOLUME','2021 RBZ-F VOLUME',
                '2022 RBZ-F VOLUME','2023 RBZ-F VOLUME','RBZ-F VOLUME 5 yr Avg','RBZ-F VOLUME 10 yr Avg'],
        
        'y2b1':['2023 RBZ OpenInt','2022 RBZ OpenInt','RBZ OpenInt 5 yr Avg','RBZ OpenInt 10 yr Avg'],
        'y2b2':['2023 RBZ OpenInt','2022 RBZ OpenInt','RBZ OpenInt 5 yr Avg','RBZ OpenInt 10 yr Avg','SMA10_RBZ_OpenInt_5yr',
                'SMA20_RBZ_OpenInt_5yr','SMA10_RBZ_OpenInt_10yr','SMA20_RBZ_OpenInt_10yr'],
        'y2b3':['2018 RBZ OpenInt','2019 RBZ OpenInt','2020 RBZ OpenInt','2021 RBZ OpenInt',
                '2022 RBZ OpenInt','2023 RBZ OpenInt','RBZ OpenInt 5 yr Avg','RBZ OpenInt 10 yr Avg'],

        'y3b1':['2023 RBZ-F OpenInt Ratio','2022 RBZ-F OpenInt Ratio','RBZ-F OpenInt Ratio 5 yr Avg','RBZ-F OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 RBZ-F OpenInt Ratio','2022 RBZ-F OpenInt Ratio','RBZ-F OpenInt Ratio 5 yr Avg','RBZ-F OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 RBZ-F OpenInt Ratio','2019 RBZ-F OpenInt Ratio','2020 RBZ-F OpenInt Ratio','2021 RBZ-F OpenInt Ratio',
                '2022 RBZ-F OpenInt Ratio','2023 RBZ-F OpenInt Ratio','RBZ-F OpenInt Ratio 5 yr Avg','RBZ-F OpenInt Ratio 10 yr Avg'],

        
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
    ('RBF-J','RBG-K','RBF-K','RBG-J','RBF-G','RBG-H','RBH-J','RBJ-K','RBK-M','RBM-N','RBN-Q','RBQ-U','RBU-V','RBV-X','RBX-Z','RBZ-F'))

    st.write('Selected Spread:', RBOB_Spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=RBOB_Spreads[spread]['y1a1']
    y1b=RBOB_Spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=RBOB_Spreads[spread]['y1a2']
    y1b=RBOB_Spreads[spread]['y1b2']

    
else:
    y1a=RBOB_Spreads[spread]['y1a3']
    y1b=RBOB_Spreads[spread]['y1b3']
    
fig = px.line(RBOB_Spreads[spread]['data'], x=RBOB_Spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(RBOB_Spreads[spread]['data'], x=RBOB_Spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

Subfig.add_traces(fig.data + fig2.data)
Subfig.layout.xaxis.title="Date"
Subfig.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig.layout.yaxis2.title="Spread Volume"
Subfig.layout.title=titletxt

Subfig.update_layout(
    title = RBOB_Spreads[spread]['description']+"  Spread Price Vs Volume",
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
    y2a=RBOB_Spreads[spread]['y2a1']
    y2b=RBOB_Spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=RBOB_Spreads[spread]['y2a2']
    y2b=RBOB_Spreads[spread]['y2b2']
    
    
else:
    y2a=RBOB_Spreads[spread]['y2a3']
    y2b=RBOB_Spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
Subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(RBOB_Spreads[spread]['data'], x=RBOB_Spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(RBOB_Spreads[spread]['data'], x=RBOB_Spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

Subfig1.add_traces(fig1.data + fig12.data)
Subfig1.layout.xaxis.title="Date"
Subfig1.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig1.layout.yaxis2.title="Open Interest"
Subfig1.layout.title=titletxt1

Subfig1.update_layout(
    title = RBOB_Spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    y3a=RBOB_Spreads[spread]['y3a1']
    y3b=RBOB_Spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=RBOB_Spreads[spread]['y3a2']
    y3b=RBOB_Spreads[spread]['y3b2']
    
    
else:
    y3a=RBOB_Spreads[spread]['y3a3']
    y3b=RBOB_Spreads[spread]['y3b3']

titletxt3='Price & Open Interest Ratio'
Subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(RBOB_Spreads[spread]['data'], x=RBOB_Spreads[spread]['x_value'], y=y3a, title=titletxt3)
fig12 = px.line(RBOB_Spreads[spread]['data'], x=RBOB_Spreads[spread]['x_value'], y=y3b, title=titletxt3)



fig12.update_traces(yaxis="y2")

Subfig2.add_traces(fig1.data + fig12.data)
Subfig2.layout.xaxis.title="Date"
Subfig2.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig2.layout.yaxis2.title="Open Interest Ratio"
Subfig2.layout.title=titletxt3

Subfig2.update_layout(
    title = RBOB_Spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    
    

     



