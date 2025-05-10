import streamlit as st
import re
import pickle
from nltk.stem import WordNetLemmatizer
import pandas as pd

st.title("\U0001F973\U0001F917\U0001F632 Sentiment Analysis \U0001F631\U0001F621\U0001F614")

with open("emotion_vectors.pkl","rb") as f:
    vector=pickle.load(f) 

with open("emotion_models.pkl","rb") as f:
    model_load=pickle.load(f)
    model=model_load["LogisticRegression"]

text=st.text_input("Enter text to get response")

if st.button("Replay"):
    vec=vector.transform([text]) 
    result=model.predict(vec)
    if result==0:
      st.success(" \U0001F621 Don't Angry , Please Cool down \U0001F976")
    elif result==1: 
      st.success(" \U0001F631 Break the Fear in your Mind , will move Fearless \U0001F60E")   
    elif result==2:
      st.success("Enjoy it \U0001F973, this day your's")
    elif result==3:
      st.success("Love lives everywhere \U0001F917")
    elif result==4:
      st.success("\U0001F614Don't be Sad i'm with you  , always be Happy \U0001F60A") 
    else:
      st.success("Wow \U0001F632 that was so Amazing ") 


feedback=st.text_input("If you love my replies,feeback for me!")  

if st.button("save") :
    st.success("Thank you!\U0001F970") 
    f=open("feedback.csv","w") 
    f.write(feedback)
    f.close()  




     

