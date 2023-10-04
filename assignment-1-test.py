import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
st.header("Assignment 1")
st.subheader("Group 1: Adit Bhosale, Sowmya Chatti, Vasundhara Sharma")

query = st.text_area("Enter your query")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


st.button('Execute', on_click=click_button)

if st.session_state.clicked:
    engine = create_engine(
        'snowflake://{user}:{password}@{account_identifier}/'.format(
            user=st.secrets.user,
            password=st.secrets.password,
            account_identifier=st.secrets.account_identifier
        )
    )
    connection = engine.connect()
    # result = connection.execute(query)
    df = pd.read_sql_query(query, engine)
    st.write(df)

    connection.close()
    engine.dispose()
