import streamlit as st
from predict_page import show_predict_page
from explore_page import graphs,visual2
from doc_page import doc


col1,col2 = st.sidebar.columns([4,3])
col1.image("doc 2.jpeg",width=120)
col2.write("")
col2.write("")
col2.write("")
col2.write("""# My Doctor""")   
# st.sidebar.image("pic\doc 2.jpeg",width=100)
# st.sidebar.write("""# My Doctor""")   
st.sidebar.write("")
st.sidebar.write("")

choice = st.sidebar.selectbox("Menu",['Diagnose','Explore','Brief'])

if choice == 'Diagnose':
    show_predict_page()
elif choice == 'Explore':
    graphs()
else:
    doc()

