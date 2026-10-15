import streamlit as st  

projects = [{
    "Project Name" : "Data Lineage and Metadata Initiation and Infra Monitoring",
    "position" : "Data Engineer",
    "duration" : "September 2025 - Present",
    "Tools Used" : "Talend,Windows Server,Grafana,Prometheus,Azure Data Factory,Talend Data Catalog,Git",
    "Description": """
        - Sole Consultant from Multipolar for the EDM team at biggest Indonesian energy company,
        - Enabling Data Lineage within the holding company with more than 10000 tables and 1000+ pipelines.
        - Initiating Data Management and Governance initiavies, such as Data Stewards Identification, Data Ownership, and Businsess Glossaries and terms.
        - Being Subject Matter Expert for Data Management and Data engineering scopes within EDM Talend pipelines.
"""

}, {
    "Project Name" : "Executive Dashboard and Project Tracker for Telkomsel B2B Division",
    "position" : "Data Engineer",
    "duration" : "January 2025 - September 2025",
    "Tools Used" : "Python,Tableau,PostgreSQL,DuckDB" ,
    "Description": """
    - Main data engineer for the project.
    - Capturing B2B Division's KPI, such as Revenue, New Customer Acquisition, Project delivery status, with the granularity down to every sales, customer and work orders   
    - Assisting in building Telkomsel B2B Executive Dashboard, a dashboard to monitor the performance of Telkomsel's B2B division, using tableau
    - Making innovation to simplify working workflow within the internal team due to stricts security poliicies within the client, with DuckDB as the main data source for local development
""" 
},{
    "Project Name" : "EMIS",
    "position" : "Data Engineer",
    "duration" : "April 2024 - March 2025",
    "Tools used" : "Talend, Google Cloud Platform, MySQL, Rundeck, Bash, BigQuery",
    "Description" : """
    - Main Data engineer for the EMIS Pendidikan Tinggi Module.
    - Designing data models and pipelines end to end for WEB API consumption, starting from source into gold layer
    - Building data pipelines from scratch using various Tools, such as Spark, Ab Initio, and Python depending on the tools various teams uses. 
    
    """
},{
    "Project Name" : "One Day Closing",
    "position" : "Data Engineer",
    "duration" : "April 2022 - April 2024",
    "Tools used" : "AB Initio, Google Cloud Platform, Spark, Python, Bash Scripting",
    "Description" : """
    - Handling Accounting Closing automation every month
    - Handling 1b+ records monthly in accrual and actual processing
    - Lead Data Developer and managing 2 other Developers regarding the job and main template
    
    """
},{
    "Project Name" : "Reenginering Analytics Pipelines",
    "position" : "Data Engineer",
    "duration" : "July 2021 - August 2022",
    "Tools used" : "AB Initio, Apache Spark, Google Cloud Platform, Cloudera, Bash Scripting",
    "Description" : """
    - Improving existing Analytics team pipelines into EDM managed pipelines
    - Handling 700m+ data daily, with the most improved query improving from 18 Hours to 15 Minutes
    - Improving data storage and processing in Cloudera
    - 
    
    """
},{
    "Project Name" : "EMIS",
    "position" : "Data Engineer",
    "duration" : "April 2021 - March 2025",
    "Tools used" : "Talend, Google Cloud Platform, MySQL, Rundeck, and others",
    "Description" : """
    - Main Data engineer for the EMIS Pendidikan Tinggi Module.
    - Reengineering Analytics team Pipelines, with the most improved query improving from 18 Hours to 15 Minutes    - Migrating on-premise Cloudera data warehouse to Google Cloud Platform 
    - Building data pipelines from scratch using various Tools, such as Spark, Ab Initio, and Python depending on the tools various teams uses. 
    
    """
},{
    "Project Name" : "EMIS",
    "position" : "Data Engineer",
    "duration" : "April 2021 - March 2025",
    "Tools used" : "Talend, Google Cloud Platform, MySQL, Rundeck, and others",
    "Description" : """
    - Main Data engineer for the EMIS Pendidikan Tinggi Module.
    - Reengineering Analytics team Pipelines, with the most improved query improving from 18 Hours to 15 Minutes    - Migrating on-premise Cloudera data warehouse to Google Cloud Platform 
    - Building data pipelines from scratch using various Tools, such as Spark, Ab Initio, and Python depending on the tools various teams uses. 
    
    """
}

]


github = 'https://github.com/Ikramyunizar'
with st.sidebar:
    st.subheader(":small[Contacts :]")
    st.markdown(":small[✉️ ikramyunizar@gmail.com]")
    st.markdown(":small[[My Github](%s)]" % github )



st.title("My Projects")

with st.container():
    for i in projects:
        st.subheader(f"{i['position']} in {i['Project Name']}")
        st.markdown(f"Tools : {i['Tools Used']}")
        st.markdown(i['Description'])

        st.divider()
    