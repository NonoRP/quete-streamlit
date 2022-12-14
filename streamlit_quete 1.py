import streamlit as st

st.title('Hello Wilders, Welcome to my first application')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df_cars=pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
st.write(df_cars.head(3))
st.title('I. Analyse de corrélations')
fig_corr= plt.figure(figsize=(14, 8))
sns.heatmap(df_cars.corr(), cmap= "PuOr_r",center=0, annot=True)   
st.pyplot(fig_corr, clear_figure=True)
st.caption("Bonne corrélation entre :")
st.caption("cylinders et hp")
st.caption("cylinders et weightlbs")
st.caption("cylinders et cubicinches")
st.caption("cubicinches et hp")
st.caption("cubicinches et weightlbs")
st.title("1. Répartition du nombre de cylindres par pays ou continent")
fig_nbcyl=plt.figure(figsize=(12, 5)) 
df_cars.groupby(["continent"])["cylinders"].value_counts()
df_cars.groupby(["continent"])["cylinders"].value_counts().plot(kind="bar")
plt.xlabel("cylinders'by continent")
plt.ylabel("quantity")
st.pyplot(fig_nbcyl, clear_figure=True)
st.caption("On constate que les plus gros cylindrées se trouvent aux USA, suivis du Japon, et enfin de l'Europe.")
st.title("2. Répartition du nombre de cylindres par région et par année")
fig_nbcyl_année=plt.figure(figsize=(12, 15)) 
df_cars.groupby(["continent", "year"])["cylinders"].value_counts()
df_cars.groupby(["continent", "year"])["cylinders"].value_counts().sort_values(ascending=True).plot(kind="barh")
plt.xlabel("quantity")
plt.ylabel("cylinders' by area and year")
st.pyplot(fig_nbcyl_année, clear_figure=True)
st.title("3. Evolution de time-to-60 par année")
# Evolution de time_to_60 par année
fig_timto60=plt.figure(figsize=(12, 5)) 
plt.scatter(x =df_cars["year"] , y = df_cars["time-to-60"] , color = "b") 
plt.xlabel("Year") 
plt.ylabel("Time-to-60")
plt.title("Time-to-60's evolution by year") 
st.pyplot(fig_timto60, clear_figure=True)  
st.title("4. Evolution de mpg par année")
# Evolution de mpg par année
fig_mpg=plt.figure(figsize=(12, 5)) 
plt.scatter(x =df_cars["year"] , y = df_cars["mpg"] , color = "b") 
plt.xlabel("Year") 
plt.ylabel("mpg")
plt.title("mpg's evolution by year") 
st.pyplot(fig_mpg, clear_figure=True)  
st.title('II. Affichage du dataframe selon la région')
regions = df_cars["continent"].unique()
option_regions= st.multiselect("Choisis la région qui t'intéresse",
      	regions, default = regions)
# # Selection de ou des regions choisies, en filtrant avec un masque :
mask_region = df_cars["continent"].isin(option_regions)
df_cars=df_cars[mask_region]
st.write(df_cars)

