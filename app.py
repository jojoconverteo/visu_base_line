import streamlit as st
import pandas as pd
import plotly.express as px
import config as conf

st.title("Baseline : Analyse Streamlit")

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])


if data is not None:
    df = pd.read_csv(data, sep=conf.sep)

    if st.checkbox("Show baseline by mag"):
        code_mag = list(df[conf.code_mag].unique())
        id_mag_selected = st.select_slider('What are your favorite colors', code_mag)

        if id_mag_selected is not None:
            df_compare_id_mag = df.query(f"{conf.code_mag} == {id_mag_selected}")
            df_compare_id_mag = pd.melt(df_compare_id_mag, id_vars= conf.col_date, value_vars=conf.name_col)
            df_compare_id_mag = df_compare_id_mag.groupby(by=[conf.col_date, "variable"]).sum()
            df_compare_id_mag.reset_index(inplace=True)

            fig = px.line(df_compare_id_mag, x=conf.col_date, y="value", color="variable")
            st.plotly_chart(fig)






