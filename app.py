import streamlit as st
import pickle
movies_list=pickle.load(open('movies.pkl'))
st.title('Movie-recommendation system')