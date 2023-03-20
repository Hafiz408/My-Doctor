import streamlit as st
import pickle
import pandas as pd



def load_model():
    with open('disease_predictor.pkl', 'rb') as file:
         data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
symptoms = data["symptoms"]
symptoms.insert(0,'nan')
df = data["df"]
severity = data["severity"]
precaution = data["precaution"]
description = data["description"]

def show_predict_page():

    cols=st.columns([2,4,2])
    cols[1].image("doc.png", width=250)
    st.title("|.......  My Doctor  ......|")
    st.write("")
    cols = st.columns([1,8,1])
    cols[1].write("""#### Enter your symptoms and click diagnose""")
    st.write("")

    symptom_list = []

    symptom1 = st.selectbox("Symptoms 1 :",symptoms)
    symptom_list.append(symptom1)

    symptom2 = st.selectbox("Symptoms 2 :",symptoms)
    symptom_list.append(symptom2)

    symptom3 = st.selectbox("Symptoms 3 :",symptoms)
    symptom_list.append(symptom3)

    symptom4 = st.selectbox("Symptoms 4 :",symptoms)
    symptom_list.append(symptom4)
        
    symptom5 = st.selectbox("Symptoms 5 :",symptoms)
    symptom_list.append(symptom5)       

    st.write("")
    cols = st.columns([2,1,2])
    ok = cols[1].button("Diagnose")

    if ok:
        
        if 'nan' in symptom_list:
            symptom_list=set(symptom_list)
            symptom_list=list(symptom_list)
            symptom_list.remove('nan')
        
        if len(symptom_list) < 2:
            st.warning("""### Enter atleast 2 different symptoms !!""")
        else:
            df.loc[0] = 0
            for i in symptom_list:
                df[i]=1

            to_pred = df.iloc[0]
            output = model.predict([to_pred])[0]

            st.write("")
            st.write("""### You are diagonised with """+ output +""".""")
            
            st.write("")
            with st.expander("# Description"):
                pd.options.display.max_colwidth = 1000
                d = description[description['Disease']==output]['Description'].to_string()[2:]
                st.write(d)

            st.write("")
            with st.expander("# Precaution"):
                pd.options.display.max_colwidth = 1000
                precaution.fillna(0,inplace=True)
                p = precaution[precaution['Disease']==output]
                for col in p:
                    if col != 'Disease':
                        o=p[col].to_string()[2:]
                        if "0" not in o:
                            st.write("-"+o)
            
        


