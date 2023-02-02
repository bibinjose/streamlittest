"""
#App to find patterns in SRW  spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
color_selected=px.colors.qualitative.Alphabet
st.set_page_config(page_title=" SRW Spreads ",layout="wide")

WH_K_df=pd.read_excel("srw_spread_data.xlsx",sheet_name='WH-K')
WK_N_df=pd.read_excel("srw_spread_data.xlsx",sheet_name='WK-N')
WN_U_df=pd.read_excel("srw_spread_data.xlsx",sheet_name='WN-U')
WU_Z_df=pd.read_excel("srw_spread_data.xlsx",sheet_name='WU-Z')
WZ_H_df=pd.read_excel("srw_spread_data.xlsx",sheet_name='WZ-H')



SRW_spreads = { 
    'WH-K': {
        'description':'SRW Jan-Mar',
        'data': WH_K_df,
        'y1a1':['2023 WH-K CLOSE','2022 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg'],
        'y2a1':['2023 WH-K CLOSE','2022 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg'],
        'y3a1':['2023 WH-K CLOSE','2022 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg'],
        'y1a2':['2023 WH-K CLOSE','2022 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg','SMA10_WH-K_Close_5yr',
                'SMA20_WH-K_Close_5yr','SMA10_WH-K_Close_10yr','SMA20_WH-K_Close_10yr'],
        'y2a2':['2023 WH-K CLOSE','2022 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg','SMA10_WH-K_Close_5yr',
                'SMA20_WH-K_Close_5yr','SMA10_WH-K_Close_10yr','SMA20_WH-K_Close_10yr'],
        'y3a2':['2023 WH-K CLOSE','2022 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg'],
        'y1a3':['2018 WH-K CLOSE','2019 WH-K CLOSE','2020 WH-K CLOSE','2021 WH-K CLOSE',
                '2022 WH-K CLOSE','2023 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg'],
        'y2a3':['2018 WH-K CLOSE','2019 WH-K CLOSE','2020 WH-K CLOSE','2021 WH-K CLOSE',
                '2022 WH-K CLOSE','2023 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg'],
        'y3a3':['2018 WH-K CLOSE','2019 WH-K CLOSE','2020 WH-K CLOSE','2021 WH-K CLOSE',
                '2022 WH-K CLOSE','2023 WH-K CLOSE','WH-K CLOSE 5 yr Avg','WH-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 WH-K VOLUME','2022 WH-K VOLUME','WH-K VOLUME 5 yr Avg','WH-K VOLUME 10 yr Avg'],
        'y1b2':['2023 WH-K VOLUME','2022 WH-K VOLUME','WH-K VOLUME 5 yr Avg','WH-K VOLUME 10 yr Avg','SMA10_WH-K_Vol_5yr',
                'SMA20_WH-K_Vol_5yr','SMA10_WH-K_Vol_10yr','SMA20_WH-K_Vol_10yr'],
        'y1b3':['2018 WH-K VOLUME','2019 WH-K VOLUME','2020 WH-K VOLUME','2021 WH-K VOLUME',
                '2022 WH-K VOLUME','2023 WH-K VOLUME','WH-K VOLUME 5 yr Avg','WH-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 WH OpenInt','2022 WH OpenInt','WH OpenInt 5 yr Avg','WH OpenInt 10 yr Avg'],
        'y2b2':['2023 WH OpenInt','2022 WH OpenInt','WH OpenInt 5 yr Avg','WH OpenInt 10 yr Avg','SMA10_WH_OpenInt_5yr',
                'SMA20_WH_OpenInt_5yr','SMA10_WH_OpenInt_10yr','SMA20_WH_OpenInt_10yr'],
        'y2b3':['2018 WH OpenInt','2019 WH OpenInt','2020 WH OpenInt','2021 WH OpenInt',
                '2022 WH OpenInt','2023 WH OpenInt','WH OpenInt 5 yr Avg','WH OpenInt 10 yr Avg'],

        'y3b1':['2023 WH-K OpenInt Ratio','2022 WH-K OpenInt Ratio','WH-K OpenInt Ratio 5 yr Avg','WH-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 WH-K OpenInt Ratio','2022 WH-K OpenInt Ratio','WH-K OpenInt Ratio 5 yr Avg','WH-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 WH-K OpenInt Ratio','2019 WH-K OpenInt Ratio','2020 WH-K OpenInt Ratio','2021 WH-K OpenInt Ratio',
                '2022 WH-K OpenInt Ratio','2023 WH-K OpenInt Ratio','WH-K OpenInt Ratio 5 yr Avg','WH-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'WK-N': {
        'description':'SRW Mar-May',
        'data': WK_N_df,
        'y1a1':['2023 WK-N CLOSE','2022 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg'],
        'y2a1':['2023 WK-N CLOSE','2022 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg'],
        'y3a1':['2023 WK-N CLOSE','2022 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg'],
        'y1a2':['2023 WK-N CLOSE','2022 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg','SMA10_WK-N_Close_5yr',
                'SMA20_WK-N_Close_5yr','SMA10_WK-N_Close_10yr','SMA20_WK-N_Close_10yr'],
        'y2a2':['2023 WK-N CLOSE','2022 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg','SMA10_WK-N_Close_5yr',
                'SMA20_WK-N_Close_5yr','SMA10_WK-N_Close_10yr','SMA20_WK-N_Close_10yr'],
        'y3a2':['2023 WK-N CLOSE','2022 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg'],
        'y1a3':['2018 WK-N CLOSE','2019 WK-N CLOSE','2020 WK-N CLOSE','2021 WK-N CLOSE',
                '2022 WK-N CLOSE','2023 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg'],
        'y2a3':['2018 WK-N CLOSE','2019 WK-N CLOSE','2020 WK-N CLOSE','2021 WK-N CLOSE',
                '2022 WK-N CLOSE','2023 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg'],
        'y3a3':['2018 WK-N CLOSE','2019 WK-N CLOSE','2020 WK-N CLOSE','2021 WK-N CLOSE',
                '2022 WK-N CLOSE','2023 WK-N CLOSE','WK-N CLOSE 5 yr Avg','WK-N CLOSE 10 yr Avg'],

        
        'y1b1':['2023 WK-N VOLUME','2022 WK-N VOLUME','WK-N VOLUME 5 yr Avg','WK-N VOLUME 10 yr Avg'],
        'y1b2':['2023 WK-N VOLUME','2022 WK-N VOLUME','WK-N VOLUME 5 yr Avg','WK-N VOLUME 10 yr Avg','SMA10_WK-N_Vol_5yr',
                'SMA20_WK-N_Vol_5yr','SMA10_WK-N_Vol_10yr','SMA20_WK-N_Vol_10yr'],
        'y1b3':['2018 WK-N VOLUME','2019 WK-N VOLUME','2020 WK-N VOLUME','2021 WK-N VOLUME',
                '2022 WK-N VOLUME','2023 WK-N VOLUME','WK-N VOLUME 5 yr Avg','WK-N VOLUME 10 yr Avg'],
        
        'y2b1':['2023 WK OpenInt','2022 WK OpenInt','WK OpenInt 5 yr Avg','WK OpenInt 10 yr Avg'],
        'y2b2':['2023 WK OpenInt','2022 WK OpenInt','WK OpenInt 5 yr Avg','WK OpenInt 10 yr Avg','SMA10_WK_OpenInt_5yr',
                'SMA20_WK_OpenInt_5yr','SMA10_WK_OpenInt_10yr','SMA20_WK_OpenInt_10yr'],
        'y2b3':['2018 WK OpenInt','2019 WK OpenInt','2020 WK OpenInt','2021 WK OpenInt',
                '2022 WK OpenInt','2023 WK OpenInt','WK OpenInt 5 yr Avg','WK OpenInt 10 yr Avg'],

        'y3b1':['2023 WK-N OpenInt Ratio','2022 WK-N OpenInt Ratio','WK-N OpenInt Ratio 5 yr Avg','WK-N OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 WK-N OpenInt Ratio','2022 WK-N OpenInt Ratio','WK-N OpenInt Ratio 5 yr Avg','WK-N OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 WK-N OpenInt Ratio','2019 WK-N OpenInt Ratio','2020 WK-N OpenInt Ratio','2021 WK-N OpenInt Ratio',
                '2022 WK-N OpenInt Ratio','2023 WK-N OpenInt Ratio','WK-N OpenInt Ratio 5 yr Avg','WK-N OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
   'WN-U': {
        'description':'SRW May-Jul',
        'data': WN_U_df,
        'y1a1':['2023 WN-U CLOSE','2022 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg'],
        'y2a1':['2023 WN-U CLOSE','2022 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg'],
        'y3a1':['2023 WN-U CLOSE','2022 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg'],
        'y1a2':['2023 WN-U CLOSE','2022 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg','SMA10_WN-U_Close_5yr',
                'SMA20_WN-U_Close_5yr','SMA10_WN-U_Close_10yr','SMA20_WN-U_Close_10yr'],
        'y2a2':['2023 WN-U CLOSE','2022 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg','SMA10_WN-U_Close_5yr',
                'SMA20_WN-U_Close_5yr','SMA10_WN-U_Close_10yr','SMA20_WN-U_Close_10yr'],
        'y3a2':['2023 WN-U CLOSE','2022 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg'],
        'y1a3':['2018 WN-U CLOSE','2019 WN-U CLOSE','2020 WN-U CLOSE','2021 WN-U CLOSE',
                '2022 WN-U CLOSE','2023 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg'],
        'y2a3':['2018 WN-U CLOSE','2019 WN-U CLOSE','2020 WN-U CLOSE','2021 WN-U CLOSE',
                '2022 WN-U CLOSE','2023 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg'],
        'y3a3':['2018 WN-U CLOSE','2019 WN-U CLOSE','2020 WN-U CLOSE','2021 WN-U CLOSE',
                '2022 WN-U CLOSE','2023 WN-U CLOSE','WN-U CLOSE 5 yr Avg','WN-U CLOSE 10 yr Avg'],

        
        'y1b1':['2023 WN-U VOLUME','2022 WN-U VOLUME','WN-U VOLUME 5 yr Avg','WN-U VOLUME 10 yr Avg'],
        'y1b2':['2023 WN-U VOLUME','2022 WN-U VOLUME','WN-U VOLUME 5 yr Avg','WN-U VOLUME 10 yr Avg','SMA10_WN-U_Vol_5yr',
                'SMA20_WN-U_Vol_5yr','SMA10_WN-U_Vol_10yr','SMA20_WN-U_Vol_10yr'],
        'y1b3':['2018 WN-U VOLUME','2019 WN-U VOLUME','2020 WN-U VOLUME','2021 WN-U VOLUME',
                '2022 WN-U VOLUME','2023 WN-U VOLUME','WN-U VOLUME 5 yr Avg','WN-U VOLUME 10 yr Avg'],
        
        'y2b1':['2023 WN OpenInt','2022 WN OpenInt','WN OpenInt 5 yr Avg','WN OpenInt 10 yr Avg'],
        'y2b2':['2023 WN OpenInt','2022 WN OpenInt','WN OpenInt 5 yr Avg','WN OpenInt 10 yr Avg','SMA10_WN_OpenInt_5yr',
                'SMA20_WN_OpenInt_5yr','SMA10_WN_OpenInt_10yr','SMA20_WN_OpenInt_10yr'],
        'y2b3':['2018 WN OpenInt','2019 WN OpenInt','2020 WN OpenInt','2021 WN OpenInt',
                '2022 WN OpenInt','2023 WN OpenInt','WN OpenInt 5 yr Avg','WN OpenInt 10 yr Avg'],

        'y3b1':['2023 WN-U OpenInt Ratio','2022 WN-U OpenInt Ratio','WN-U OpenInt Ratio 5 yr Avg','WN-U OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 WN-U OpenInt Ratio','2022 WN-U OpenInt Ratio','WN-U OpenInt Ratio 5 yr Avg','WN-U OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 WN-U OpenInt Ratio','2019 WN-U OpenInt Ratio','2020 WN-U OpenInt Ratio','2021 WN-U OpenInt Ratio',
                '2022 WN-U OpenInt Ratio','2023 WN-U OpenInt Ratio','WN-U OpenInt Ratio 5 yr Avg','WN-U OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'WU-Z': {
        'description':'SRW Jul-Aug',
        'data': WU_Z_df,
        'y1a1':['2023 WU-Z CLOSE','2022 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg'],
        'y2a1':['2023 WU-Z CLOSE','2022 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg'],
        'y3a1':['2023 WU-Z CLOSE','2022 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg'],
        'y1a2':['2023 WU-Z CLOSE','2022 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg','SMA10_WU-Z_Close_5yr',
                'SMA20_WU-Z_Close_5yr','SMA10_WU-Z_Close_10yr','SMA20_WU-Z_Close_10yr'],
        'y2a2':['2023 WU-Z CLOSE','2022 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg','SMA10_WU-Z_Close_5yr',
                'SMA20_WU-Z_Close_5yr','SMA10_WU-Z_Close_10yr','SMA20_WU-Z_Close_10yr'],
        'y3a2':['2023 WU-Z CLOSE','2022 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg'],
        'y1a3':['2018 WU-Z CLOSE','2019 WU-Z CLOSE','2020 WU-Z CLOSE','2021 WU-Z CLOSE',
                '2022 WU-Z CLOSE','2023 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg'],
        'y2a3':['2018 WU-Z CLOSE','2019 WU-Z CLOSE','2020 WU-Z CLOSE','2021 WU-Z CLOSE',
                '2022 WU-Z CLOSE','2023 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg'],
        'y3a3':['2018 WU-Z CLOSE','2019 WU-Z CLOSE','2020 WU-Z CLOSE','2021 WU-Z CLOSE',
                '2022 WU-Z CLOSE','2023 WU-Z CLOSE','WU-Z CLOSE 5 yr Avg','WU-Z CLOSE 10 yr Avg'],

        
        'y1b1':['2023 WU-Z VOLUME','2022 WU-Z VOLUME','WU-Z VOLUME 5 yr Avg','WU-Z VOLUME 10 yr Avg'],
        'y1b2':['2023 WU-Z VOLUME','2022 WU-Z VOLUME','WU-Z VOLUME 5 yr Avg','WU-Z VOLUME 10 yr Avg','SMA10_WU-Z_Vol_5yr',
                'SMA20_WU-Z_Vol_5yr','SMA10_WU-Z_Vol_10yr','SMA20_WU-Z_Vol_10yr'],
        'y1b3':['2018 WU-Z VOLUME','2019 WU-Z VOLUME','2020 WU-Z VOLUME','2021 WU-Z VOLUME',
                '2022 WU-Z VOLUME','2023 WU-Z VOLUME','WU-Z VOLUME 5 yr Avg','WU-Z VOLUME 10 yr Avg'],
        
        'y2b1':['2023 WU OpenInt','2022 WU OpenInt','WU OpenInt 5 yr Avg','WU OpenInt 10 yr Avg'],
        'y2b2':['2023 WU OpenInt','2022 WU OpenInt','WU OpenInt 5 yr Avg','WU OpenInt 10 yr Avg','SMA10_WU_OpenInt_5yr',
                'SMA20_WU_OpenInt_5yr','SMA10_WU_OpenInt_10yr','SMA20_WU_OpenInt_10yr'],
        'y2b3':['2018 WU OpenInt','2019 WU OpenInt','2020 WU OpenInt','2021 WU OpenInt',
                '2022 WU OpenInt','2023 WU OpenInt','WU OpenInt 5 yr Avg','WU OpenInt 10 yr Avg'],

        'y3b1':['2023 WU-Z OpenInt Ratio','2022 WU-Z OpenInt Ratio','WU-Z OpenInt Ratio 5 yr Avg','WU-Z OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 WU-Z OpenInt Ratio','2022 WU-Z OpenInt Ratio','WU-Z OpenInt Ratio 5 yr Avg','WU-Z OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 WU-Z OpenInt Ratio','2019 WU-Z OpenInt Ratio','2020 WU-Z OpenInt Ratio','2021 WU-Z OpenInt Ratio',
                '2022 WU-Z OpenInt Ratio','2023 WU-Z OpenInt Ratio','WU-Z OpenInt Ratio 5 yr Avg','WU-Z OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },

       'WZ-H': {
        'description':'SRW Aug-Sep',
        'data': WZ_H_df,
        'y1a1':['2023 WZ-H CLOSE','2022 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg'],
        'y2a1':['2023 WZ-H CLOSE','2022 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg'],
        'y3a1':['2023 WZ-H CLOSE','2022 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg'],
        'y1a2':['2023 WZ-H CLOSE','2022 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg','SMA10_WZ-H_Close_5yr',
                'SMA20_WZ-H_Close_5yr','SMA10_WZ-H_Close_10yr','SMA20_WZ-H_Close_10yr'],
        'y2a2':['2023 WZ-H CLOSE','2022 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg','SMA10_WZ-H_Close_5yr',
                'SMA20_WZ-H_Close_5yr','SMA10_WZ-H_Close_10yr','SMA20_WZ-H_Close_10yr'],
        'y3a2':['2023 WZ-H CLOSE','2022 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg'],
        'y1a3':['2018 WZ-H CLOSE','2019 WZ-H CLOSE','2020 WZ-H CLOSE','2021 WZ-H CLOSE',
                '2022 WZ-H CLOSE','2023 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg'],
        'y2a3':['2018 WZ-H CLOSE','2019 WZ-H CLOSE','2020 WZ-H CLOSE','2021 WZ-H CLOSE',
                '2022 WZ-H CLOSE','2023 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg'],
        'y3a3':['2018 WZ-H CLOSE','2019 WZ-H CLOSE','2020 WZ-H CLOSE','2021 WZ-H CLOSE',
                '2022 WZ-H CLOSE','2023 WZ-H CLOSE','WZ-H CLOSE 5 yr Avg','WZ-H CLOSE 10 yr Avg'],

        
        'y1b1':['2023 WZ-H VOLUME','2022 WZ-H VOLUME','WZ-H VOLUME 5 yr Avg','WZ-H VOLUME 10 yr Avg'],
        'y1b2':['2023 WZ-H VOLUME','2022 WZ-H VOLUME','WZ-H VOLUME 5 yr Avg','WZ-H VOLUME 10 yr Avg','SMA10_WZ-H_Vol_5yr',
                'SMA20_WZ-H_Vol_5yr','SMA10_WZ-H_Vol_10yr','SMA20_WZ-H_Vol_10yr'],
        'y1b3':['2018 WZ-H VOLUME','2019 WZ-H VOLUME','2020 WZ-H VOLUME','2021 WZ-H VOLUME',
                '2022 WZ-H VOLUME','2023 WZ-H VOLUME','WZ-H VOLUME 5 yr Avg','WZ-H VOLUME 10 yr Avg'],
        
        'y2b1':['2023 WZ OpenInt','2022 WZ OpenInt','WZ OpenInt 5 yr Avg','WZ OpenInt 10 yr Avg'],
        'y2b2':['2023 WZ OpenInt','2022 WZ OpenInt','WZ OpenInt 5 yr Avg','WZ OpenInt 10 yr Avg','SMA10_WZ_OpenInt_5yr',
                'SMA20_WZ_OpenInt_5yr','SMA10_WZ_OpenInt_10yr','SMA20_WZ_OpenInt_10yr'],
        'y2b3':['2018 WZ OpenInt','2019 WZ OpenInt','2020 WZ OpenInt','2021 WZ OpenInt',
                '2022 WZ OpenInt','2023 WZ OpenInt','WZ OpenInt 5 yr Avg','WZ OpenInt 10 yr Avg'],

        'y3b1':['2023 WZ-H OpenInt Ratio','2022 WZ-H OpenInt Ratio','WZ-H OpenInt Ratio 5 yr Avg','WZ-H OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 WZ-H OpenInt Ratio','2022 WZ-H OpenInt Ratio','WZ-H OpenInt Ratio 5 yr Avg','WZ-H OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 WZ-H OpenInt Ratio','2019 WZ-H OpenInt Ratio','2020 WZ-H OpenInt Ratio','2021 WZ-H OpenInt Ratio',
                '2022 WZ-H OpenInt Ratio','2023 WZ-H OpenInt Ratio','WZ-H OpenInt Ratio 5 yr Avg','WZ-H OpenInt Ratio 10 yr Avg'],

        
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
    ('WH-K','WK-N','WN-U','WU-Z','WZ-H'))

    st.write('Selected Spread:', SRW_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=SRW_spreads[spread]['y1a1']
    y1b=SRW_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=SRW_spreads[spread]['y1a2']
    y1b=SRW_spreads[spread]['y1b2']

    
else:
    y1a=SRW_spreads[spread]['y1a3']
    y1b=SRW_spreads[spread]['y1b3']
    
fig = px.line(SRW_spreads[spread]['data'], x=SRW_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(SRW_spreads[spread]['data'], x=SRW_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

Subfig.add_traces(fig.data + fig2.data)
Subfig.layout.xaxis.title="Date"
Subfig.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig.layout.yaxis2.title="Spread Volume"
Subfig.layout.title=titletxt

Subfig.update_layout(
    title = SRW_spreads[spread]['description']+"  Spread Price Vs Volume",
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
    y2a=SRW_spreads[spread]['y2a1']
    y2b=SRW_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=SRW_spreads[spread]['y2a2']
    y2b=SRW_spreads[spread]['y2b2']
    
    
else:
    y2a=SRW_spreads[spread]['y2a3']
    y2b=SRW_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
Subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(SRW_spreads[spread]['data'], x=SRW_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(SRW_spreads[spread]['data'], x=SRW_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

Subfig1.add_traces(fig1.data + fig12.data)
Subfig1.layout.xaxis.title="Date"
Subfig1.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig1.layout.yaxis2.title="Open Interest"
Subfig1.layout.title=titletxt1

Subfig1.update_layout(
    title = SRW_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    y3a=SRW_spreads[spread]['y3a1']
    y3b=SRW_spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=SRW_spreads[spread]['y3a2']
    y3b=SRW_spreads[spread]['y3b2']
    
    
else:
    y3a=SRW_spreads[spread]['y3a3']
    y3b=SRW_spreads[spread]['y3b3']

titletxt3='Price & Open Interest Ratio'
Subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(SRW_spreads[spread]['data'], x=SRW_spreads[spread]['x_value'], y=y3a, title=titletxt3)
fig12 = px.line(SRW_spreads[spread]['data'], x=SRW_spreads[spread]['x_value'], y=y3b, title=titletxt3)



fig12.update_traces(yaxis="y2")

Subfig2.add_traces(fig1.data + fig12.data)
Subfig2.layout.xaxis.title="Date"
Subfig2.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig2.layout.yaxis2.title="Open Interest Ratio"
Subfig2.layout.title=titletxt3

Subfig2.update_layout(
    title = SRW_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    
    

     



