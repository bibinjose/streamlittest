"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
cu_df=pd.read_excel("Full_data.xlsx")
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
    selected_values = st.radio('Chart Value', ['Volume','Open Interest'], index = 0)
    selected_graph = st.radio('Chart Type', ['2022 and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    

if selected_graph=='2022 and Historic Avg':
    y1a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg']
    y1b=['2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg']

elif selected_graph=='Historic & Moving Avg':
    #y1a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_5yr','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr']
    #y1a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg']
    #y1b=['2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','SMA10_CU-Z_Vol_5yr','SMA20_CU-Z_Vol_5yr','CU-Z VOLUME 10 yr Avg','SMA10_CU-Z_Vol_10yr','SMA20_CU-Z_Vol_10yr']
    #y1b=['2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg']
    #y1a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg']
    #y1b=['2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg']
    y1a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_5yr','SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr']
    y1b=['2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg','CU-Z VOLUME 10 yr Avg','SMA10_CU-Z_Vol_5yr','SMA20_CU-Z_Vol_5yr','SMA10_CU-Z_Vol_10yr','SMA20_CU-Z_Vol_10yr']

    
else:
    y1a=['2018 CU-Z CLOSE','2019 CU-Z CLOSE','2020 CU-Z CLOSE','2021 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg']
    y1b=['2018 CU-Z VOLUME','2019 CU-Z VOLUME','2020 CU-Z VOLUME','2021 CU-Z VOLUME','2022 CU-Z VOLUME','CU-Z VOLUME 5 yr Avg']
    
fig = px.line(cu_df, x='2022 Dates', y=y1a, title=titletxt)
fig2 = px.line(cu_df, x='2022 Dates', y=y1b, title=titletxt)



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


if selected_graph=='2022 and Historic Avg':
    y2a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg']
    y2b=['2022 CU OpenInt','CU OpenInt 5 yr Avg','CU OpenInt 10 yr Avg']

elif selected_graph=='Historic & Moving Avg':
    #y2a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg']
    #y2a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_5yr','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr']
    
    #y2b=['2022 CU-Z OpenInt','CU-Z OpenInt 5 yr Avg']
    #y2b=['2022 CU-Z OpenInt','CU-Z OpenInt 5 yr Avg','SMA10_CU_OpenInt_5yr','SMA20_CU_OpenInt_5yr','CU-Z OpenInt 10 yr Avg','SMA10_CU_OpenInt_10yr','SMA20_CU_OpenInt_10yr']
    #y2a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_5yr','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr']
    #y2b=['2022 CU OpenInt','CU OpenInt 5 yr Avg','SMA10_CU_OpenInt_5yr']
    y2a=['2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg','CU-Z CLOSE 10 yr Avg','SMA10_CU-Z_Close_5yr','SMA20_CU-Z_Close_5yr','SMA10_CU-Z_Close_10yr','SMA20_CU-Z_Close_10yr']
    y2b=['2022 CU OpenInt','CU OpenInt 5 yr Avg','CU OpenInt 10 yr Avg','SMA10_CU_OpenInt_5yr','SMA20_CU_OpenInt_5yr','SMA10_CU_OpenInt_10yr','SMA20_CU_OpenInt_10yr']
    
    
else:
    y2a=['2018 CU-Z CLOSE','2019 CU-Z CLOSE','2020 CU-Z CLOSE','2021 CU-Z CLOSE','2022 CU-Z CLOSE','CU-Z CLOSE 5 yr Avg']
    y2b=['2018 CU OpenInt','2019 CU OpenInt','2020 CU OpenInt','2021 CU OpenInt','2022 CU OpenInt','CU OpenInt 5 yr Avg']

titletxt1='Price & Open Interest '
subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(cu_df, x='2022 Dates', y=y2a, title=titletxt)
fig12 = px.line(cu_df, x='2022 Dates', y=y2b, title=titletxt)



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
     




