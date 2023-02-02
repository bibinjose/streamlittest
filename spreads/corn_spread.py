"""
#App to find patterns in Corn Meal spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
color_selected=px.colors.qualitative.Alphabet
st.set_page_config(page_title=" Corn Spreads ",layout="wide")

CH_K_df=pd.read_excel("Corn_spread_data.xlsx",sheet_name='CH-K')
CK_N_df=pd.read_excel("Corn_spread_data.xlsx",sheet_name='CK-N')
CN_U_df=pd.read_excel("Corn_spread_data.xlsx",sheet_name='CN-U')
CU_Z_df=pd.read_excel("Corn_spread_data.xlsx",sheet_name='CU-Z')
CZ_H_df=pd.read_excel("Corn_spread_data.xlsx",sheet_name='CZ-H')



Corn_spreads = { 
    'CH-K': {
        'description':'Corn Jan-Mar',
        'data': CH_K_df,
        'y1a1':['2023 CH-K CLOSE','2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y2a1':['2023 CH-K CLOSE','2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y3a1':['2023 CH-K CLOSE','2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y1a2':['2023 CH-K CLOSE','2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg','SMA10_CH-K_Close_5yr',
                'SMA20_CH-K_Close_5yr','SMA10_CH-K_Close_10yr','SMA20_CH-K_Close_10yr'],
        'y2a2':['2023 CH-K CLOSE','2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg','SMA10_CH-K_Close_5yr',
                'SMA20_CH-K_Close_5yr','SMA10_CH-K_Close_10yr','SMA20_CH-K_Close_10yr'],
        'y3a2':['2023 CH-K CLOSE','2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y1a3':['2018 CH-K CLOSE','2019 CH-K CLOSE','2020 CH-K CLOSE','2021 CH-K CLOSE',
                '2022 CH-K CLOSE','2023 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y2a3':['2018 CH-K CLOSE','2019 CH-K CLOSE','2020 CH-K CLOSE','2021 CH-K CLOSE',
                '2022 CH-K CLOSE','2023 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y3a3':['2018 CH-K CLOSE','2019 CH-K CLOSE','2020 CH-K CLOSE','2021 CH-K CLOSE',
                '2022 CH-K CLOSE','2023 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 CH-K VOLUME','2022 CH-K VOLUME','CH-K VOLUME 5 yr Avg','CH-K VOLUME 10 yr Avg'],
        'y1b2':['2023 CH-K VOLUME','2022 CH-K VOLUME','CH-K VOLUME 5 yr Avg','CH-K VOLUME 10 yr Avg','SMA10_CH-K_Vol_5yr',
                'SMA20_CH-K_Vol_5yr','SMA10_CH-K_Vol_10yr','SMA20_CH-K_Vol_10yr'],
        'y1b3':['2018 CH-K VOLUME','2019 CH-K VOLUME','2020 CH-K VOLUME','2021 CH-K VOLUME',
                '2022 CH-K VOLUME','2023 CH-K VOLUME','CH-K VOLUME 5 yr Avg','CH-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 CH OpenInt','2022 CH OpenInt','CH OpenInt 5 yr Avg','CH OpenInt 10 yr Avg'],
        'y2b2':['2023 CH OpenInt','2022 CH OpenInt','CH OpenInt 5 yr Avg','CH OpenInt 10 yr Avg','SMA10_CH_OpenInt_5yr',
                'SMA20_CH_OpenInt_5yr','SMA10_CH_OpenInt_10yr','SMA20_CH_OpenInt_10yr'],
        'y2b3':['2018 CH OpenInt','2019 CH OpenInt','2020 CH OpenInt','2021 CH OpenInt',
                '2022 CH OpenInt','2023 CH OpenInt','CH OpenInt 5 yr Avg','CH OpenInt 10 yr Avg'],

        'y3b1':['2023 CH-K OpenInt Ratio','2022 CH-K OpenInt Ratio','CH-K OpenInt Ratio 5 yr Avg','CH-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 CH-K OpenInt Ratio','2022 CH-K OpenInt Ratio','CH-K OpenInt Ratio 5 yr Avg','CH-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 CH-K OpenInt Ratio','2019 CH-K OpenInt Ratio','2020 CH-K OpenInt Ratio','2021 CH-K OpenInt Ratio',
                '2022 CH-K OpenInt Ratio','2023 CH-K OpenInt Ratio','CH-K OpenInt Ratio 5 yr Avg','CH-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'CK-N': {
        'description':'Corn Mar-May',
        'data': CK_N_df,
        'y1a1':['2023 CK-N CLOSE','2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y2a1':['2023 CK-N CLOSE','2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y3a1':['2023 CK-N CLOSE','2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y1a2':['2023 CK-N CLOSE','2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg','SMA10_CK-N_Close_5yr',
                'SMA20_CK-N_Close_5yr','SMA10_CK-N_Close_10yr','SMA20_CK-N_Close_10yr'],
        'y2a2':['2023 CK-N CLOSE','2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg','SMA10_CK-N_Close_5yr',
                'SMA20_CK-N_Close_5yr','SMA10_CK-N_Close_10yr','SMA20_CK-N_Close_10yr'],
        'y3a2':['2023 CK-N CLOSE','2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y1a3':['2018 CK-N CLOSE','2019 CK-N CLOSE','2020 CK-N CLOSE','2021 CK-N CLOSE',
                '2022 CK-N CLOSE','2023 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y2a3':['2018 CK-N CLOSE','2019 CK-N CLOSE','2020 CK-N CLOSE','2021 CK-N CLOSE',
                '2022 CK-N CLOSE','2023 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y3a3':['2018 CK-N CLOSE','2019 CK-N CLOSE','2020 CK-N CLOSE','2021 CK-N CLOSE',
                '2022 CK-N CLOSE','2023 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],

        
        'y1b1':['2023 CK-N VOLUME','2022 CK-N VOLUME','CK-N VOLUME 5 yr Avg','CK-N VOLUME 10 yr Avg'],
        'y1b2':['2023 CK-N VOLUME','2022 CK-N VOLUME','CK-N VOLUME 5 yr Avg','CK-N VOLUME 10 yr Avg','SMA10_CK-N_Vol_5yr',
                'SMA20_CK-N_Vol_5yr','SMA10_CK-N_Vol_10yr','SMA20_CK-N_Vol_10yr'],
        'y1b3':['2018 CK-N VOLUME','2019 CK-N VOLUME','2020 CK-N VOLUME','2021 CK-N VOLUME',
                '2022 CK-N VOLUME','2023 CK-N VOLUME','CK-N VOLUME 5 yr Avg','CK-N VOLUME 10 yr Avg'],
        
        'y2b1':['2023 CK OpenInt','2022 CK OpenInt','CK OpenInt 5 yr Avg','CK OpenInt 10 yr Avg'],
        'y2b2':['2023 CK OpenInt','2022 CK OpenInt','CK OpenInt 5 yr Avg','CK OpenInt 10 yr Avg','SMA10_CK_OpenInt_5yr',
                'SMA20_CK_OpenInt_5yr','SMA10_CK_OpenInt_10yr','SMA20_CK_OpenInt_10yr'],
        'y2b3':['2018 CK OpenInt','2019 CK OpenInt','2020 CK OpenInt','2021 CK OpenInt',
                '2022 CK OpenInt','2023 CK OpenInt','CK OpenInt 5 yr Avg','CK OpenInt 10 yr Avg'],

        'y3b1':['2023 CK-N OpenInt Ratio','2022 CK-N OpenInt Ratio','CK-N OpenInt Ratio 5 yr Avg','CK-N OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 CK-N OpenInt Ratio','2022 CK-N OpenInt Ratio','CK-N OpenInt Ratio 5 yr Avg','CK-N OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 CK-N OpenInt Ratio','2019 CK-N OpenInt Ratio','2020 CK-N OpenInt Ratio','2021 CK-N OpenInt Ratio',
                '2022 CK-N OpenInt Ratio','2023 CK-N OpenInt Ratio','CK-N OpenInt Ratio 5 yr Avg','CK-N OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
   'CN-U': {
        'description':'Corn May-Jul',
        'data': CN_U_df,
        'y1a1':['2023 CN-U CLOSE','2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y2a1':['2023 CN-U CLOSE','2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y3a1':['2023 CN-U CLOSE','2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y1a2':['2023 CN-U CLOSE','2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg','SMA10_CN-U_Close_5yr',
                'SMA20_CN-U_Close_5yr','SMA10_CN-U_Close_10yr','SMA20_CN-U_Close_10yr'],
        'y2a2':['2023 CN-U CLOSE','2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg','SMA10_CN-U_Close_5yr',
                'SMA20_CN-U_Close_5yr','SMA10_CN-U_Close_10yr','SMA20_CN-U_Close_10yr'],
        'y3a2':['2023 CN-U CLOSE','2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y1a3':['2018 CN-U CLOSE','2019 CN-U CLOSE','2020 CN-U CLOSE','2021 CN-U CLOSE',
                '2022 CN-U CLOSE','2023 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y2a3':['2018 CN-U CLOSE','2019 CN-U CLOSE','2020 CN-U CLOSE','2021 CN-U CLOSE',
                '2022 CN-U CLOSE','2023 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y3a3':['2018 CN-U CLOSE','2019 CN-U CLOSE','2020 CN-U CLOSE','2021 CN-U CLOSE',
                '2022 CN-U CLOSE','2023 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],

        
        'y1b1':['2023 CN-U VOLUME','2022 CN-U VOLUME','CN-U VOLUME 5 yr Avg','CN-U VOLUME 10 yr Avg'],
        'y1b2':['2023 CN-U VOLUME','2022 CN-U VOLUME','CN-U VOLUME 5 yr Avg','CN-U VOLUME 10 yr Avg','SMA10_CN-U_Vol_5yr',
                'SMA20_CN-U_Vol_5yr','SMA10_CN-U_Vol_10yr','SMA20_CN-U_Vol_10yr'],
        'y1b3':['2018 CN-U VOLUME','2019 CN-U VOLUME','2020 CN-U VOLUME','2021 CN-U VOLUME',
                '2022 CN-U VOLUME','2023 CN-U VOLUME','CN-U VOLUME 5 yr Avg','CN-U VOLUME 10 yr Avg'],
        
        'y2b1':['2023 CN OpenInt','2022 CN OpenInt','CN OpenInt 5 yr Avg','CN OpenInt 10 yr Avg'],
        'y2b2':['2023 CN OpenInt','2022 CN OpenInt','CN OpenInt 5 yr Avg','CN OpenInt 10 yr Avg','SMA10_CN_OpenInt_5yr',
                'SMA20_CN_OpenInt_5yr','SMA10_CN_OpenInt_10yr','SMA20_CN_OpenInt_10yr'],
        'y2b3':['2018 CN OpenInt','2019 CN OpenInt','2020 CN OpenInt','2021 CN OpenInt',
                '2022 CN OpenInt','2023 CN OpenInt','CN OpenInt 5 yr Avg','CN OpenInt 10 yr Avg'],

        'y3b1':['2023 CN-U OpenInt Ratio','2022 CN-U OpenInt Ratio','CN-U OpenInt Ratio 5 yr Avg','CN-U OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 CN-U OpenInt Ratio','2022 CN-U OpenInt Ratio','CN-U OpenInt Ratio 5 yr Avg','CN-U OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 CN-U OpenInt Ratio','2019 CN-U OpenInt Ratio','2020 CN-U OpenInt Ratio','2021 CN-U OpenInt Ratio',
                '2022 CN-U OpenInt Ratio','2023 CN-U OpenInt Ratio','CN-U OpenInt Ratio 5 yr Avg','CN-U OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'CU-Z': {
        'description':'Corn Jul-Aug',
        'data': CU_Z_df,
        'y1a1':['2023 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y2a1':['2023 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y3a1':['2023 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y1a2':['2023 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_5yr',
                'SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr'],
        'y2a2':['2023 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_5yr',
                'SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr'],
        'y3a2':['2023 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y1a3':['2018 CU-Z CLOSE','2019 CU-Z CLOSE','2020 CU-Z CLOSE','2021 CU-Z CLOSE',
                '2022 CU-Z CLOSE','2023 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y2a3':['2018 CU-Z CLOSE','2019 CU-Z CLOSE','2020 CU-Z CLOSE','2021 CU-Z CLOSE',
                '2022 CU-Z CLOSE','2023 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y3a3':['2018 CU-Z CLOSE','2019 CU-Z CLOSE','2020 CU-Z CLOSE','2021 CU-Z CLOSE',
                '2022 CU-Z CLOSE','2023 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],

        
        'y1b1':['2023 CU-Z VOLUME','2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg'],
        'y1b2':['2023 CU-Z VOLUME','2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg','SMA10_CU-Z_Vol_5yr',
                'SMA20_CU-Z_Vol_5yr','SMA10_CU-Z_Vol_10yr','SMA20_CU-Z_Vol_10yr'],
        'y1b3':['2018 CU-Z VOLUME','2019 CU-Z VOLUME','2020 CU-Z VOLUME','2021 CU-Z VOLUME',
                '2022 CU-Z VOLUME','2023 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg'],
        
        'y2b1':['2023 CU OpenInt','2022 CU OpenInt','CU OpenInt 5 yr Avg','CU OpenInt 10 yr Avg'],
        'y2b2':['2023 CU OpenInt','2022 CU OpenInt','CU OpenInt 5 yr Avg','CU OpenInt 10 yr Avg','SMA10_CU_OpenInt_5yr',
                'SMA20_CU_OpenInt_5yr','SMA10_CU_OpenInt_10yr','SMA20_CU_OpenInt_10yr'],
        'y2b3':['2018 CU OpenInt','2019 CU OpenInt','2020 CU OpenInt','2021 CU OpenInt',
                '2022 CU OpenInt','2023 CU OpenInt','CU OpenInt 5 yr Avg','CU OpenInt 10 yr Avg'],

        'y3b1':['2023 CU-Z OpenInt Ratio','2022 CU-Z OpenInt Ratio','CU-Z OpenInt Ratio 5 yr Avg','CU-Z OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 CU-Z OpenInt Ratio','2022 CU-Z OpenInt Ratio','CU-Z OpenInt Ratio 5 yr Avg','CU-Z OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 CU-Z OpenInt Ratio','2019 CU-Z OpenInt Ratio','2020 CU-Z OpenInt Ratio','2021 CU-Z OpenInt Ratio',
                '2022 CU-Z OpenInt Ratio','2023 CU-Z OpenInt Ratio','CU-Z OpenInt Ratio 5 yr Avg','CU-Z OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },

       'CZ-H': {
        'description':'Corn Aug-Sep',
        'data': CZ_H_df,
        'y1a1':['2023 CZ-H CLOSE','2022 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y2a1':['2023 CZ-H CLOSE','2022 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y3a1':['2023 CZ-H CLOSE','2022 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y1a2':['2023 CZ-H CLOSE','2022 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg','SMA10_CZ-H_Close_5yr',
                'SMA20_CZ-H_Close_5yr','SMA10_CZ-H_Close_10yr','SMA20_CZ-H_Close_10yr'],
        'y2a2':['2023 CZ-H CLOSE','2022 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg','SMA10_CZ-H_Close_5yr',
                'SMA20_CZ-H_Close_5yr','SMA10_CZ-H_Close_10yr','SMA20_CZ-H_Close_10yr'],
        'y3a2':['2023 CZ-H CLOSE','2022 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y1a3':['2018 CZ-H CLOSE','2019 CZ-H CLOSE','2020 CZ-H CLOSE','2021 CZ-H CLOSE',
                '2022 CZ-H CLOSE','2023 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y2a3':['2018 CZ-H CLOSE','2019 CZ-H CLOSE','2020 CZ-H CLOSE','2021 CZ-H CLOSE',
                '2022 CZ-H CLOSE','2023 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y3a3':['2018 CZ-H CLOSE','2019 CZ-H CLOSE','2020 CZ-H CLOSE','2021 CZ-H CLOSE',
                '2022 CZ-H CLOSE','2023 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],

        
        'y1b1':['2023 CZ-H VOLUME','2022 CZ-H VOLUME','CZ-H VOLUME 5 yr Avg','CZ-H VOLUME 10 yr Avg'],
        'y1b2':['2023 CZ-H VOLUME','2022 CZ-H VOLUME','CZ-H VOLUME 5 yr Avg','CZ-H VOLUME 10 yr Avg','SMA10_CZ-H_Vol_5yr',
                'SMA20_CZ-H_Vol_5yr','SMA10_CZ-H_Vol_10yr','SMA20_CZ-H_Vol_10yr'],
        'y1b3':['2018 CZ-H VOLUME','2019 CZ-H VOLUME','2020 CZ-H VOLUME','2021 CZ-H VOLUME',
                '2022 CZ-H VOLUME','2023 CZ-H VOLUME','CZ-H VOLUME 5 yr Avg','CZ-H VOLUME 10 yr Avg'],
        
        'y2b1':['2023 CZ OpenInt','2022 CZ OpenInt','CZ OpenInt 5 yr Avg','CZ OpenInt 10 yr Avg'],
        'y2b2':['2023 CZ OpenInt','2022 CZ OpenInt','CZ OpenInt 5 yr Avg','CZ OpenInt 10 yr Avg','SMA10_CZ_OpenInt_5yr',
                'SMA20_CZ_OpenInt_5yr','SMA10_CZ_OpenInt_10yr','SMA20_CZ_OpenInt_10yr'],
        'y2b3':['2018 CZ OpenInt','2019 CZ OpenInt','2020 CZ OpenInt','2021 CZ OpenInt',
                '2022 CZ OpenInt','2023 CZ OpenInt','CZ OpenInt 5 yr Avg','CZ OpenInt 10 yr Avg'],

        'y3b1':['2023 CZ-H OpenInt Ratio','2022 CZ-H OpenInt Ratio','CZ-H OpenInt Ratio 5 yr Avg','CZ-H OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 CZ-H OpenInt Ratio','2022 CZ-H OpenInt Ratio','CZ-H OpenInt Ratio 5 yr Avg','CZ-H OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 CZ-H OpenInt Ratio','2019 CZ-H OpenInt Ratio','2020 CZ-H OpenInt Ratio','2021 CZ-H OpenInt Ratio',
                '2022 CZ-H OpenInt Ratio','2023 CZ-H OpenInt Ratio','CZ-H OpenInt Ratio 5 yr Avg','CZ-H OpenInt Ratio 10 yr Avg'],

        
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
    ('CH-K','CK-N','CN-U','CU-Z','CZ-H'))

    st.write('Selected Spread:', Corn_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=Corn_spreads[spread]['y1a1']
    y1b=Corn_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=Corn_spreads[spread]['y1a2']
    y1b=Corn_spreads[spread]['y1b2']

    
else:
    y1a=Corn_spreads[spread]['y1a3']
    y1b=Corn_spreads[spread]['y1b3']
    
fig = px.line(Corn_spreads[spread]['data'], x=Corn_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(Corn_spreads[spread]['data'], x=Corn_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

Subfig.add_traces(fig.data + fig2.data)
Subfig.layout.xaxis.title="Date"
Subfig.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig.layout.yaxis2.title="Spread Volume"
Subfig.layout.title=titletxt

Subfig.update_layout(
    title = Corn_spreads[spread]['description']+"  Spread Price Vs Volume",
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
    y2a=Corn_spreads[spread]['y2a1']
    y2b=Corn_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=Corn_spreads[spread]['y2a2']
    y2b=Corn_spreads[spread]['y2b2']
    
    
else:
    y2a=Corn_spreads[spread]['y2a3']
    y2b=Corn_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
Subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(Corn_spreads[spread]['data'], x=Corn_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(Corn_spreads[spread]['data'], x=Corn_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

Subfig1.add_traces(fig1.data + fig12.data)
Subfig1.layout.xaxis.title="Date"
Subfig1.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig1.layout.yaxis2.title="Open Interest"
Subfig1.layout.title=titletxt1

Subfig1.update_layout(
    title = Corn_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    y3a=Corn_spreads[spread]['y3a1']
    y3b=Corn_spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=Corn_spreads[spread]['y3a2']
    y3b=Corn_spreads[spread]['y3b2']
    
    
else:
    y3a=Corn_spreads[spread]['y3a3']
    y3b=Corn_spreads[spread]['y3b3']

titletxt3='Price & Open Interest Ratio'
Subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(Corn_spreads[spread]['data'], x=Corn_spreads[spread]['x_value'], y=y3a, title=titletxt3)
fig12 = px.line(Corn_spreads[spread]['data'], x=Corn_spreads[spread]['x_value'], y=y3b, title=titletxt3)



fig12.update_traces(yaxis="y2")

Subfig2.add_traces(fig1.data + fig12.data)
Subfig2.layout.xaxis.title="Date"
Subfig2.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig2.layout.yaxis2.title="Open Interest Ratio"
Subfig2.layout.title=titletxt3

Subfig2.update_layout(
    title = Corn_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    
    

     



