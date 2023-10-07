import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
# business query 18 logic
# ---------------------------------------------------------------
st.subheader("Business Query 18:")
st.markdown(
    "Compute, for each county, the average quantity, list price, coupon amount, sales price, net profit, age, "
    "and number of dependents for all items purchased through catalog sales in a given year by customers who were "
    "born in a given list of six months and living in a given list of seven states and who also belong to a given "
    "gender and education demographic."
)

try:

    year_param = st.slider("Choose year:", min_value=1998, max_value=2002, value=1998, step=1, key=2001)

    gender_param = st.selectbox(
        "Select Gender",
        options=["M", "F"],
    )

    education_param = st.selectbox(
        "Choose 3 education levels:",
        options=['Primary', 'Secondary', 'College', '2 yr Degree', '4 yr Degree', 'Advanced Degree', 'Unknown'],
    )

    state_param = st.multiselect(
        "Choose 7 states:",
        options=['AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL',
                 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
                 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV',
                 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR',
                 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA',
                 'VI', 'WA', 'WV', 'WI', 'WY'],
        default=['TX', 'OH', 'CA', 'OR', 'NM', 'KY', 'VA'],
        max_selections=7
    )

    month_param = st.multiselect(
        "Choose 6 months:",
        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        default=['1', '2', '3', '4', '5', '6'],
        max_selections=6
    )

    bs_query_8 = read_query(f"queries/query_8.sql").replace("{year_param}", str(year_param))

    bs_query_8 = (bs_query_8.replace("{gender_param}", str(gender_param)))

    bs_query_8 = (bs_query_8.replace("{education_param}", str(education_param)))

    bs_query_8 = (bs_query_8.replace("{state_param_1}", state_param[0])
                  .replace("{state_param_2}", state_param[1])
                  .replace("{state_param_3}", state_param[2])
                  .replace("{state_param_4}", state_param[3])
                  .replace("{state_param_5}", state_param[4])
                  .replace("{state_param_6}", state_param[5])
                  .replace("{state_param_7}", state_param[6]))

    bs_query_8 = (bs_query_8.replace("{month_param_1}", month_param[0])
                  .replace("{month_param_2}", month_param[1])
                  .replace("{month_param_3}", month_param[2])
                  .replace("{month_param_4}", month_param[3])
                  .replace("{month_param_5}", month_param[4])
                  .replace("{month_param_6}", month_param[5]))

    with st.expander("**Show query**"):
        st.code(bs_query_8)

    button_clicked = st.button('Execute', key=1002)
    if button_clicked:
        df_1 = get_query_data(bs_query_8)
        st.table(df_1)
    st.markdown("---")
except IndexError as ie:
    st.markdown(f":red[> Please select required number of options to generate a query. Error: {ie} :fearful:]",
                unsafe_allow_html=True)
except BaseException as e:
    st.markdown(f">{e}")
