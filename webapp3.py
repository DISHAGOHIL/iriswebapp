import streamlit as st
import pickle


st.title("Iris Recognized")

#slider
a=st.slider("sepal.length", 4.3,7.9)

b=st.slider("sepal.width", 2.0,4.4)

c=st.slider("petal.length", 1.0,6.9)

d=st.slider("petal.width", 0.1,2.5)

#Selectbox
ml=st.selectbox("select: ",['SVM', 'KNN','DT','RF','ET'])

pd=st.button("Predict")
if pd:
    if ml=="SVM":
        model=pickle.load(open("irissvm.pkl",'rb'))
        clss=model.predict([[float(a),float(b),float(c),float(d)]])
        st.success(clss[0])
    elif ml=="KNN":
        model=pickle.load(open("irissvm.pkl",'rb'))
        clss=model.predict([[float(a),float(b),float(c),float(d)]])
        st.success(clss[0])
    elif ml=="DT":
        model=pickle.load(open("irissvm.pkl",'rb'))
        clss=model.predict([[float(a),float(b),float(c),float(d)]])
        st.success(clss[0])
    elif ml=="RF":
        model=pickle.load(open("irissvm.pkl",'rb'))
        clss=model.predict([[float(a),float(b),float(c),float(d)]])
        st.success(clss[0])
    elif ml=="ET":
        model=pickle.load(open("irissvm.pkl",'rb'))
        clss=model.predict([[float(a),float(b),float(c),float(d)]])
        st.success(clss[0])
    




