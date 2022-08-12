import streamlit as st
from multiapp import MultiApp
from dashboard import data_dash

st.set_page_config(page_title="Global China-Taiwan Data Analysis")

app = MultiApp()


st.title("Tweet Sentiment Analysis")

st.markdown("""
            # Economic Data Analysis
            Twitter Data Analysis of Economic Data
            """)

app.add_app("Home", home.app)
app.add_app("Data", data_dash.selectHashTag)
app.add_app("Visualization", data_dash.wordCloud)

#  main app
app.run()