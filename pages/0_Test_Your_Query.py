import streamlit as st
from functions.get_data import get_query_data

# test your query
# ---------------------------------------------------------------
st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
try:
    query_input = st.text_area("Enter your query")

    with st.expander("**Query entered**"):
        st.write(query_input)
    button_clicked = st.button('Execute', key=1001)

    if button_clicked:
        df_0 = get_query_data(query_input)
        st.markdown(f"YAY! Here's your data :tada::sunglasses:")
        st.write(df_0)
    st.markdown("---")
except Exception as e:
    st.markdown(f">:red[An error occurred. Error: {e} :shocked_face_with_exploding_head::fearful:]",
                unsafe_allow_html=True)
