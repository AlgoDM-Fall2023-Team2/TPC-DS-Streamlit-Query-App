import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
# business query 19 logic
# ---------------------------------------------------------------
st.subheader("Business Query 19:")
st.markdown(
    "Select the top revenue generating products bought by out of zip code customers for a given year, month and "
    "manager."
)

try:
    year_param = st.slider("Choose year:", min_value=1998, max_value=2002, value=1998, step=1, key=2001)

    month_param = st.selectbox(
        "Choose 1 month:",
        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    )

    manager_param = st.slider("Choose year:", min_value=1, max_value=100, value=50, step=1)

    bs_query_9 = read_query(f"queries/query_9.sql").replace("{year_param}", str(year_param))

    bs_query_9 = (bs_query_9.replace("{month_param}", str(month_param)))

    bs_query_9 = (bs_query_9.replace("{manager_param}", str(manager_param)))

    with st.expander("**Show query**"):
        st.code(bs_query_9)

    button_clicked = st.button('Execute', key=1002)
    if button_clicked:
        df_1 = get_query_data(bs_query_9)
        st.table(df_1)
    st.markdown("---")
except IndexError as ie:
    st.markdown(f">:red[Please select required number of options to generate a query. Error: {ie} :fearful:]",
                unsafe_allow_html=True)
except BaseException as e:
    st.markdown(f">{e}")
