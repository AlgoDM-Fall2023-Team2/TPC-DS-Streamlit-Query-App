import streamlit as st

from functions.get_data import get_query_data
from functions.get_query import read_query

# business query 7 logic
# ---------------------------------------------------------------
st.subheader("Business Query 7:")
st.markdown("For each state, all items that were sold in stores in a particular quarter and returned in " 
            "the next three quarters and then re-purchased by the customer through the catalog channel"
            " in the three following quarters.")
year = st.slider("Choose year:", min_value=1998, max_value=2002, value=1998, step=1, key=2001)


bs_query_7 = read_query(f"queries/query_7.sql").replace("{year_param}", str(year))

with st.expander("**Show query**"):
    st.code(bs_query_7)

button_clicked = st.button('Execute', key=1002)
if button_clicked:
    df_7 = get_query_data(bs_query_7)
    st.table(df_7)
st.markdown("---")




