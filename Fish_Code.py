# FishDataset
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\pmgan\DATA200\hw4\Fish_Dataset.csv')
Species_Of_Fish = df['Species']
Weight_Of_Fish = df['Weight']

fig,ax=plt.subplots()
ax.bar(Species_Of_Fish,Weight_Of_Fish)

plt.bar(Species_Of_Fish,Weight_Of_Fish)
plt.xlabel('Species_Of_Fish')
plt.ylabel('Weight_Of_Fish')
plt.title('Weight_vs_Species')
plt.xticks(rotation=45,horizontalalignment='right' )

st.pyplot(fig)

print ('Pike species fishes weights more')
