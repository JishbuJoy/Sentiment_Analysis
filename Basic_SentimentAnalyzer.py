#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


# In[11]:


st.title("Real Time Sentiment Analysis")
user_input = st.text_input("Please Rate our Sevices:")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
if score==0:
    st.write(" ")
elif score['neg'] != 0:
    st.write("Negative")
elif score['pos'] != 0:
    st.write("Positive")


# In[9]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




