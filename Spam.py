import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Streamlit app
st.image(r"innomaticslogo.webp")
st.title('Email SPAM or HAM Classifier')

# Load the trained model
model = pickle.load(open(r"model.pkl", "rb"))
model1= pickle.load(open(r"model1.pkl", "rb"))

# Input text box
email=st.text_input("Please Enter Your Email text to classify")
checking=model1.transform([email])
prediction = model.predict(checking)[0]


# Predict button
if st.button('Predict'):
    if prediction=="spam":
        st.write("This Email is SPAM,Stay SAFE")
        st.image(r"spam.png")
    else:
        st.write("This Email is NOT SPAM,it's SAFE")
        st.image(r"ham.jpeg")

        st.write("This Email is NOT SPAM,it's SAFE")
        st.image(r"C:\Users\SK\Downloads\ham.jpeg")


