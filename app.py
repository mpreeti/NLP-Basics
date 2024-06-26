
import streamlit as st
import pandas as pd

st.title('Hello, Streamlit!')
st.write('First DataFrame')

st.write(pd.DataFrame({
    'A':[1,2,3,4,5],
    'B':[6,7,8,9,0]
}))