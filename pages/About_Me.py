import streamlit as st
import plotly.express as pltex
import pandas as pd

skills_dict = {
'Big Data and Database' : ['BigQuery','Cloudera','Iceberg','Hadoop','SQL Server','Teradata','Greenplum','MySQL','PostgreSQL'],
'Languange' : ['Python','SQL','Bash','R','PHP','Javascript'],
'Cloud' : ['Google Cloud Platform','Amazon Web Services','Azure'],
'ETL' : ['Apache Spark','Duckdb','Talend','AB Initio','Pentaho','dlt'],
'Metadata Management' : ['Talend Data Catalog','OpenMetadata'],
'Other Tools' : ['Docker','Git','Airflow','Rundeck']
}



base_skills = dict(
    skills_level = [90,80,80,90,70],
    skills = ['Pipeline Development','Data Modeling','DQ and Governance','Analytics Engineering','Visualization']
)
skills_df = pd.DataFrame(base_skills)


head_c = st.container()
head_c.title("Ikram Yunizar")

head_c.header("Data Engineer")

head_c.markdown("""Experienced Data Engineer with 5+ years in consulting, bringing a versatile track record across Telecommunications, Oil & Gas, Retail, Healthcare, and beyond. Adept at architecting scalable data pipelines and infrastructure from the ground up, while also identifying opportunities to modernize and optimize existing legacy systems.
 Combines strong technical depth with a problem-solving mindset to deliver practical, 
                forward-thinking solutions across a wide range of business contexts.
                 """)


radar_chart = pltex.line_polar(skills_df,r='skills_level',theta='skills',line_close=True)
# radar_chart.update_traces(fill='toself')
radar_chart.update_layout(template='plotly_dark')
radar_chart.update_traces(fill='toself')
radar_chart.update_layout(font=dict(size=14))

st.header('Overall Skills')
st.plotly_chart(radar_chart)

st.header('Tools and Languanges')

for title, value in skills_dict.items():
    with st.expander(title):
        st.write(', '.join(value))


