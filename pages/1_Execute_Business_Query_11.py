import datetime
import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query


# business query 1 logic
# ---------------------------------------------------------------
st.subheader("Business Query 1:")
st.markdown("Find customers whose increase in spending was large over the web than in stores this year compared to "
            "last year.")
year = st.slider("Choose year:", min_value=1998, max_value=2002, value=1998, step=1, key=2001)
bs_query_1 = read_query(f"queries/query_1.sql").replace("{year_param}", str(year))

with st.expander("**Show query**"):
    st.code(bs_query_1)

button_clicked = st.button('Execute', key=1002)
if button_clicked:
    df_1 = get_query_data(bs_query_1)
    st.write(df_1)
st.markdown("---")




