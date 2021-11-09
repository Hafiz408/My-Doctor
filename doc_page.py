import streamlit as st
import webbrowser

url = 'https://github.com/Hafiz408/My-Doctor'

def doc():
    st.balloons()
    st.title("Hello guys !!")
    st.write("")
    st.write("""
    #
    ##### " My Doctor " is a web app created using streamlit library in python. It diagnises the disease based on the symptoms and provides us with it's description and precautions. It uses Random Forest classifier to build the model and predicts the output.
    #
    ##### It also offers another feature i.e. the Explore page where we can see various visuals about the diseases , symptoms and severity of them.
    #
    """)

    cols=st.columns([3,2])
    cols[0].write("For the Github link of this project, click")
    github = cols[1].button("Here.")
    if github:
        webbrowser.open_new_tab(url)
