import datetime
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# page headings
st.set_page_config(layout="centered", page_title="INFO7374: Algorithmic Marketing")
st.header("Assignment 1")
st.subheader("Group 1: Adit Bhosale, Sowmya Chatti, Vasundhara Sharma")


# connect to Snowflake
# ---------------------------------------------------------------
def get_query_data(query) -> pd.DataFrame:
    try:
        engine = create_engine(
            'snowflake://{user}:{password}@{account_identifier}/{database_name}/{schema_name}'.format(
                user=st.secrets.user,
                password=st.secrets.password,
                account_identifier=st.secrets.account_identifier,
                database_name='snowflake_sample_data',
                schema_name='tpcds_sf10tcl',
                connect_args={'connect_timeout': 1000, 'read_timeout': 1000}
            )
        )
        connection = engine.connect()
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        raise e
    finally:
        connection.close()
        engine.dispose()


# button functions
# ---------------------------------------------------------------
if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


# read query file
def read_query(query_file_path) -> str:
    file = open(query_file_path, "r")
    query = file.read()
    return query


# test your query
# ---------------------------------------------------------------
with st.expander("**Test your query!**"):
    # st.subheader("Test your query!")
    query_input = st.text_area("Enter your query")
    st.button('Execute', on_click=click_button, key=1001)
    if st.session_state.clicked:
        df_0 = get_query_data(query_input)
        st.write(df_0)
st.markdown("---")

# business query 1 logic
# ---------------------------------------------------------------
st.subheader("Business Query 1:")
st.markdown("Find customers whose increase in spending was large over the web than in stores this year compared to "
            "last year.")
year = st.selectbox("Choose year:", (1998, 1999, 2000, 2001, 2002), placeholder="Year", key=2001)
bs_query_1 = read_query(f"queries/query_1.sql").replace("{year_param}", str(year))
with st.expander("**Show query**"):
    st.write(bs_query_1)
st.button('Execute', on_click=click_button, key=1002)

if st.session_state.clicked:
    df_1 = get_query_data(bs_query_1)
    st.write(df_1)
st.markdown("---")


# business query 2 logic
# ---------------------------------------------------------------
st.subheader("Business Query 2:")
st.markdown("Compute the revenue ratios across item classes:  For each item in a list of given categories, "
            "during a 30 day time period, sold through the web channel compute the ratio of sales of that item to the "
            "sum of all of the sales in that item's class.")
category_param = st.multiselect("Choose 3 categories:", options=['Sports', 'Men', 'Music', 'Children', 'Electronics',
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
    st.write(bs_query_2)
st.button('Execute', on_click=click_button, key=1003)
if st.session_state.clicked:
    df_2 = get_query_data(bs_query_2)
    st.write(df_2)
st.markdown("---")

# business query 3 logic
# ---------------------------------------------------------------
st.subheader("Business Query 3:")
st.markdown("Calculate the average sales quantity, average sales price, average wholesale cost, total wholesale cost "
            "for store sales of different customer types (e.g., based on marital status, education status) including "
            "their household demographics, sales price and different combinations of state and sales profit for a "
            "given year.")
try:
    state_param = st.multiselect("Choose 9 states:",
                                 options=['AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL',
                                          'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
                                          'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV',
                                          'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR',
                                          'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA',
                                          'VI', 'WA', 'WV', 'WI', 'WY'],
                                 default=['TX', 'OH', 'CA', 'OR', 'NM', 'KY', 'VA', 'AZ', 'MS'],
                                 max_selections=9)
    education_param = st.multiselect("Choose 3 education levels:", options=['Primary', 'Secondary', 'College',
                                                                            '2 yr Degree', '4 yr Degree',
                                                                            'Advanced Degree', 'Unknown'],
                                     default=['2 yr Degree', 'College', 'Advanced Degree'],
                                     max_selections=3)
    marital_param = st.multiselect("Choose 3 education levels:", options=['M', 'S', 'D', 'W', 'U'],
                                   default=['M', 'S', 'W'],
                                   max_selections=3)

    bs_query_3 = read_query(f"queries/query_2.sql")

    # replacing state_param
    bs_query_3 = (bs_query_3.replace("{state_param_1}", state_param[0])
                  .replace("{state_param_2}", state_param[1])
                  .replace("{state_param_3}", state_param[2])
                  .replace("{state_param_4}", state_param[3])
                  .replace("{state_param_5}", state_param[4])
                  .replace("{state_param_6}", state_param[5])
                  .replace("{state_param_7}", state_param[6])
                  .replace("{state_param_8}", state_param[7])
                  .replace("{state_param_9}", state_param[8]))

    # replacing education_param
    bs_query_3 = (bs_query_3.replace("{education_param_1}", education_param[0])
                  .replace("{education_param_2}", education_param[1])
                  .replace("{education_param_3}", education_param[2]))

    # replacing marital_status_param
    bs_query_3 = (bs_query_3.replace("{marital_status_param_1}", marital_param[0])
                  .replace("{marital_status_param_2}", marital_param[1])
                  .replace("{marital_status_param_3}", marital_param[2]))
    print(education_param)
    print(marital_param)
    print(state_param)
    print(bs_query_3)
except IndexError as ie:
    st.markdown(f":red[> Please select required number of options to generate a query. Error: {ie} :fearful:]",
                unsafe_allow_html=True)
except BaseException as e:
    st.markdown(f">{e}")
print(bs_query_3)
with st.expander("**Show query**"):
    st.write(bs_query_3)
st.button('Execute', on_click=click_button, key=1004)
if st.session_state.clicked:
    df_3 = get_query_data(bs_query_3)
    st.write(df_3)
st.markdown("---")
