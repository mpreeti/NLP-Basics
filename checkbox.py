import streamlit as st

st.title('Checkbox example')

checkbox_one=st.checkbox("yes")
checkbox_two=st.checkbox("No")

if checkbox_one:
    value='yes'
elif checkbox_two:
    value='No'
else:
    value='No Value Selected'

st.write(f'You selected: {value}')