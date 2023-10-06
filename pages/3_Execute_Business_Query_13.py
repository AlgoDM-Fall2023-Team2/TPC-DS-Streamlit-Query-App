import streamlit as st
from functions.get_data import get_query_data
from functions.get_query import read_query

# business query 3 logic
# ---------------------------------------------------------------
try:
    st.subheader("Business Query 3:")
    st.markdown(
        "Calculate the average sales quantity, average sales price, average wholesale cost, total wholesale cost "
        "for store sales of different customer types (e.g., based on marital status, education status) including "
        "their household demographics, sales price and different combinations of state and sales profit for a "
        "given year.")

    bs_query_3 = read_query(f"queries/query_2.sql")
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

    with st.expander("**Show query**"):
        st.code(bs_query_3)

    button_clicked = st.button('Execute', key=1004)
    if button_clicked:
        df_3 = get_query_data(bs_query_3)
        st.markdown(f"YAY! Here's your data :tada::sunglasses:")
        st.write(df_3)
    st.markdown("---")
except IndexError as ie:
    st.markdown(f">:red[Please select required number of options to generate a query. Error: {ie}"
                ":shocked_face_with_exploding_head::fearful:]",
                unsafe_allow_html=True)
except Exception as e:
    st.markdown(f">:red[An error occurred. Error: {e} :shocked_face_with_exploding_head::fearful:]",
                unsafe_allow_html=True)
