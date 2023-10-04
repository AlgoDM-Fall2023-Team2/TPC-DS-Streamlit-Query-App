import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
st.header("Assignment 1")
st.subheader("Group 1: Adit Bhosale, Sowmya Chatti, Vasundhara Sharma")


# Connect to Snowflake
# ------------------------------------------------------------
def get_query_data(query) -> pd.DataFrame:
    engine = create_engine(
        'snowflake://{user}:{password}@{account_identifier}/'.format(
            user=st.secrets.user,
            password=st.secrets.password,
            account_identifier=st.secrets.account_identifier,
            connect_args={'connect_timeout': 500, 'read_timeout': 500}
        )
    )
    connection = engine.connect()
    df = pd.read_sql_query(query, engine)
    connection.close()
    engine.dispose()
    return df

# Button functions
# ------------------------------------------------------------
if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


# Test your query
# ------------------------------------------------------------
st.subheader("Test your query!")
query = st.text_area("Enter your query")

st.button('Execute', on_click=click_button, key=1001)
if st.session_state.clicked:
    df = get_query_data(query)
    st.write(df)

# business query 1 logic
# ---------------------------------------------------------------
st.subheader("Business Query 1:")
st.markdown("Find customers whose increase in spending was large over the web than in stores this year compared to last year.")
year = st.selectbox("Choose year", (1998, 1999, 2000, 2001, 2002), placeholder="Year")
bs_query_1 = f"""with year_total as ( select c_customer_id customer_id, c_first_name customer_first_name, c_last_name customer_last_name, c_preferred_cust_flag customer_preferred_cust_flag, c_birth_country customer_birth_country, c_login customer_login, c_email_address customer_email_address, d_year dyear, sum( ss_ext_list_price - ss_ext_discount_amt ) year_total, 's' sale_type from customer, store_sales, date_dim where c_customer_sk = ss_customer_sk and ss_sold_date_sk = d_date_sk group by c_customer_id, c_first_name, c_last_name, c_preferred_cust_flag, c_birth_country, c_login, c_email_address, d_year union all select c_customer_id customer_id, c_first_name customer_first_name, c_last_name customer_last_name, c_preferred_cust_flag customer_preferred_cust_flag, c_birth_country customer_birth_country, c_login customer_login, c_email_address customer_email_address, d_year dyear, sum( ws_ext_list_price - ws_ext_discount_amt ) year_total, 'w' sale_type from customer, web_sales, date_dim where c_customer_sk = ws_bill_customer_sk and ws_sold_date_sk = d_date_sk group by c_customer_id, c_first_name, c_last_name, c_preferred_cust_flag, c_birth_country, c_login, c_email_address, d_year ) select t_s_secyear.customer_id, t_s_secyear.customer_first_name, t_s_secyear.customer_last_name, t_s_secyear.customer_login from year_total t_s_firstyear, year_total t_s_secyear, year_total t_w_firstyear, year_total t_w_secyear where t_s_secyear.customer_id = t_s_firstyear.customer_id and t_s_firstyear.customer_id = t_w_secyear.customer_id and t_s_firstyear.customer_id = t_w_firstyear.customer_id and t_s_firstyear.sale_type = 's' and t_w_firstyear.sale_type = 'w' and t_s_secyear.sale_type = 's' and t_w_secyear.sale_type = 'w' and t_s_firstyear.dyear = {year} and t_s_secyear.dyear = {year} + 1 and t_w_firstyear.dyear = {year} and t_w_secyear.dyear = {year} + 1 and t_s_firstyear.year_total > 0 and t_w_firstyear.year_total > 0 and case when t_w_firstyear.year_total > 0 then t_w_secyear.year_total / t_w_firstyear.year_total else 0.0 end > case when t_s_firstyear.year_total > 0 then t_s_secyear.year_total / t_s_firstyear.year_total else 0.0 end order by t_s_secyear.customer_id, t_s_secyear.customer_first_name, t_s_secyear.customer_last_name, t_s_secyear.customer_login limit 10;"""

st.write(bs_query_1)
st.button('Execute', on_click=click_button, key=1002)

if st.session_state.clicked:
    df = get_query_data(bs_query_1)
    st.write(df)



