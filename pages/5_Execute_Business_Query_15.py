import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

# business query 5 logic
st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
# ---------------------------------------------------------------
try:
    st.subheader("Business Query 5:")
    st.markdown("Total catalog sales for customers in selected geographical regions or who made large purchases for a "
                "given year and quarter")

    year = st.slider("Choose year:", min_value=1998, max_value=2002, value=1998, step=1, key=2001)
    quarter = st.selectbox('Select the quarter', (1, 2, 3, 4))
    bs_query_5 = (read_query(f"queries/query_5.sql").replace("{year_param}", str(year))
                  .replace("{quarter_param}", str(quarter)))

    with st.expander("**Show query**"):
        st.code(bs_query_5)

    button_clicked = st.button('Execute', key=1002)
    if button_clicked:
        df_5 = get_query_data(bs_query_5)
        st.table(df_5)
    st.markdown("---")
except Exception as e:
    st.markdown(f">:red[An error occurred. Error: {e} :shocked_face_with_exploding_head::fearful:]",
                unsafe_allow_html=True)

