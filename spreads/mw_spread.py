"""
#App to find patterns in MW  spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
color_selected=px.colors.qualitative.Alphabet
st.set_page_config(page_title=" MW Spreads ",layout="wide")

MWEH_K_df=pd.read_excel("milling_wheat_spread_data.xlsx",sheet_name='MWEH-K')

MWEN_U_df=pd.read_excel("milling_wheat_spread_data.xlsx",sheet_name='MWEN-U')
MWEU_Z_df=pd.read_excel("milling_wheat_spread_data.xlsx",sheet_name='MWEU-Z')
MWEZ_H_df=pd.read_excel("milling_wheat_spread_data.xlsx",sheet_name='MWEZ-H')



MW_spreads = { 
    'MWEH-K': {
        'description':'MW Jan-Mar',
        'data': MWEH_K_df,
        'y1a1':['2023 MWEH-K CLOSE','2022 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg'],
        'y2a1':['2023 MWEH-K CLOSE','2022 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg'],
        'y3a1':['2023 MWEH-K CLOSE','2022 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg'],
        'y1a2':['2023 MWEH-K CLOSE','2022 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg','SMA10_MWEH-K_Close_5yr',
                'SMA20_MWEH-K_Close_5yr','SMA10_MWEH-K_Close_10yr','SMA20_MWEH-K_Close_10yr'],
        'y2a2':['2023 MWEH-K CLOSE','2022 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg','SMA10_MWEH-K_Close_5yr',
                'SMA20_MWEH-K_Close_5yr','SMA10_MWEH-K_Close_10yr','SMA20_MWEH-K_Close_10yr'],
        'y3a2':['2023 MWEH-K CLOSE','2022 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg'],
        'y1a3':['2018 MWEH-K CLOSE','2019 MWEH-K CLOSE','2020 MWEH-K CLOSE','2021 MWEH-K CLOSE',
                '2022 MWEH-K CLOSE','2023 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg'],
        'y2a3':['2018 MWEH-K CLOSE','2019 MWEH-K CLOSE','2020 MWEH-K CLOSE','2021 MWEH-K CLOSE',
                '2022 MWEH-K CLOSE','2023 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg'],
        'y3a3':['2018 MWEH-K CLOSE','2019 MWEH-K CLOSE','2020 MWEH-K CLOSE','2021 MWEH-K CLOSE',
                '2022 MWEH-K CLOSE','2023 MWEH-K CLOSE','MWEH-K CLOSE 5 yr Avg','MWEH-K CLOSE 10 yr Avg'],

        
        'y1b1':['2023 MWEH-K VOLUME','2022 MWEH-K VOLUME','MWEH-K VOLUME 5 yr Avg','MWEH-K VOLUME 10 yr Avg'],
        'y1b2':['2023 MWEH-K VOLUME','2022 MWEH-K VOLUME','MWEH-K VOLUME 5 yr Avg','MWEH-K VOLUME 10 yr Avg','SMA10_MWEH-K_Vol_5yr',
                'SMA20_MWEH-K_Vol_5yr','SMA10_MWEH-K_Vol_10yr','SMA20_MWEH-K_Vol_10yr'],
        'y1b3':['2018 MWEH-K VOLUME','2019 MWEH-K VOLUME','2020 MWEH-K VOLUME','2021 MWEH-K VOLUME',
                '2022 MWEH-K VOLUME','2023 MWEH-K VOLUME','MWEH-K VOLUME 5 yr Avg','MWEH-K VOLUME 10 yr Avg'],
        
        'y2b1':['2023 MWEH OpenInt','2022 MWEH OpenInt','MWEH OpenInt 5 yr Avg','MWEH OpenInt 10 yr Avg'],
        'y2b2':['2023 MWEH OpenInt','2022 MWEH OpenInt','MWEH OpenInt 5 yr Avg','MWEH OpenInt 10 yr Avg','SMA10_MWEH_OpenInt_5yr',
                'SMA20_MWEH_OpenInt_5yr','SMA10_MWEH_OpenInt_10yr','SMA20_MWEH_OpenInt_10yr'],
        'y2b3':['2018 MWEH OpenInt','2019 MWEH OpenInt','2020 MWEH OpenInt','2021 MWEH OpenInt',
                '2022 MWEH OpenInt','2023 MWEH OpenInt','MWEH OpenInt 5 yr Avg','MWEH OpenInt 10 yr Avg'],

        'y3b1':['2023 MWEH-K OpenInt Ratio','2022 MWEH-K OpenInt Ratio','MWEH-K OpenInt Ratio 5 yr Avg','MWEH-K OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 MWEH-K OpenInt Ratio','2022 MWEH-K OpenInt Ratio','MWEH-K OpenInt Ratio 5 yr Avg','MWEH-K OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 MWEH-K OpenInt Ratio','2019 MWEH-K OpenInt Ratio','2020 MWEH-K OpenInt Ratio','2021 MWEH-K OpenInt Ratio',
                '2022 MWEH-K OpenInt Ratio','2023 MWEH-K OpenInt Ratio','MWEH-K OpenInt Ratio 5 yr Avg','MWEH-K OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
   
   'MWEN-U': {
        'description':'MW May-Jul',
        'data': MWEN_U_df,
        'y1a1':['2023 MWEN-U CLOSE','2022 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg'],
        'y2a1':['2023 MWEN-U CLOSE','2022 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg'],
        'y3a1':['2023 MWEN-U CLOSE','2022 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg'],
        'y1a2':['2023 MWEN-U CLOSE','2022 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg','SMA10_MWEN-U_Close_5yr',
                'SMA20_MWEN-U_Close_5yr','SMA10_MWEN-U_Close_10yr','SMA20_MWEN-U_Close_10yr'],
        'y2a2':['2023 MWEN-U CLOSE','2022 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg','SMA10_MWEN-U_Close_5yr',
                'SMA20_MWEN-U_Close_5yr','SMA10_MWEN-U_Close_10yr','SMA20_MWEN-U_Close_10yr'],
        'y3a2':['2023 MWEN-U CLOSE','2022 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg'],
        'y1a3':['2018 MWEN-U CLOSE','2019 MWEN-U CLOSE','2020 MWEN-U CLOSE','2021 MWEN-U CLOSE',
                '2022 MWEN-U CLOSE','2023 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg'],
        'y2a3':['2018 MWEN-U CLOSE','2019 MWEN-U CLOSE','2020 MWEN-U CLOSE','2021 MWEN-U CLOSE',
                '2022 MWEN-U CLOSE','2023 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg'],
        'y3a3':['2018 MWEN-U CLOSE','2019 MWEN-U CLOSE','2020 MWEN-U CLOSE','2021 MWEN-U CLOSE',
                '2022 MWEN-U CLOSE','2023 MWEN-U CLOSE','MWEN-U CLOSE 5 yr Avg','MWEN-U CLOSE 10 yr Avg'],

        
        'y1b1':['2023 MWEN-U VOLUME','2022 MWEN-U VOLUME','MWEN-U VOLUME 5 yr Avg','MWEN-U VOLUME 10 yr Avg'],
        'y1b2':['2023 MWEN-U VOLUME','2022 MWEN-U VOLUME','MWEN-U VOLUME 5 yr Avg','MWEN-U VOLUME 10 yr Avg','SMA10_MWEN-U_Vol_5yr',
                'SMA20_MWEN-U_Vol_5yr','SMA10_MWEN-U_Vol_10yr','SMA20_MWEN-U_Vol_10yr'],
        'y1b3':['2018 MWEN-U VOLUME','2019 MWEN-U VOLUME','2020 MWEN-U VOLUME','2021 MWEN-U VOLUME',
                '2022 MWEN-U VOLUME','2023 MWEN-U VOLUME','MWEN-U VOLUME 5 yr Avg','MWEN-U VOLUME 10 yr Avg'],
        
        'y2b1':['2023 MWEN OpenInt','2022 MWEN OpenInt','MWEN OpenInt 5 yr Avg','MWEN OpenInt 10 yr Avg'],
        'y2b2':['2023 MWEN OpenInt','2022 MWEN OpenInt','MWEN OpenInt 5 yr Avg','MWEN OpenInt 10 yr Avg','SMA10_MWEN_OpenInt_5yr',
                'SMA20_MWEN_OpenInt_5yr','SMA10_MWEN_OpenInt_10yr','SMA20_MWEN_OpenInt_10yr'],
        'y2b3':['2018 MWEN OpenInt','2019 MWEN OpenInt','2020 MWEN OpenInt','2021 MWEN OpenInt',
                '2022 MWEN OpenInt','2023 MWEN OpenInt','MWEN OpenInt 5 yr Avg','MWEN OpenInt 10 yr Avg'],

        'y3b1':['2023 MWEN-U OpenInt Ratio','2022 MWEN-U OpenInt Ratio','MWEN-U OpenInt Ratio 5 yr Avg','MWEN-U OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 MWEN-U OpenInt Ratio','2022 MWEN-U OpenInt Ratio','MWEN-U OpenInt Ratio 5 yr Avg','MWEN-U OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 MWEN-U OpenInt Ratio','2019 MWEN-U OpenInt Ratio','2020 MWEN-U OpenInt Ratio','2021 MWEN-U OpenInt Ratio',
                '2022 MWEN-U OpenInt Ratio','2023 MWEN-U OpenInt Ratio','MWEN-U OpenInt Ratio 5 yr Avg','MWEN-U OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },
    'MWEU-Z': {
        'description':'MW Jul-Aug',
        'data': MWEU_Z_df,
        'y1a1':['2023 MWEU-Z CLOSE','2022 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg'],
        'y2a1':['2023 MWEU-Z CLOSE','2022 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg'],
        'y3a1':['2023 MWEU-Z CLOSE','2022 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg'],
        'y1a2':['2023 MWEU-Z CLOSE','2022 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg','SMA10_MWEU-Z_Close_5yr',
                'SMA20_MWEU-Z_Close_5yr','SMA10_MWEU-Z_Close_10yr','SMA20_MWEU-Z_Close_10yr'],
        'y2a2':['2023 MWEU-Z CLOSE','2022 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg','SMA10_MWEU-Z_Close_5yr',
                'SMA20_MWEU-Z_Close_5yr','SMA10_MWEU-Z_Close_10yr','SMA20_MWEU-Z_Close_10yr'],
        'y3a2':['2023 MWEU-Z CLOSE','2022 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg'],
        'y1a3':['2018 MWEU-Z CLOSE','2019 MWEU-Z CLOSE','2020 MWEU-Z CLOSE','2021 MWEU-Z CLOSE',
                '2022 MWEU-Z CLOSE','2023 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg'],
        'y2a3':['2018 MWEU-Z CLOSE','2019 MWEU-Z CLOSE','2020 MWEU-Z CLOSE','2021 MWEU-Z CLOSE',
                '2022 MWEU-Z CLOSE','2023 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg'],
        'y3a3':['2018 MWEU-Z CLOSE','2019 MWEU-Z CLOSE','2020 MWEU-Z CLOSE','2021 MWEU-Z CLOSE',
                '2022 MWEU-Z CLOSE','2023 MWEU-Z CLOSE','MWEU-Z CLOSE 5 yr Avg','MWEU-Z CLOSE 10 yr Avg'],

        
        'y1b1':['2023 MWEU-Z VOLUME','2022 MWEU-Z VOLUME','MWEU-Z VOLUME 5 yr Avg','MWEU-Z VOLUME 10 yr Avg'],
        'y1b2':['2023 MWEU-Z VOLUME','2022 MWEU-Z VOLUME','MWEU-Z VOLUME 5 yr Avg','MWEU-Z VOLUME 10 yr Avg','SMA10_MWEU-Z_Vol_5yr',
                'SMA20_MWEU-Z_Vol_5yr','SMA10_MWEU-Z_Vol_10yr','SMA20_MWEU-Z_Vol_10yr'],
        'y1b3':['2018 MWEU-Z VOLUME','2019 MWEU-Z VOLUME','2020 MWEU-Z VOLUME','2021 MWEU-Z VOLUME',
                '2022 MWEU-Z VOLUME','2023 MWEU-Z VOLUME','MWEU-Z VOLUME 5 yr Avg','MWEU-Z VOLUME 10 yr Avg'],
        
        'y2b1':['2023 MWEU OpenInt','2022 MWEU OpenInt','MWEU OpenInt 5 yr Avg','MWEU OpenInt 10 yr Avg'],
        'y2b2':['2023 MWEU OpenInt','2022 MWEU OpenInt','MWEU OpenInt 5 yr Avg','MWEU OpenInt 10 yr Avg','SMA10_MWEU_OpenInt_5yr',
                'SMA20_MWEU_OpenInt_5yr','SMA10_MWEU_OpenInt_10yr','SMA20_MWEU_OpenInt_10yr'],
        'y2b3':['2018 MWEU OpenInt','2019 MWEU OpenInt','2020 MWEU OpenInt','2021 MWEU OpenInt',
                '2022 MWEU OpenInt','2023 MWEU OpenInt','MWEU OpenInt 5 yr Avg','MWEU OpenInt 10 yr Avg'],

        'y3b1':['2023 MWEU-Z OpenInt Ratio','2022 MWEU-Z OpenInt Ratio','MWEU-Z OpenInt Ratio 5 yr Avg','MWEU-Z OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 MWEU-Z OpenInt Ratio','2022 MWEU-Z OpenInt Ratio','MWEU-Z OpenInt Ratio 5 yr Avg','MWEU-Z OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 MWEU-Z OpenInt Ratio','2019 MWEU-Z OpenInt Ratio','2020 MWEU-Z OpenInt Ratio','2021 MWEU-Z OpenInt Ratio',
                '2022 MWEU-Z OpenInt Ratio','2023 MWEU-Z OpenInt Ratio','MWEU-Z OpenInt Ratio 5 yr Avg','MWEU-Z OpenInt Ratio 10 yr Avg'],

        
        'x_value':'current_dates'
    },

       'MWEZ-H': {
        'description':'MW Aug-Sep',
        'data': MWEZ_H_df,
        'y1a1':['2023 MWEZ-H CLOSE','2022 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg'],
        'y2a1':['2023 MWEZ-H CLOSE','2022 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg'],
        'y3a1':['2023 MWEZ-H CLOSE','2022 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg'],
        'y1a2':['2023 MWEZ-H CLOSE','2022 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg','SMA10_MWEZ-H_Close_5yr',
                'SMA20_MWEZ-H_Close_5yr','SMA10_MWEZ-H_Close_10yr','SMA20_MWEZ-H_Close_10yr'],
        'y2a2':['2023 MWEZ-H CLOSE','2022 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg','SMA10_MWEZ-H_Close_5yr',
                'SMA20_MWEZ-H_Close_5yr','SMA10_MWEZ-H_Close_10yr','SMA20_MWEZ-H_Close_10yr'],
        'y3a2':['2023 MWEZ-H CLOSE','2022 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg'],
        'y1a3':['2018 MWEZ-H CLOSE','2019 MWEZ-H CLOSE','2020 MWEZ-H CLOSE','2021 MWEZ-H CLOSE',
                '2022 MWEZ-H CLOSE','2023 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg'],
        'y2a3':['2018 MWEZ-H CLOSE','2019 MWEZ-H CLOSE','2020 MWEZ-H CLOSE','2021 MWEZ-H CLOSE',
                '2022 MWEZ-H CLOSE','2023 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg'],
        'y3a3':['2018 MWEZ-H CLOSE','2019 MWEZ-H CLOSE','2020 MWEZ-H CLOSE','2021 MWEZ-H CLOSE',
                '2022 MWEZ-H CLOSE','2023 MWEZ-H CLOSE','MWEZ-H CLOSE 5 yr Avg','MWEZ-H CLOSE 10 yr Avg'],

        
        'y1b1':['2023 MWEZ-H VOLUME','2022 MWEZ-H VOLUME','MWEZ-H VOLUME 5 yr Avg','MWEZ-H VOLUME 10 yr Avg'],
        'y1b2':['2023 MWEZ-H VOLUME','2022 MWEZ-H VOLUME','MWEZ-H VOLUME 5 yr Avg','MWEZ-H VOLUME 10 yr Avg','SMA10_MWEZ-H_Vol_5yr',
                'SMA20_MWEZ-H_Vol_5yr','SMA10_MWEZ-H_Vol_10yr','SMA20_MWEZ-H_Vol_10yr'],
        'y1b3':['2018 MWEZ-H VOLUME','2019 MWEZ-H VOLUME','2020 MWEZ-H VOLUME','2021 MWEZ-H VOLUME',
                '2022 MWEZ-H VOLUME','2023 MWEZ-H VOLUME','MWEZ-H VOLUME 5 yr Avg','MWEZ-H VOLUME 10 yr Avg'],
        
        'y2b1':['2023 MWEZ OpenInt','2022 MWEZ OpenInt','MWEZ OpenInt 5 yr Avg','MWEZ OpenInt 10 yr Avg'],
        'y2b2':['2023 MWEZ OpenInt','2022 MWEZ OpenInt','MWEZ OpenInt 5 yr Avg','MWEZ OpenInt 10 yr Avg','SMA10_MWEZ_OpenInt_5yr',
                'SMA20_MWEZ_OpenInt_5yr','SMA10_MWEZ_OpenInt_10yr','SMA20_MWEZ_OpenInt_10yr'],
        'y2b3':['2018 MWEZ OpenInt','2019 MWEZ OpenInt','2020 MWEZ OpenInt','2021 MWEZ OpenInt',
                '2022 MWEZ OpenInt','2023 MWEZ OpenInt','MWEZ OpenInt 5 yr Avg','MWEZ OpenInt 10 yr Avg'],

        'y3b1':['2023 MWEZ-H OpenInt Ratio','2022 MWEZ-H OpenInt Ratio','MWEZ-H OpenInt Ratio 5 yr Avg','MWEZ-H OpenInt Ratio 10 yr Avg'],
        'y3b2':['2023 MWEZ-H OpenInt Ratio','2022 MWEZ-H OpenInt Ratio','MWEZ-H OpenInt Ratio 5 yr Avg','MWEZ-H OpenInt Ratio 10 yr Avg'],
        'y3b3':['2018 MWEZ-H OpenInt Ratio','2019 MWEZ-H OpenInt Ratio','2020 MWEZ-H OpenInt Ratio','2021 MWEZ-H OpenInt Ratio',
                '2022 MWEZ-H OpenInt Ratio','2023 MWEZ-H OpenInt Ratio','MWEZ-H OpenInt Ratio 5 yr Avg','MWEZ-H OpenInt Ratio 10 yr Avg'],

        
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
    ('MWEH-K','MWEK-N','MWEN-U','MWEU-Z','MWEZ-H'))

    st.write('Selected Spread:', MW_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest','Open Interest ratio'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=MW_spreads[spread]['y1a1']
    y1b=MW_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=MW_spreads[spread]['y1a2']
    y1b=MW_spreads[spread]['y1b2']

    
else:
    y1a=MW_spreads[spread]['y1a3']
    y1b=MW_spreads[spread]['y1b3']
    
fig = px.line(MW_spreads[spread]['data'], x=MW_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(MW_spreads[spread]['data'], x=MW_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

Subfig.add_traces(fig.data + fig2.data)
Subfig.layout.xaxis.title="Date"
Subfig.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig.layout.yaxis2.title="Spread Volume"
Subfig.layout.title=titletxt

Subfig.update_layout(
    title = MW_spreads[spread]['description']+"  Spread Price Vs Volume",
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
    y2a=MW_spreads[spread]['y2a1']
    y2b=MW_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=MW_spreads[spread]['y2a2']
    y2b=MW_spreads[spread]['y2b2']
    
    
else:
    y2a=MW_spreads[spread]['y2a3']
    y2b=MW_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
Subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(MW_spreads[spread]['data'], x=MW_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(MW_spreads[spread]['data'], x=MW_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

Subfig1.add_traces(fig1.data + fig12.data)
Subfig1.layout.xaxis.title="Date"
Subfig1.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig1.layout.yaxis2.title="Open Interest"
Subfig1.layout.title=titletxt1

Subfig1.update_layout(
    title = MW_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    y3a=MW_spreads[spread]['y3a1']
    y3b=MW_spreads[spread]['y3b1']

elif selected_graph=='Historic & Moving Avg':
    y3a=MW_spreads[spread]['y3a2']
    y3b=MW_spreads[spread]['y3b2']
    
    
else:
    y3a=MW_spreads[spread]['y3a3']
    y3b=MW_spreads[spread]['y3b3']

titletxt3='Price & Open Interest Ratio'
Subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(MW_spreads[spread]['data'], x=MW_spreads[spread]['x_value'], y=y3a, title=titletxt3)
fig12 = px.line(MW_spreads[spread]['data'], x=MW_spreads[spread]['x_value'], y=y3b, title=titletxt3)



fig12.update_traces(yaxis="y2")

Subfig2.add_traces(fig1.data + fig12.data)
Subfig2.layout.xaxis.title="Date"
Subfig2.layout.yaxis.title="Spread Price"
#Subfig.layout.yaxis2.type="log"
Subfig2.layout.yaxis2.title="Open Interest Ratio"
Subfig2.layout.title=titletxt3

Subfig2.update_layout(
    title = MW_spreads[spread]['description']+"  Spread Price Vs Open Interest",
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
    
    

     



