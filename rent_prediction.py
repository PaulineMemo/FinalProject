from pydoc import describe
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide", initial_sidebar_state="expanded",
                   page_title='rent_prediction_App')
# set_page_config => https://github.com/streamlit/streamlit/issues/1770
st.title("Nairobi_House_Rent_Prediction")
st.write("The app predicts the rent for houses within Nairobi area")
path = "Nairobi_House_rent_data.csv"
data = st.sidebar.file_uploader("Upload Dataset", type=['csv', 'txt', 'xlsx'])
if data is not None:
    df = pd.read_csv('Nairobi_House_rent_data.csv')
    df.Bathrooms.replace("Missing", np.nan, inplace=True)
    df.Balcony.replace("Missing", np.nan, inplace=True)
    df['Build_up_area(sq.ft)'] = df['Build_up_area(sq.ft)'].str.split().str[0]
    df['Build_up_area(sq.ft)'] = df['Build_up_area(sq.ft)'].astype('int')
    df["Carpet_area(sq.ft)"].replace("Missing", 0, inplace=True)
    df['Carpet_area(sq.ft)'] = df['Carpet_area(sq.ft)'].str.split().str[0]

    def to_num(s):
        if type(s) == str:
            return int(s)
        else:
            return s
    df['Carpet_area(sq.ft)'] = df['Carpet_area(sq.ft)'].apply(to_num)
    df.drop('Carpet_area(sq.ft)', axis=1, inplace=True)
    df.Parking.mode()[0]
    df.Parking.fillna(df.Parking.mode()[0], inplace=True)
    df[df.Type == '1 RK Apartment']['Bathrooms'].mode()[0]
    df.loc[i, 'Bathrooms'] = 1
    df[df.Type == '1 BHK Apartment']['Bathrooms'].mode()[0]


st.write(df)
st.write(df.head(5))
df.info()


st.sidebar.header("Query Parameters")
st.sidebar.multiselect('Select the type of the House', df.Type.unique())
Locality = st.sidebar.multiselect("Select the Locality", df.Locality.unique())
Bathrooms = df.Bathrooms.replace("Missing", np.nan, inplace=True)
Bathrooms = st.sidebar.multiselect(
    'Select Number of Bathrooms', df.Bathrooms.unique())
Balcony = df.Balcony.replace("Missing", np.nan, inplace=True)
Balcony = st.sidebar.multiselect("Number of balcony", df.Balcony.unique())
Parking = st.sidebar.multiselect(
    " Select the number of parking spaces", df.Parking.unique())
Build_area = st.sidebar.number_input('Enter the build area in sq.ft')
Furnishing = st.sidebar.multiselect("Is it furnished", options=[
    'Unfurnished', 'Fully furnished'])
