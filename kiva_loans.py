# Importing libraries
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

st.set_page_config(page_title='Kiva Loans Data Analysis', page_icon=None, layout="wide", initial_sidebar_state="expanded")

# App title and description
st.title('Streamlit App for :green[Kiva Loans Data Analysis]')
st.markdown('This app provides insights and visualizations on Kiva_loans data.')

# Loading of Kiva dataset
df = pd.read_csv('kiva_loans_original.csv')

# Display data
st.subheader(':green[Kiva_Loans Dataset]')
st.write(df.head())

st.write('')
st.write('')
st.subheader(':green[Loan Amounts by Country]')
loan_amounts_by_country = df.groupby('country')['funded_amount'].sum()

fig = px.bar(loan_amounts_by_country)
st.plotly_chart(fig, use_container_width=True)

st.subheader(':green[Loan Amounts by Sector]')
loan_amounts_by_sector = df.groupby('sector')['funded_amount'].sum()

fig = px.bar(loan_amounts_by_sector)
st.plotly_chart(fig, use_container_width=True)

st.subheader(':green[Loan Amounts by Activity]')
loan_amounts_by_activity = df.groupby('activity')['funded_amount'].sum()

fig1 = px.bar(loan_amounts_by_activity)
st.plotly_chart(fig1, use_container_width=True)

# Display sidebar with interactive widgets
st.sidebar.title('Filter Data')

selected_country = st.sidebar.selectbox('Select Country', df['country'].unique())
selected_sector = st.sidebar.selectbox('Select Sector', df['sector'].unique())
selected_activity = st.sidebar.selectbox('Select Activity', df['activity'].unique())
loan_amount_slider = st.sidebar.slider('funded_mount', min_value=0, max_value=100000, step=1000)
repayment_interval = st.sidebar.selectbox('Repayment Interval', df['repayment_interval'])
fig3 = st.sidebar.selectbox('From Map', df['repayment_interval'].unique())

filtered_df = df[(df['country'] == selected_country) & (df['repayment_interval'] == fig3) & (df['sector'] == selected_sector) & (df['activity'] == selected_activity) & (df['funded_amount'] <= loan_amount_slider)]

st.subheader(':green[Filtered Dataset Depending on Country and Funded_amount]')
st.dataframe(filtered_df)


st.sidebar.image('loan.png')
st.sidebar.markdown('# Make a loan, change a life')
st.sidebar.markdown(" With Kiva you can lend as little as $5 and make a big change in someone's life 😃")
st.sidebar.write('')
st.sidebar.markdown('#### Made with ❤️ by Dr. [Mohamed Thabit](https://youtu.be/8roZwJX9o1A)')

# Add map visualization
st.subheader('Loan Locations')
fig3 = px.scatter_mapbox(
    filtered_df, lat='funded_amount',
    lon='funded_amount',
    hover_name='country',
    hover_data=['sector', 'funded_amount'],
    color='funded_amount',
    color_continuous_scale='Viridis',
    size='funded_amount',
    size_max=15,
    zoom=1
)

fig3.update_layout(mapbox_style='open-street-map')
fig3.update_layout(margin={'r':0,'t':0,'l':0,'b':0})

st.plotly_chart(fig3)
