"""
#App to find patterns in RBOB spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots




st.set_page_config(page_title=" Energy Spreads ",layout="wide")

RBF_G_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='RBF-G')
RBG_H_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='RBG-H')
RBH_J_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='RBH-J')
RBJ_K_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='RBJ-K')
RBK_M_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='RBK-M')
RBM_N_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='RBM-N')
RBN_Q_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='RBN-Q')




rbob_spreads = { 
    'RBF-G': {
        'description':'RBOB Jan-Feb',
        'data': RBF_G_df,

        
        'y1a1':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y1a2':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg','SMA10_RBF-G_Close_5yr','SMA20_RBF-G_Close_5yr','SMA10_RBF-G_Close_10yr','SMA20_RBF-G_Close_10yr'],
        'y1a3':['2018 RBF-G CLOSE','2019 RBF-G CLOSE','2020 RBF-G CLOSE','2021 RBF-G CLOSE','2022 RBF-G CLOSE','2023 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg'],

        
        'y1b1':['2023 RBF-G VOLUME','2022 RBF-G VOLUME','RBF-G VOLUME 5 yr Avg','RBF-G VOLUME 10 yr Avg'],
        'y1b2':['2023 RBF-G VOLUME','2022 RBF-G VOLUME','RBF-G VOLUME 5 yr Avg','RBF-G VOLUME 10 yr Avg','SMA10_RBF-G_Vol_5yr','SMA20_RBF-G_Vol_5yr','SMA10_RBF-G_Vol_10yr','SMA20_RBF-G_Vol_10yr'],
        'y1b3':['2018 RBF-G VOLUME','2019 RBF-G VOLUME','2020 RBF-G VOLUME','2021 RBF-G VOLUME','2022 RBF-G VOLUME','2023 RBF-G VOLUME','RBF-G VOLUME 5 yr Avg'],

        
        'y2a1':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y2b1':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg'],
        'y2a2':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg','SMA10_RBF-G_Close_5yr','SMA20_RBF-G_Close_5yr','SMA10_RBF-G_Close_10yr','SMA20_RBF-G_Close_10yr'],
        
        'y2b2':['2023 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg','RBF OpenInt 10 yr Avg','SMA10_RBF_OpenInt_5yr','SMA20_RBF_OpenInt_5yr','SMA10_RBF_OpenInt_10yr','SMA20_RBF_OpenInt_10yr'],
        'y2a3':['2018 RBF-G CLOSE','2019 RBF-G CLOSE','2020 RBF-G CLOSE','2021 RBF-G CLOSE','2022 RBF-G CLOSE','2023 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg'],
        'y2b3':['2023 RBF OpenInt','2018 RBF OpenInt','2019 RBF OpenInt','2020 RBF OpenInt','2021 RBF OpenInt','2022 RBF OpenInt','RBF OpenInt 5 yr Avg'],


        'y3a1':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y3b1':['2023 RBF-G OI Ratio','2022 RBF-G OI Ratio','RBF-G OI Ratio 5 yr Avg','RBF-G OI Ratio 10 yr Avg'],

        'y3a2':['2023 RBF-G CLOSE','2022 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg','RBF-G CLOSE 10 yr Avg'],
        'y3b2':['2023 RBF-G OI Ratio','2022 RBF-G OI Ratio','RBF-G OI Ratio 5 yr Avg','RBF-G OI Ratio 10 yr Avg'],

        
        
        'y3a3':['2018 RBF-G CLOSE','2019 RBF-G CLOSE','2020 RBF-G CLOSE','2021 RBF-G CLOSE','2022 RBF-G CLOSE','2023 RBF-G CLOSE','RBF-G CLOSE 5 yr Avg'],
        'y3b3':['2023 RBF-G OI Ratio','2022 RBF-G OI Ratio','2021 RBF-G OI Ratio','2020 RBF-G OI Ratio','2019 RBF-G OI Ratio','2018 RBF-G OI Ratio','RBF-G OI Ratio 5 yr Avg','RBF-G OI Ratio 10 yr Avg'],
        
        'x_value':'2022 Dates'
    },
  'RBG-H': {
        'description':'RBOB Feb-Mar',
        'data': RBG_H_df,

        
        'y1a1':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y1a2':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg','SMA10_RBG-H_Close_5yr','SMA20_RBG-H_Close_5yr','SMA10_RBG-H_Close_10yr','SMA20_RBG-H_Close_10yr'],
        'y1a3':['2018 RBG-H CLOSE','2019 RBG-H CLOSE','2020 RBG-H CLOSE','2021 RBG-H CLOSE','2022 RBG-H CLOSE','2023 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg'],

        
        'y1b1':['2023 RBG-H VOLUME','2022 RBG-H VOLUME','RBG-H VOLUME 5 yr Avg','RBG-H VOLUME 10 yr Avg'],
        'y1b2':['2023 RBG-H VOLUME','2022 RBG-H VOLUME','RBG-H VOLUME 5 yr Avg','RBG-H VOLUME 10 yr Avg','SMA10_RBG-H_Vol_5yr','SMA20_RBG-H_Vol_5yr','SMA10_RBG-H_Vol_10yr','SMA20_RBG-H_Vol_10yr'],
        'y1b3':['2018 RBG-H VOLUME','2019 RBG-H VOLUME','2020 RBG-H VOLUME','2021 RBG-H VOLUME','2022 RBG-H VOLUME','2023 RBG-H VOLUME','RBG-H VOLUME 5 yr Avg'],

        
        'y2a1':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y2b1':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg'],
        'y2a2':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg','SMA10_RBG-H_Close_5yr','SMA20_RBG-H_Close_5yr','SMA10_RBG-H_Close_10yr','SMA20_RBG-H_Close_10yr'],
        
        'y2b2':['2023 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg','RBG OpenInt 10 yr Avg','SMA10_RBG_OpenInt_5yr','SMA20_RBG_OpenInt_5yr','SMA10_RBG_OpenInt_10yr','SMA20_RBG_OpenInt_10yr'],
        'y2a3':['2018 RBG-H CLOSE','2019 RBG-H CLOSE','2020 RBG-H CLOSE','2021 RBG-H CLOSE','2022 RBG-H CLOSE','2023 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg'],
        'y2b3':['2023 RBG OpenInt','2018 RBG OpenInt','2019 RBG OpenInt','2020 RBG OpenInt','2021 RBG OpenInt','2022 RBG OpenInt','RBG OpenInt 5 yr Avg'],


        'y3a1':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y3b1':['2023 RBG-H OI Ratio','2022 RBG-H OI Ratio','RBG-H OI Ratio 5 yr Avg','RBG-H OI Ratio 10 yr Avg'],

        'y3a2':['2023 RBG-H CLOSE','2022 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg','RBG-H CLOSE 10 yr Avg'],
        'y3b2':['2023 RBG-H OI Ratio','2022 RBG-H OI Ratio','RBG-H OI Ratio 5 yr Avg','RBG-H OI Ratio 10 yr Avg'],

        
        
        'y3a3':['2018 RBG-H CLOSE','2019 RBG-H CLOSE','2020 RBG-H CLOSE','2021 RBG-H CLOSE','2022 RBG-H CLOSE','2023 RBG-H CLOSE','RBG-H CLOSE 5 yr Avg'],
        'y3b3':['2023 RBG-H OI Ratio','2022 RBG-H OI Ratio','2021 RBG-H OI Ratio','2020 RBG-H OI Ratio','2019 RBG-H OI Ratio','2018 RBG-H OI Ratio','RBG-H OI Ratio 5 yr Avg','RBG-H OI Ratio 10 yr Avg'],
        
        'x_value':'2022 Dates'
    },



    'RBH-J': {
        'description':'RBOB Mar-Apr',
        'data': RBH_J_df,

        
        'y1a1':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y1a2':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg','SMA10_RBH-J_Close_5yr','SMA20_RBH-J_Close_5yr','SMA10_RBH-J_Close_10yr','SMA20_RBH-J_Close_10yr'],
        'y1a3':['2018 RBH-J CLOSE','2019 RBH-J CLOSE','2020 RBH-J CLOSE','2021 RBH-J CLOSE','2022 RBH-J CLOSE','2023 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg'],

        
        'y1b1':['2023 RBH-J VOLUME','2022 RBH-J VOLUME','RBH-J VOLUME 5 yr Avg','RBH-J VOLUME 10 yr Avg'],
        'y1b2':['2023 RBH-J VOLUME','2022 RBH-J VOLUME','RBH-J VOLUME 5 yr Avg','RBH-J VOLUME 10 yr Avg','SMA10_RBH-J_Vol_5yr','SMA20_RBH-J_Vol_5yr','SMA10_RBH-J_Vol_10yr','SMA20_RBH-J_Vol_10yr'],
        'y1b3':['2018 RBH-J VOLUME','2019 RBH-J VOLUME','2020 RBH-J VOLUME','2021 RBH-J VOLUME','2022 RBH-J VOLUME','2023 RBH-J VOLUME','RBH-J VOLUME 5 yr Avg'],

        
        'y2a1':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y2b1':['2023 RBH OpenInt','2022 RBH OpenInt','RBH OpenInt 5 yr Avg','RBH OpenInt 10 yr Avg'],
        'y2a2':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg','SMA10_RBH-J_Close_5yr','SMA20_RBH-J_Close_5yr','SMA10_RBH-J_Close_10yr','SMA20_RBH-J_Close_10yr'],
        
        'y2b2':['2023 RBH OpenInt','2022 RBH OpenInt','RBH OpenInt 5 yr Avg','RBH OpenInt 10 yr Avg','SMA10_RBH_OpenInt_5yr','SMA20_RBH_OpenInt_5yr','SMA10_RBH_OpenInt_10yr','SMA20_RBH_OpenInt_10yr'],
        'y2a3':['2018 RBH-J CLOSE','2019 RBH-J CLOSE','2020 RBH-J CLOSE','2021 RBH-J CLOSE','2022 RBH-J CLOSE','2023 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg'],
        'y2b3':['2023 RBH OpenInt','2018 RBH OpenInt','2019 RBH OpenInt','2020 RBH OpenInt','2021 RBH OpenInt','2022 RBH OpenInt','RBH OpenInt 5 yr Avg'],


        'y3a1':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y3b1':['2023 RBH-J OI Ratio','2022 RBH-J OI Ratio','RBH-J OI Ratio 5 yr Avg','RBH-J OI Ratio 10 yr Avg'],

        'y3a2':['2023 RBH-J CLOSE','2022 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg','RBH-J CLOSE 10 yr Avg'],
        'y3b2':['2023 RBH-J OI Ratio','2022 RBH-J OI Ratio','RBH-J OI Ratio 5 yr Avg','RBH-J OI Ratio 10 yr Avg'],

        
        
        'y3a3':['2018 RBH-J CLOSE','2019 RBH-J CLOSE','2020 RBH-J CLOSE','2021 RBH-J CLOSE','2022 RBH-J CLOSE','2023 RBH-J CLOSE','RBH-J CLOSE 5 yr Avg'],
        'y3b3':['2023 RBH-J OI Ratio','2022 RBH-J OI Ratio','2021 RBH-J OI Ratio','2020 RBH-J OI Ratio','2019 RBH-J OI Ratio','2018 RBH-J OI Ratio','RBH-J OI Ratio 5 yr Avg','RBH-J OI Ratio 10 yr Avg'],
        
        'x_value':'2022 Dates'
    },

    
    'RBJ-K': {
        'description':'RBOB Apr-May',
        'data': RBJ_K_df,

        
        'y1a1':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y1a2':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg','SMA10_RBJ-K_Close_5yr','SMA20_RBJ-K_Close_5yr','SMA10_RBJ-K_Close_10yr','SMA20_RBJ-K_Close_10yr'],
        'y1a3':['2018 RBJ-K CLOSE','2019 RBJ-K CLOSE','2020 RBJ-K CLOSE','2021 RBJ-K CLOSE','2022 RBJ-K CLOSE','2023 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg'],

        
        'y1b1':['2023 RBJ-K VOLUME','2022 RBJ-K VOLUME','RBJ-K VOLUME 5 yr Avg','RBJ-K VOLUME 10 yr Avg'],
        'y1b2':['2023 RBJ-K VOLUME','2022 RBJ-K VOLUME','RBJ-K VOLUME 5 yr Avg','RBJ-K VOLUME 10 yr Avg','SMA10_RBJ-K_Vol_5yr','SMA20_RBJ-K_Vol_5yr','SMA10_RBJ-K_Vol_10yr','SMA20_RBJ-K_Vol_10yr'],
        'y1b3':['2018 RBJ-K VOLUME','2019 RBJ-K VOLUME','2020 RBJ-K VOLUME','2021 RBJ-K VOLUME','2022 RBJ-K VOLUME','2023 RBJ-K VOLUME','RBJ-K VOLUME 5 yr Avg'],

        
        'y2a1':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y2b1':['2023 RBJ OpenInt','2022 RBJ OpenInt','RBJ OpenInt 5 yr Avg','RBJ OpenInt 10 yr Avg'],
        'y2a2':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg','SMA10_RBJ-K_Close_5yr','SMA20_RBJ-K_Close_5yr','SMA10_RBJ-K_Close_10yr','SMA20_RBJ-K_Close_10yr'],
        
        'y2b2':['2023 RBJ OpenInt','2022 RBJ OpenInt','RBJ OpenInt 5 yr Avg','RBJ OpenInt 10 yr Avg','SMA10_RBJ_OpenInt_5yr','SMA20_RBJ_OpenInt_5yr','SMA10_RBJ_OpenInt_10yr','SMA20_RBJ_OpenInt_10yr'],
        'y2a3':['2018 RBJ-K CLOSE','2019 RBJ-K CLOSE','2020 RBJ-K CLOSE','2021 RBJ-K CLOSE','2022 RBJ-K CLOSE','2023 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg'],
        'y2b3':['2023 RBJ OpenInt','2018 RBJ OpenInt','2019 RBJ OpenInt','2020 RBJ OpenInt','2021 RBJ OpenInt','2022 RBJ OpenInt','RBJ OpenInt 5 yr Avg'],


        'y3a1':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y3b1':['2023 RBJ-K OI Ratio','2022 RBJ-K OI Ratio','RBJ-K OI Ratio 5 yr Avg','RBJ-K OI Ratio 10 yr Avg'],

        'y3a2':['2023 RBJ-K CLOSE','2022 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg','RBJ-K CLOSE 10 yr Avg'],
        'y3b2':['2023 RBJ-K OI Ratio','2022 RBJ-K OI Ratio','RBJ-K OI Ratio 5 yr Avg','RBJ-K OI Ratio 10 yr Avg'],

        
        
        'y3a3':['2018 RBJ-K CLOSE','2019 RBJ-K CLOSE','2020 RBJ-K CLOSE','2021 RBJ-K CLOSE','2022 RBJ-K CLOSE','2023 RBJ-K CLOSE','RBJ-K CLOSE 5 yr Avg'],
        'y3b3':['2023 RBJ-K OI Ratio','2022 RBJ-K OI Ratio','2021 RBJ-K OI Ratio','2020 RBJ-K OI Ratio','2019 RBJ-K OI Ratio','2018 RBJ-K OI Ratio','RBJ-K OI Ratio 5 yr Avg','RBJ-K OI Ratio 10 yr Avg'],
        
        'x_value':'2022 Dates'
    },
    
    'RBK-M': {
        'description':'RBOB May-Jun',
        'data': RBK_M_df,

        
        'y1a1':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y1a2':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg','SMA10_RBK-M_Close_5yr','SMA20_RBK-M_Close_5yr','SMA10_RBK-M_Close_10yr','SMA20_RBK-M_Close_10yr'],
        'y1a3':['2018 RBK-M CLOSE','2019 RBK-M CLOSE','2020 RBK-M CLOSE','2021 RBK-M CLOSE','2022 RBK-M CLOSE','2023 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg'],

        
        'y1b1':['2023 RBK-M VOLUME','2022 RBK-M VOLUME','RBK-M VOLUME 5 yr Avg','RBK-M VOLUME 10 yr Avg'],
        'y1b2':['2023 RBK-M VOLUME','2022 RBK-M VOLUME','RBK-M VOLUME 5 yr Avg','RBK-M VOLUME 10 yr Avg','SMA10_RBK-M_Vol_5yr','SMA20_RBK-M_Vol_5yr','SMA10_RBK-M_Vol_10yr','SMA20_RBK-M_Vol_10yr'],
        'y1b3':['2018 RBK-M VOLUME','2019 RBK-M VOLUME','2020 RBK-M VOLUME','2021 RBK-M VOLUME','2022 RBK-M VOLUME','2023 RBK-M VOLUME','RBK-M VOLUME 5 yr Avg'],

        
        'y2a1':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y2b1':['2023 RBK OpenInt','2022 RBK OpenInt','RBK OpenInt 5 yr Avg','RBK OpenInt 10 yr Avg'],
        'y2a2':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg','SMA10_RBK-M_Close_5yr','SMA20_RBK-M_Close_5yr','SMA10_RBK-M_Close_10yr','SMA20_RBK-M_Close_10yr'],
        
        'y2b2':['2023 RBK OpenInt','2022 RBK OpenInt','RBK OpenInt 5 yr Avg','RBK OpenInt 10 yr Avg','SMA10_RBK_OpenInt_5yr','SMA20_RBK_OpenInt_5yr','SMA10_RBK_OpenInt_10yr','SMA20_RBK_OpenInt_10yr'],
        'y2a3':['2018 RBK-M CLOSE','2019 RBK-M CLOSE','2020 RBK-M CLOSE','2021 RBK-M CLOSE','2022 RBK-M CLOSE','2023 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg'],
        'y2b3':['2023 RBK OpenInt','2018 RBK OpenInt','2019 RBK OpenInt','2020 RBK OpenInt','2021 RBK OpenInt','2022 RBK OpenInt','RBK OpenInt 5 yr Avg'],


        'y3a1':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y3b1':['2023 RBK-M OI Ratio','2022 RBK-M OI Ratio','RBK-M OI Ratio 5 yr Avg','RBK-M OI Ratio 10 yr Avg'],

        'y3a2':['2023 RBK-M CLOSE','2022 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg','RBK-M CLOSE 10 yr Avg'],
        'y3b2':['2023 RBK-M OI Ratio','2022 RBK-M OI Ratio','RBK-M OI Ratio 5 yr Avg','RBK-M OI Ratio 10 yr Avg'],

        
        
        'y3a3':['2018 RBK-M CLOSE','2019 RBK-M CLOSE','2020 RBK-M CLOSE','2021 RBK-M CLOSE','2022 RBK-M CLOSE','2023 RBK-M CLOSE','RBK-M CLOSE 5 yr Avg'],
        'y3b3':['2023 RBK-M OI Ratio','2022 RBK-M OI Ratio','2021 RBK-M OI Ratio','2020 RBK-M OI Ratio','2019 RBK-M OI Ratio','2018 RBK-M OI Ratio','RBK-M OI Ratio 5 yr Avg','RBK-M OI Ratio 10 yr Avg'],
        
        'x_value':'2022 Dates'
    },


    
    'RBM-N': {
        'description':'RBOB Jun-Jul',
        'data': RBM_N_df,

        
        'y1a1':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y1a2':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg','SMA10_RBM-N_Close_5yr','SMA20_RBM-N_Close_5yr','SMA10_RBM-N_Close_10yr','SMA20_RBM-N_Close_10yr'],
        'y1a3':['2018 RBM-N CLOSE','2019 RBM-N CLOSE','2020 RBM-N CLOSE','2021 RBM-N CLOSE','2022 RBM-N CLOSE','2023 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg'],

        
        'y1b1':['2023 RBM-N VOLUME','2022 RBM-N VOLUME','RBM-N VOLUME 5 yr Avg','RBM-N VOLUME 10 yr Avg'],
        'y1b2':['2023 RBM-N VOLUME','2022 RBM-N VOLUME','RBM-N VOLUME 5 yr Avg','RBM-N VOLUME 10 yr Avg','SMA10_RBM-N_Vol_5yr','SMA20_RBM-N_Vol_5yr','SMA10_RBM-N_Vol_10yr','SMA20_RBM-N_Vol_10yr'],
        'y1b3':['2018 RBM-N VOLUME','2019 RBM-N VOLUME','2020 RBM-N VOLUME','2021 RBM-N VOLUME','2022 RBM-N VOLUME','2023 RBM-N VOLUME','RBM-N VOLUME 5 yr Avg'],

        
        'y2a1':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y2b1':['2023 RBM OpenInt','2022 RBM OpenInt','RBM OpenInt 5 yr Avg','RBM OpenInt 10 yr Avg'],
        'y2a2':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg','SMA10_RBM-N_Close_5yr','SMA20_RBM-N_Close_5yr','SMA10_RBM-N_Close_10yr','SMA20_RBM-N_Close_10yr'],
        
        'y2b2':['2023 RBM OpenInt','2022 RBM OpenInt','RBM OpenInt 5 yr Avg','RBM OpenInt 10 yr Avg','SMA10_RBM_OpenInt_5yr','SMA20_RBM_OpenInt_5yr','SMA10_RBM_OpenInt_10yr','SMA20_RBM_OpenInt_10yr'],
        'y2a3':['2018 RBM-N CLOSE','2019 RBM-N CLOSE','2020 RBM-N CLOSE','2021 RBM-N CLOSE','2022 RBM-N CLOSE','2023 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg'],
        'y2b3':['2023 RBM OpenInt','2018 RBM OpenInt','2019 RBM OpenInt','2020 RBM OpenInt','2021 RBM OpenInt','2022 RBM OpenInt','RBM OpenInt 5 yr Avg'],


        'y3a1':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y3b1':['2023 RBM-N OI Ratio','2022 RBM-N OI Ratio','RBM-N OI Ratio 5 yr Avg','RBM-N OI Ratio 10 yr Avg'],

        'y3a2':['2023 RBM-N CLOSE','2022 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg','RBM-N CLOSE 10 yr Avg'],
        'y3b2':['2023 RBM-N OI Ratio','2022 RBM-N OI Ratio','RBM-N OI Ratio 5 yr Avg','RBM-N OI Ratio 10 yr Avg'],

        
        
        'y3a3':['2018 RBM-N CLOSE','2019 RBM-N CLOSE','2020 RBM-N CLOSE','2021 RBM-N CLOSE','2022 RBM-N CLOSE','2023 RBM-N CLOSE','RBM-N CLOSE 5 yr Avg'],
        'y3b3':['2023 RBM-N OI Ratio','2022 RBM-N OI Ratio','2021 RBM-N OI Ratio','2020 RBM-N OI Ratio','2019 RBM-N OI Ratio','2018 RBM-N OI Ratio','RBM-N OI Ratio 5 yr Avg','RBM-N OI Ratio 10 yr Avg'],
        
        'x_value':'2022 Dates'
    },

    
    'RBN-Q': {
        'description':'RBOB Jul-Aug',
        'data': RBN_Q_df,

        
        'y1a1':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y1a2':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg','SMA10_RBN-Q_Close_5yr','SMA20_RBN-Q_Close_5yr','SMA10_RBN-Q_Close_10yr','SMA20_RBN-Q_Close_10yr'],
        'y1a3':['2018 RBN-Q CLOSE','2019 RBN-Q CLOSE','2020 RBN-Q CLOSE','2021 RBN-Q CLOSE','2022 RBN-Q CLOSE','2023 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg'],

        
        'y1b1':['2023 RBN-Q VOLUME','2022 RBN-Q VOLUME','RBN-Q VOLUME 5 yr Avg','RBN-Q VOLUME 10 yr Avg'],
        'y1b2':['2023 RBN-Q VOLUME','2022 RBN-Q VOLUME','RBN-Q VOLUME 5 yr Avg','RBN-Q VOLUME 10 yr Avg','SMA10_RBN-Q_Vol_5yr','SMA20_RBN-Q_Vol_5yr','SMA10_RBN-Q_Vol_10yr','SMA20_RBN-Q_Vol_10yr'],
        'y1b3':['2018 RBN-Q VOLUME','2019 RBN-Q VOLUME','2020 RBN-Q VOLUME','2021 RBN-Q VOLUME','2022 RBN-Q VOLUME','2023 RBN-Q VOLUME','RBN-Q VOLUME 5 yr Avg'],

        
        'y2a1':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y2b1':['2023 RBN OpenInt','2022 RBN OpenInt','RBN OpenInt 5 yr Avg','RBN OpenInt 10 yr Avg'],
        'y2a2':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg','SMA10_RBN-Q_Close_5yr','SMA20_RBN-Q_Close_5yr','SMA10_RBN-Q_Close_10yr','SMA20_RBN-Q_Close_10yr'],
        
        'y2b2':['2023 RBN OpenInt','2022 RBN OpenInt','RBN OpenInt 5 yr Avg','RBN OpenInt 10 yr Avg','SMA10_RBN_OpenInt_5yr','SMA20_RBN_OpenInt_5yr','SMA10_RBN_OpenInt_10yr','SMA20_RBN_OpenInt_10yr'],
        'y2a3':['2018 RBN-Q CLOSE','2019 RBN-Q CLOSE','2020 RBN-Q CLOSE','2021 RBN-Q CLOSE','2022 RBN-Q CLOSE','2023 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg'],
        'y2b3':['2023 RBN OpenInt','2018 RBN OpenInt','2019 RBN OpenInt','2020 RBN OpenInt','2021 RBN OpenInt','2022 RBN OpenInt','RBN OpenInt 5 yr Avg'],


        'y3a1':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y3b1':['2023 RBN-Q OI Ratio','2022 RBN-Q OI Ratio','RBN-Q OI Ratio 5 yr Avg','RBN-Q OI Ratio 10 yr Avg'],

        'y3a2':['2023 RBN-Q CLOSE','2022 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg','RBN-Q CLOSE 10 yr Avg'],
        'y3b2':['2023 RBN-Q OI Ratio','2022 RBN-Q OI Ratio','RBN-Q OI Ratio 5 yr Avg','RBN-Q OI Ratio 10 yr Avg'],

        
        
        'y3a3':['2018 RBN-Q CLOSE','2019 RBN-Q CLOSE','2020 RBN-Q CLOSE','2021 RBN-Q CLOSE','2022 RBN-Q CLOSE','2023 RBN-Q CLOSE','RBN-Q CLOSE 5 yr Avg'],
        'y3b3':['2023 RBN-Q OI Ratio','2022 RBN-Q OI Ratio','2021 RBN-Q OI Ratio','2020 RBN-Q OI Ratio','2019 RBN-Q OI Ratio','2018 RBN-Q OI Ratio','RBN-Q OI Ratio 5 yr Avg','RBN-Q OI Ratio 10 yr Avg'],
        
        'x_value':'2022 Dates'
    }
}

comments=pd.read_excel("comments.xlsx")

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""


def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

        
titletxt='Price & Volume'
subfig = make_subplots(specs=[[{"secondary_y": True}]])






with st.sidebar.container():

    
    
    spread = st.selectbox(
    'Select spread',
    (['RBF-G','RBG-H','RBH-J','RBJ-K','RBK-M','RBM-N','RBN-Q']))
    #
    st.write('Selected Spread:', rbob_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest Ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=rbob_spreads[spread]['y1a1']
    y1b=rbob_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=rbob_spreads[spread]['y1a2']
    y1b=rbob_spreads[spread]['y1b2']

    
else:
    y1a=rbob_spreads[spread]['y1a3']
    y1b=rbob_spreads[spread]['y1b3']
    
fig = px.line(rbob_spreads[spread]['data'], x=rbob_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(rbob_spreads[spread]['data'], x=rbob_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Date"
#subfig.layout.xaxis_tickformat ='%d %B <br>%Y'
subfig.layout.yaxis.title="Spread Price"
#subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="Spread Volume"
subfig.layout.title=titletxt

subfig.update_layout(
    title = rbob_spreads[spread]['description']+"  Spread Price Vs Volume",
    #xaxis_tickformat = '%d %B (%a)<br>%Y'
    xaxis_tickformat = '%b %d'
    #xaxis_tickformat = '%B'

)



# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#subfig.show()

subfig.update_xaxes(
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






#--------------------------------------------------------------------------------------------------------------##########################********************************************


if selected_graph=='Latest and Historic Avg':
    y2a=rbob_spreads[spread]['y2a1']
    y2b=rbob_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=rbob_spreads[spread]['y2a2']
    y2b=rbob_spreads[spread]['y2b2']
    
    
else:
    y2a=rbob_spreads[spread]['y2a3']
    y2b=rbob_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(rbob_spreads[spread]['data'], x=rbob_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(rbob_spreads[spread]['data'], x=rbob_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

subfig1.add_traces(fig1.data + fig12.data)
subfig1.layout.xaxis.title="Date"
subfig1.layout.yaxis.title="Spread Price"
#subfig.layout.yaxis2.type="log"
subfig1.layout.yaxis2.title="Open Interest"
subfig1.layout.title=titletxt1
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this


subfig1.update_layout(
    title = rbob_spreads[spread]['description']+"  Spread Price Vs Open Interest",
    #xaxis_tickformat = '%d %B (%a)<br>%Y'
    xaxis_tickformat = '%b %d'
    #xaxis_tickformat = '%B'

)

subfig1.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#subfig.show()

#subfig1.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Red')

subfig1.update_xaxes(
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


#--------------------------------------------------------------------------------------------------------------##########################********************************************


if selected_graph=='Latest and Historic Avg':
    y3a=rbob_spreads[spread]['y3a1']
    y3b=rbob_spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=rbob_spreads[spread]['y3a2']
    y3b=rbob_spreads[spread]['y3b2']
    
    
else:
    y3a=rbob_spreads[spread]['y3a3']
    y3b=rbob_spreads[spread]['y3b3']

titletxt1='Price & Open Interest Ratio [Front_Open_Int / ( Front_Open_Int + Back_Open_Int) * 100] '
subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2 = px.line(rbob_spreads[spread]['data'], x=rbob_spreads[spread]['x_value'], y=y3a, title=titletxt)
fig22 = px.line(rbob_spreads[spread]['data'], x=rbob_spreads[spread]['x_value'], y=y3b, title=titletxt)



fig22.update_traces(yaxis="y2")

subfig2.add_traces(fig2.data + fig22.data)
subfig2.layout.xaxis.title="Date"
subfig2.layout.yaxis.title="Spread Price"
#subfig.layout.yaxis2.type="log"
subfig2.layout.yaxis2.title="Open Interest Ratio "
subfig2.layout.title=titletxt1



subfig2.update_layout(
    title = rbob_spreads[spread]['description']+"  Spread Price Vs Open Interest Ratio",
    #xaxis_tickformat = '%d %B (%a)<br>%Y'
    xaxis_tickformat = '%b %d'
    #xaxis_tickformat = '%B'

)



# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig2.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#subfig.show()

#subfig1.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Red')

subfig2.update_xaxes(
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
    subfig.update_layout(height=650,width=1200)
    st.plotly_chart(subfig,use_container_width = True,height=650,width=1200)
elif selected_values=='Open Interest':
    subfig1.update_layout(height=650,width=1200)
    st.plotly_chart(subfig1,use_container_width = True,height=650,width=1200)

else:
    subfig2.update_layout(height=650,width=1200)
    st.plotly_chart(subfig2,use_container_width = True,height=650,width=1200)


    




