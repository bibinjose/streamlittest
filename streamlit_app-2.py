"""
#App to find patterns in Corn spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
#CZ_df=pd.read_excel("Full_data1.xlsx")


CU_Z_df=pd.read_excel("full_data_2.xlsx",sheet_name='CU-Z')
CZ_H_df=pd.read_excel("full_data_2.xlsx",sheet_name='CZ-H')
CN_U_df=pd.read_excel("full_data_2.xlsx",sheet_name='CN-U')
CK_N_df=pd.read_excel("full_data_2.xlsx",sheet_name='CK-N')
CH_K_df=pd.read_excel("full_data_2.xlsx",sheet_name='CH-K')

corn_spreads = { 
    'CU-Z': {
        'data': CU_Z_df,
        'y1a1':['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y1a2':['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_5yr',
                'SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr'],
        'y1a3':['2018 CU-Z CLOSE','2019 CU-Z CLOSE','2020 CU-Z CLOSE','2021 CU-Z CLOSE',
                '2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg'],
        'y1b1':['2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg'],
        'y1b2':['2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg','SMA10_CU-Z_Vol_5yr',
                'SMA20_CU-Z_Vol_5yr','SMA10_CU-Z_Vol_10yr','SMA20_CU-Z_Vol_10yr'],
        'y1b3':['2018 CU-Z VOLUME','2019 CU-Z VOLUME','2020 CU-Z VOLUME','2021 CU-Z VOLUME',
                '2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg'],
        'y2a1':['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg'],
        'y2b1':['2022 CU OpenInt','CU OpenInt 5 yr Avg','CU OpenInt 10 yr Avg'],
        'y2a2':['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_5yr',
                'SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr'],
        'y2b2':['2022 CU OpenInt','CU OpenInt 5 yr Avg','CU OpenInt 10 yr Avg','SMA10_CU_OpenInt_5yr',
                'SMA20_CU_OpenInt_5yr','SMA10_CU_OpenInt_10yr','SMA20_CU_OpenInt_10yr'],
        'y2a3':['2018 CU-Z CLOSE','2019 CU-Z CLOSE','2020 CU-Z CLOSE','2021 CU-Z CLOSE',
                '2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg'],
        'y2b3':['2018 CU OpenInt','2019 CU OpenInt','2020 CU OpenInt','2021 CU OpenInt',
                '2022 CU OpenInt','CU OpenInt 5 yr Avg'],
        'x_value':'2022 Dates'
        
    },
    'CZ-H': {
        'data': CZ_H_df,
        'y1a1':['2021 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y1a2':['2021 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg','SMA10_CZ-H_Close_5yr',
                'SMA20_CZ-H_Close_5yr','SMA10_CZ-H_Close_10yr','SMA20_CZ-H_Close_10yr'],
        'y1a3':['2017 CZ-H CLOSE','2018 CZ-H CLOSE','2019 CZ-H CLOSE','2020 CZ-H CLOSE',
                '2021 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg'],
        'y1b1':['2021 CZ-H VOLUME','CZ-H VOLUME 5 yr Avg','CZ-H VOLUME 10 yr Avg'],
        'y1b2':['2021 CZ-H VOLUME','CZ-H VOLUME 5 yr Avg','CZ-H VOLUME 10 yr Avg','SMA10_CZ-H_Vol_5yr',
                'SMA20_CZ-H_Vol_5yr','SMA10_CZ-H_Vol_10yr','SMA20_CZ-H_Vol_10yr'],
        'y1b3':['2017 CZ-H VOLUME','2018 CZ-H VOLUME','2019 CZ-H VOLUME','2020 CZ-H VOLUME',
                '2021 CZ-H VOLUME','CZ-H VOLUME 5 yr Avg'],
        'y2a1':['2021 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg'],
        'y2b1':['2021 CZ OpenInt','CZ OpenInt 5 yr Avg','CZ OpenInt 10 yr Avg'],
        'y2a2':['2021 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg','CZ-H CLOSE 10 yr Avg','SMA10_CZ-H_Close_5yr',
                'SMA20_CZ-H_Close_5yr','SMA10_CZ-H_Close_10yr','SMA20_CZ-H_Close_10yr'],
        'y2b2':['2021 CZ OpenInt','CZ OpenInt 5 yr Avg','CZ OpenInt 10 yr Avg','SMA10_CZ_OpenInt_5yr',
                'SMA20_CZ_OpenInt_5yr','SMA10_CZ_OpenInt_10yr','SMA20_CZ_OpenInt_10yr'],
        'y2a3':['2017 CZ-H CLOSE','2018 CZ-H CLOSE','2019 CZ-H CLOSE','2020 CZ-H CLOSE',
                '2021 CZ-H CLOSE','CZ-H CLOSE 5 yr Avg'],
        'y2b3':['2017 CZ OpenInt','2018 CZ OpenInt','2019 CZ OpenInt','2020 CZ OpenInt',
                '2021 CZ OpenInt','CZ OpenInt 5 yr Avg'],
        'x_value':'2021 Dates'
        
    },
    'CN-U': {
        'data': CN_U_df,
        'y1a1':['2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y1a2':['2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg','SMA10_CN-U_Close_5yr',
                'SMA20_CN-U_Close_5yr','SMA10_CN-U_Close_10yr','SMA20_CN-U_Close_10yr'],
        'y1a3':['2018 CN-U CLOSE','2019 CN-U CLOSE','2020 CN-U CLOSE','2021 CN-U CLOSE',
                '2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg'],
        'y1b1':['2022 CN-U VOLUME','CN-U VOLUME 5 yr Avg','CN-U VOLUME 10 yr Avg'],
        'y1b2':['2022 CN-U VOLUME','CN-U VOLUME 5 yr Avg','CN-U VOLUME 10 yr Avg','SMA10_CN-U_Vol_5yr',
                'SMA20_CN-U_Vol_5yr','SMA10_CN-U_Vol_10yr','SMA20_CN-U_Vol_10yr'],
        'y1b3':['2018 CN-U VOLUME','2019 CN-U VOLUME','2020 CN-U VOLUME','2021 CN-U VOLUME',
                '2022 CN-U VOLUME','CN-U VOLUME 5 yr Avg'],
        'y2a1':['2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg'],
        'y2b1':['2022 CN OpenInt','CN OpenInt 5 yr Avg','CN OpenInt 10 yr Avg'],
        'y2a2':['2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg','CN-U CLOSE 10 yr Avg','SMA10_CN-U_Close_5yr',
                'SMA20_CN-U_Close_5yr','SMA10_CN-U_Close_10yr','SMA20_CN-U_Close_10yr'],
        'y2b2':['2022 CN OpenInt','CN OpenInt 5 yr Avg','CN OpenInt 10 yr Avg','SMA10_CN_OpenInt_5yr',
                'SMA20_CN_OpenInt_5yr','SMA10_CN_OpenInt_10yr','SMA20_CN_OpenInt_10yr'],
        'y2a3':['2018 CN-U CLOSE','2019 CN-U CLOSE','2020 CN-U CLOSE','2021 CN-U CLOSE',
                '2022 CN-U CLOSE','CN-U CLOSE 5 yr Avg'],
        'y2b3':['2018 CN OpenInt','2019 CN OpenInt','2020 CN OpenInt','2021 CN OpenInt',
                '2022 CN OpenInt','CN OpenInt 5 yr Avg'],
        'x_value':'2022 Dates'
        
    },
    'CK-N': {
        'data': CK_N_df,
        'y1a1':['2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y1a2':['2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg','SMA10_CK-N_Close_5yr',
                'SMA20_CK-N_Close_5yr','SMA10_CK-N_Close_10yr','SMA20_CK-N_Close_10yr'],
        'y1a3':['2018 CK-N CLOSE','2019 CK-N CLOSE','2020 CK-N CLOSE','2021 CK-N CLOSE',
                '2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg'],
        'y1b1':['2022 CK-N VOLUME','CK-N VOLUME 5 yr Avg','CK-N VOLUME 10 yr Avg'],
        'y1b2':['2022 CK-N VOLUME','CK-N VOLUME 5 yr Avg','CK-N VOLUME 10 yr Avg','SMA10_CK-N_Vol_5yr',
                'SMA20_CK-N_Vol_5yr','SMA10_CK-N_Vol_10yr','SMA20_CK-N_Vol_10yr'],
        'y1b3':['2018 CK-N VOLUME','2019 CK-N VOLUME','2020 CK-N VOLUME','2021 CK-N VOLUME',
                '2022 CK-N VOLUME','CK-N VOLUME 5 yr Avg'],
        'y2a1':['2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg'],
        'y2b1':['2022 CK OpenInt','CK OpenInt 5 yr Avg','CK OpenInt 10 yr Avg'],
        'y2a2':['2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg','CK-N CLOSE 10 yr Avg','SMA10_CK-N_Close_5yr',
                'SMA20_CK-N_Close_5yr','SMA10_CK-N_Close_10yr','SMA20_CK-N_Close_10yr'],
        'y2b2':['2022 CK OpenInt','CK OpenInt 5 yr Avg','CK OpenInt 10 yr Avg','SMA10_CK_OpenInt_5yr',
                'SMA20_CK_OpenInt_5yr','SMA10_CK_OpenInt_10yr','SMA20_CK_OpenInt_10yr'],
        'y2a3':['2018 CK-N CLOSE','2019 CK-N CLOSE','2020 CK-N CLOSE','2021 CK-N CLOSE',
                '2022 CK-N CLOSE','CK-N CLOSE 5 yr Avg'],
        'y2b3':['2018 CK OpenInt','2019 CK OpenInt','2020 CK OpenInt','2021 CK OpenInt',
                '2022 CK OpenInt','CK OpenInt 5 yr Avg'],
        'x_value':'2022 Dates'
            },
    'CH-K': {
        'data': CH_K_df,
        'y1a1':['2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y1a2':['2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg','SMA10_CH-K_Close_5yr',
                'SMA20_CH-K_Close_5yr','SMA10_CH-K_Close_10yr','SMA20_CH-K_Close_10yr'],
        'y1a3':['2018 CH-K CLOSE','2019 CH-K CLOSE','2020 CH-K CLOSE','2021 CH-K CLOSE',
                '2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg'],
        'y1b1':['2022 CH-K VOLUME','CH-K VOLUME 5 yr Avg','CH-K VOLUME 10 yr Avg'],
        'y1b2':['2022 CH-K VOLUME','CH-K VOLUME 5 yr Avg','CH-K VOLUME 10 yr Avg','SMA10_CH-K_Vol_5yr',
                'SMA20_CH-K_Vol_5yr','SMA10_CH-K_Vol_10yr','SMA20_CH-K_Vol_10yr'],
        'y1b3':['2018 CH-K VOLUME','2019 CH-K VOLUME','2020 CH-K VOLUME','2021 CH-K VOLUME',
                '2022 CH-K VOLUME','CH-K VOLUME 5 yr Avg'],
        'y2a1':['2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg'],
        'y2b1':['2022 CH OpenInt','CH OpenInt 5 yr Avg','CH OpenInt 10 yr Avg'],
        'y2a2':['2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg','CH-K CLOSE 10 yr Avg','SMA10_CH-K_Close_5yr',
                'SMA20_CH-K_Close_5yr','SMA10_CH-K_Close_10yr','SMA20_CH-K_Close_10yr'],
        'y2b2':['2022 CH OpenInt','CH OpenInt 5 yr Avg','CH OpenInt 10 yr Avg','SMA10_CH_OpenInt_5yr',
                'SMA20_CH_OpenInt_5yr','SMA10_CH_OpenInt_10yr','SMA20_CH_OpenInt_10yr'],
        'y2a3':['2018 CH-K CLOSE','2019 CH-K CLOSE','2020 CH-K CLOSE','2021 CH-K CLOSE',
                '2022 CH-K CLOSE','CH-K CLOSE 5 yr Avg'],
        'y2b3':['2018 CH OpenInt','2019 CH OpenInt','2020 CH OpenInt','2021 CH OpenInt',
                '2022 CH OpenInt','CH OpenInt 5 yr Avg'],
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


st.set_page_config(page_title=" Corn Spreads ",layout="wide")



with st.sidebar.container():
    spread = st.selectbox(
    'Select your spread',
    ('CU-Z', 'CZ-H', 'CN-U','CK-N','CH-K'))

    st.write('Selected Spread:', spread)
    selected_values = st.radio('Chart Value', ['Volume','Open Interest'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=corn_spreads[spread]['y1a1']
    y1b=corn_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=corn_spreads[spread]['y1a2']
    y1b=corn_spreads[spread]['y1b2']

    
else:
    y1a=corn_spreads[spread]['y1a3']
    y1b=corn_spreads[spread]['y1b3']
    
fig = px.line(corn_spreads[spread]['data'], x=corn_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(corn_spreads[spread]['data'], x=corn_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Date"
subfig.layout.yaxis.title="Spread Price"
#subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="Spread Volume"
subfig.layout.title=titletxt
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
    y2a=corn_spreads[spread]['y2a1']
    y2b=corn_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=corn_spreads[spread]['y2a2']
    y2b=corn_spreads[spread]['y2b2']
    
    
else:
    y2a=corn_spreads[spread]['y2a3']
    y2b=corn_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(corn_spreads[spread]['data'], x=corn_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(corn_spreads[spread]['data'], x=corn_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

subfig1.add_traces(fig1.data + fig12.data)
subfig1.layout.xaxis.title="Date"
subfig1.layout.yaxis.title="Spread Price"
#subfig.layout.yaxis2.type="log"
subfig1.layout.yaxis2.title="Open Interest"
subfig1.layout.title=titletxt1
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig1.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#subfig.show()

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


if selected_values=='Volume':
    subfig.update_layout(height=650,width=1200)
    st.plotly_chart(subfig,use_container_width = True,height=650,width=1200)
else:
    subfig1.update_layout(height=650,width=1200)
    st.plotly_chart(subfig1,use_container_width = True,height=650,width=1200)
    
    
with st.expander("Open comments"):

    # Show comments

    st.write("**Comments:**")
    for index, entry in enumerate(comments.itertuples()):
        st.markdown(COMMENT_TEMPLATE_MD.format(entry.user, entry.time, entry.comments))
        is_last = index == len(comments) - 1
        is_new = "just_posted" in st.session_state and is_last
        if is_new:
            st.success("Your comment was successfully posted.")
    space(2)
    st.write("**Add your own comment:**")
    form = st.form("comment")
    name = form.text_input("Name")
    comment = form.text_area("Comment")
    submit = form.form_submit_button("Add comment")
    df = pd.DataFrame({"user":[name], "time":[datetime.now().strftime("%d/%m/%Y %H:%M:%S")],"comments":comment})

    
    if submit:
        #date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        append_df_to_excel(df, r"comments.xlsx")
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()
     




