from PIL import Image
import sys
import os
import streamlit as st

# sys.path.append(os.path.abspath(os.path.join('../')))


def app():
    st.title('Home')

    st.write("Topics on the Impact of Pelosi's visit to Taiwan")

    st.write(
        'Go to the data navigation to learn more about the data and the visualization page to get insight of the Data.')

    image = Image.open('./wordcloud.png')
    st.image(image, caption="Word cloud analysis", use_column_width=True)