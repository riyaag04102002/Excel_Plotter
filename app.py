import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import openpyxl 
import os

st.set_page_config(page_title='graphs')
st.header('Graph Plotter')

uploaded_files = st.sidebar.file_uploader('Choose a XLSX file', type='xlsx', accept_multiple_files=True)

for file in uploaded_files:    
    wb = openpyxl.load_workbook(file)
    sheet_selector = st.sidebar.selectbox("Select a Sheet: ", wb.sheetnames )
     
    for sheet in sheet_selector:
       df = pd.read_excel(file,sheet_selector, engine='openpyxl')


    st.write("File Uploaded: ", file.name)
    st.dataframe(df)

    title = st.write('I-V CURVE for :', file.name, "Sheet name: ")

    
    fig = px.line(
    df,
    x='Voltage (Volts)',
    y='Current (Amps)',
    template = 'plotly_white',
    title = title
    )
    st.plotly_chart(fig)

          
        
  






    



