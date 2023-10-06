import datetime
import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query


# test your query
# ---------------------------------------------------------------

query_input = st.text_area("Enter your query")

with st.expander("**Query entered**"):
    st.write(query_input)
button_clicked = st.button('Execute', key=1001)

if button_clicked:
    df_0 = get_query_data(query_input)
    st.write(df_0)
st.markdown("---")

