import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
# business query 6 logic
# ---------------------------------------------------------------
try:
    st.subheader("Business Query 6:")
    st.markdown(
        "Number of orders, total shipping costs and profits from catalog sales of particular counties and states for "
        "a given 60 day period for non-returned sales filled from an alternate warehouse")

    year = st.slider("Choose year:", min_value=1998, max_value=2002, value=1998, step=1, key=2001)
    month = st.selectbox("Choose a month:", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    state = st.selectbox("Select a State", ('IL', 'LA', 'TX', 'WI', 'MI', 'NY', 'CA', 'GA', 'KS', 'FL',
                                            'MT', 'CO', 'NE', 'NC', 'MN', 'PA', 'OH'))
    counties = st.multiselect("Choose 5 counties:",
                              options=['Luce County', 'Ziebach County', 'San Miguel County',
                                       'Dauphin County', 'Marshall County'],
                              default=['Luce County', 'Ziebach County', 'San Miguel County',
                                       'Dauphin County', 'Marshall County'],
                              max_selections=5)
    if len(counties) < 5:
        st.error('Please select 5 counties ')

    bs_query_6 = (read_query(f"queries/query_6.sql").replace("{year_param}", str(year))
                  .replace("{month_param}", str(month))
                  .replace("{state_param}", state)
                  .replace("{county_param_1}", counties[0])
                  .replace("{county_param_2}", counties[1])
                  .replace("{county_param_3}", counties[2])
                  .replace("{county_param_4}", counties[3])
                  .replace("{county_param_5}", counties[4]))

    with st.expander("**Show query**"):
        st.code(bs_query_6)

    button_clicked = st.button('Execute', key=1002)
    if button_clicked:
        df_6 = get_query_data(bs_query_6)
        st.write(df_6)
    st.markdown("---")
except IndexError as ie:
    st.markdown(f">:red[Please select required number of options to generate a query. Error: {ie} :fearful:]",
                unsafe_allow_html=True)
except BaseException as e:
    st.markdown(f">{e}")
