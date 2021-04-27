import streamlit as st
import pandas as pd
import plotly.express as px
import config as conf

st.title("Baseline : Analyse Streamlit")

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])


if data is not None:
    df = pd.read_csv(data, sep=conf.sep)
    float_explcativite_vente = df[conf.col_baseline_vente].sum() / df[conf.col_vente].sum() 
    float_explcativite_vente_web = df[conf.col_baseline_vente_web].sum() / df[conf.col_vente_web].sum()

    if st.checkbox("Show baseline by mag"):
        code_mag = list(df[conf.code_mag].unique())
        id_mag_selected = st.select_slider('Magasin', code_mag)

        if id_mag_selected is not None:
            df_compare_id_mag = df.query(f"{conf.code_mag} == {id_mag_selected}")
            df_compare_id_mag = pd.melt(df_compare_id_mag, id_vars= conf.col_date, value_vars=conf.name_col)
            df_compare_id_mag = df_compare_id_mag.groupby(by=[conf.col_date, "variable"]).sum()
            df_compare_id_mag.reset_index(inplace=True)

            fig = px.line(df_compare_id_mag, x=conf.col_date, y="value", color="variable")
            st.plotly_chart(fig)

    if st.checkbox("Show baseline by cluster"):
        code_cluster = list(df[conf.col_cluster].unique())
        id_cluster_selected = st.select_slider('Cluster', code_cluster)

        if id_cluster_selected is not None:
            df_compare_cluster = df.query(f"{conf.col_cluster} == {id_cluster_selected}")
            df_compare_cluster = pd.melt(df_compare_cluster, id_vars= conf.col_date, value_vars=conf.name_col)
            df_compare_cluster = df_compare_cluster.groupby(by=[conf.col_date, "variable"]).sum()
            df_compare_cluster.reset_index(inplace=True)

            fig = px.line(df_compare_cluster, x=conf.col_date, y="value", color="variable")
            st.plotly_chart(fig)


    if st.checkbox("Show explicativite baseline"):
        st.header('Explicativité baseline') 
        if float_explcativite_vente is not None and float_explcativite_vente_web is not None:
            st.subheader(f"% baseline vente web : {float_explcativite_vente}")
            st.subheader(f"% baseline vente : {float_explcativite_vente_web}")





