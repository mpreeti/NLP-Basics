import streamlit as st

st.title('Box selection example')

selectedbox=st.selectbox(
        "Select yes or no",
        ["Yes",'No']
)
st.write(f'You selected {selectedbox}')