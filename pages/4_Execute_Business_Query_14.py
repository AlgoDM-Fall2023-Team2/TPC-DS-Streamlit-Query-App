import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
# business query 1 logic
# ---------------------------------------------------------------
try:
    st.header("Business Query 4:")
    year = st.selectbox("Choose year:", options=range(1998, 2001))
    month = st.text_input("Choose month:", value="11", disabled=True)
    day = st.selectbox("Choose day:", options=range(1, 30))
    st.subheader("Iteration 1")
    st.markdown("First identify items in the same brand, class and category that are sold in all three sales channels "
                "in two consecutive years. Then compute the average sales (quantity*list price) across all sales of "
                "all three sales channels in the same three years (average sales). Finally, compute the total sales "
                "and the total number of sales rolled up for each channel, brand, class and category. Only consider "
                "sales of cross channel sales that had sales larger than the average sale.")
    bs_query_4_1 = (read_query(f"queries/query_4_01.sql")
                    .replace("{year_param}", str(year))
                    .replace("{month_param}", month)
                    .replace("{day_param}", str(day)))
    with st.expander("**Show query**"):
        st.code(bs_query_4_1)

    button_clicked = st.button('Execute', key=1002)
    if button_clicked:
        df_1 = get_query_data(bs_query_4_1)
        st.markdown(f">YAY! Here's your data :tada::sunglasses:", unsafe_allow_html=True)
        st.table(df_1)
    st.markdown("---")

    st.subheader("Iteration 2")
    st.markdown("Based on the previous query compare December store sales.")
    bs_query_4_2 = (read_query(f"queries/query_4_02.sql")
                    .replace("{year_param}", str(year))
                    .replace("{month_param}", month)
                    .replace("{day_param}", str(month)))
    with st.expander("**Show query**"):
        st.code(bs_query_4_2)

    button_clicked = st.button('Execute', key=1003)
    if button_clicked:
        df_1 = get_query_data(bs_query_4_1)
        st.markdown(f">YAY! Here's your data :tada::sunglasses:", unsafe_allow_html=True)
        st.write(df_1)
    st.markdown("---")

except Exception as e:
    st.markdown(f">:red[An error occurred. Error: {e} :shocked_face_with_exploding_head::fearful:]",
                unsafe_allow_html=True)
