import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "covid-cells.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "country_wise_latest.csv")

st.title("Dashboard - Covid Data")
img = image.imread(IMAGE_PATH)
st.image(img)
df = pd.read_csv(DATA_PATH)
st.dataframe(df)


# Create a choropleth map of confirmed cases by country
fig = px.choropleth(df, locations='Country/Region', locationmode='country names',
                    color='Confirmed', range_color=[0, max(df['Confirmed'])],
                    title='Confirmed Covid-19 Cases by Country')
st.plotly_chart(fig)

fig_1 = px.choropleth(df, locations='Country/Region', locationmode='country names',
                    color='Deaths', range_color=[0, max(df['Deaths'])],color_continuous_scale='Viridis',
                    title='Covid-19 Deaths by Country')

st.plotly_chart(fig_1)

fig_2 = px.choropleth(df, locations='Country/Region', locationmode='country names',
                    color='Recovered', range_color=[0, max(df['Recovered'])],color_continuous_scale='Turbo',
                    title='Recovered  by Country')

st.plotly_chart(fig_2)

countries = st.selectbox("Select the Country:", df['Country/Region'].unique())
columns_to_plot = ['Active', 'New cases', 'New deaths', 'New recovered']

# Filter the data for the selected country
selected_country = df[df["Country/Region"] == countries].iloc[:, -4:].T

# Create a bar plot of the selected columns for the selected country
fig_3 = px.bar(selected_country, y=list(selected_country.values.flatten()), x=columns_to_plot, title=f"{countries} - Covid-19 Data")
st.plotly_chart(fig_3)
