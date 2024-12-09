import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score
from collections import Counter
import joblib
from sklearn.model_selection import train_test_split

def split_vals(df: pd.DataFrame, n: int) -> pd.DataFrame: 
    return df[:n].copy(), df[n:].copy()

st.markdown("<h1 style='color: #E0218A;'>Buy sell or wait that is the question</h1>", unsafe_allow_html=True)
st.header("😎 Quote from a great philosopher😎 ")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    
    data = pd.read_csv(uploaded_file)
    
    st.write("Data Preview:")
    st.write(data.head())
    
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    calibrated_classifier = joblib.load('c:/Users/Melissa/Bureau/Bsc 2/ML/BITCOIN/ML-project/models/calibrated_classifier.pkl')

    y_pred = calibrated_classifier.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    
    
    
    counter = Counter(y_pred)
    
    if counter[0] > counter[1] and counter[0] > counter[2]:
        action = "Sell"
    elif counter[1] > counter[0] and counter[1] > counter[2]:
        action = "Hold"
    else:
        action = "Buy"
    
    st.markdown(f"<h2 style='text-align: center; color: #E0218A;'>Recommended Action: {action}</h2>", unsafe_allow_html=True)
