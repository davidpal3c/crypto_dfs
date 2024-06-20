import streamlit as st
from shape_data import main_df



st.header("Crypto_dfs")
user_name = st.text_input("Enter your Name: ")


is_clicked = st.button('Browse current Crypto Info.')

if is_clicked:
    st.write(f"Welcome {user_name}! ")
    
else: 
    st.write('')



st.dataframe(main_df())


# st.json(data, expanded=True)

