import datetime
import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
# business query 2 logic
# ---------------------------------------------------------------
try:
    st.subheader("Business Query 2:")
    st.markdown("Compute the revenue ratios across item classes:  For each item in a list of given categories, "
                "during a 30 day time period, sold through the web channel compute the ratio of sales of that item to "
                "the sum of all of the sales in that item's class.")
    category_param = st.multiselect("Choose 3 categories:",
                                    options=['Sports', 'Men', 'Music', 'Children', 'Electronics',
                                             'Home', 'Women', 'Shoes', 'Jewelry', 'Books'],
                                    default=['Sports', 'Home', 'Books'],
                                    max_selections=3)
    date_param = st.date_input("Select Date:", value=datetime.date(1999, 1, 1),
                               min_value=datetime.date(1999, 1, 1),
                               max_value=datetime.date(2002, 12, 31))

    bs_query_2 = (read_query(f"queries/query_2.sql").replace("{category_param_1}", category_param[0])
                  .replace("{category_param_2}", category_param[1])
                  .replace("{category_param_3}", category_param[2]))
    bs_query_2 = bs_query_2.replace("{date_param}", date_param.strftime("%Y-%m-%d"))
    with st.expander("**Show query**"):
        st.code(bs_query_2)
    button_clicked = st.button('Execute', key=1003)
    if button_clicked:
        df_2 = get_query_data(bs_query_2)
        st.markdown(f">YAY! Here's your data :tada::sunglasses:", unsafe_allow_html=True)
        st.table(df_2)
    st.markdown("---")

except Exception as e:
    st.markdown(f">:red[An error occurred. Error: {e} :shocked_face_with_exploding_head::fearful:]",
                unsafe_allow_html=True)
