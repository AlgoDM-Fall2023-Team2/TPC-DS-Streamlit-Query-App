import datetime
import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

# business query 20 logic
# ---------------------------------------------------------------
st.subheader("Business Query 20:")
st.markdown(
    "Compute the total revenue and the ratio of total revenue to revenue by item class for specified item categories and time periods."
)

try:

    date_param = st.date_input(
        "Select Date:", value=datetime.date(1999, 1, 1),
        min_value=datetime.date(1999, 1, 1),
        max_value=datetime.date(2002, 12, 31)
    )

    category_param = st.multiselect(
        "Choose 3 category:",
        options=['Men', 'Music', 'Children', 'Electronics', 'Home', 'Women', 'Shoes', 'Jewlery', 'Books', 'Sports'],
        default=['Men', 'Music', 'Children'],
        max_selections=3
    )

    bs_query_10 = read_query(f"queries/query_10.sql").replace("{date_param}", date_param.strftime("%Y-%m-%d"))

    bs_query_10 = (bs_query_10.replace("{category_param_1}", category_param[0])
                  .replace("{category_param_2}", category_param[1])
                  .replace("{category_param_3}", category_param[2])
                  )

except IndexError as ie:
    st.markdown(f":red[> Please select required number of options to generate a query. Error: {ie} :fearful:]",
                unsafe_allow_html=True)
except BaseException as e:
    st.markdown(f">{e}")

with st.expander("**Show query**"):
    st.code(bs_query_10)

button_clicked = st.button('Execute', key=1002)
if button_clicked:
    df_1 = get_query_data(bs_query_10)
    st.write(df_1)
st.markdown("---")