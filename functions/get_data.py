import logging

from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import logging
import datetime

logging.basicConfig(filename="logs.log", encoding="utf-8", level=logging.DEBUG)


# connect to Snowflake
# ---------------------------------------------------------------
def get_query_data(query) -> pd.DataFrame:
    try:
        logging.info(f"{datetime.datetime.now()}: Creating engine...")
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
        logging.info(f"{datetime.datetime.now()}: Connecting engine...")
        connection = engine.connect()
        logging.info(f"{datetime.datetime.now()}: Executing query...")
        df = pd.read_sql_query(query, engine)
        logging.info(f"{datetime.datetime.now()}: Dataframe retrieved..")
        return df
    except Exception as e:
        raise e
    finally:
        connection.close()
        engine.dispose()