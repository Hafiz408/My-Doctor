import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle


def load_model():
    with open('disease_predictor.pkl', 'rb') as file:
         data = pickle.load(file)
    return data

data = load_model()

ss = data["severity"]
sp = data["precaution"]
df = data["dataframe"]


def graphs():

    st.title("Explore")

    d = ss.groupby('weight').count()
    d.insert(0,'Weight',range(1,1+len(d)))
    x2=d['Symptom']
    y2=d['Weight']
    v = plt.figure(figsize=(10,8))
    plt.pie(x2,labels=y2,autopct="%1.1f%%")
    plt.legend(title="Severity:")

    st.write("""
    #
    ### Pie Chart
    On the basis of severity of symptoms.
     """)
    st.pyplot(v)
    st.write("""
    Inference:

    From the above pie chart we can infer that

    - More that 50% of the symptoms lie in the severity rate of 4 and 5(according to the given data).
    - Symptoms with most severity and least severity occupy only 5%.
    - And the rest covers more than 40% in total.
    """)
    visual2()


def visual2():
    ss.drop(117,inplace=True)
    df['severity']=0
    for i in range(0,len(df)):
        w=0
        l=df.iloc[i]['Symptoms']
        for x in l:
            x=x.replace(" ", "")
            w+=int(ss[ss['Symptom']==x]['weight'])
        s=float(w)/int(len(l))
        df['severity'][i]=round(s,2)

    dict={}
    for x in df['Disease'].unique():
        dict[x]=df[df['Disease']==x]['severity'].mean()
    vc=pd.DataFrame(dict,index=['severity'])
    vc=vc.T


    st.write("""
        #
        ### Disease severity dataframe
        #
        """)
    st.dataframe(vc)

    st.write("""
        #
        ### Bar graph
        On basis of severity of diseases.

        """)
    st.bar_chart(vc)
    st.write("""
    Inference:

    From the above bar graph we can infer that

    - AIDS, piles and urinary tract infection has the highest severity rate of 5.
    - Acne and psoriasis has the lowest severity rate of 2.
    """)



    
