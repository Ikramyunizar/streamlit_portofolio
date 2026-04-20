import streamlit as st  

experiences = [{
    "company" : "Multipolar Techonology",
    "position" : "Data Engineer",
    "duration" : "September 2025 - Present",
    "projects" : ["Data Lineage and Metadata System", "Hadoop Migration"],
    "Description": """
        - Consultant for the EDM team at biggest Indonesian energy company,
        - Implementing Talend Studio/Cloud and managing data lineage for subholdings.,
        - Main technical person for data management and governance initiatives using Talend Data Catalog.,
        - Managing servers of talend products in Windows Server
"""

}, {
    "company" : "Juke Solutions",
    "position" : "Data Engineer",
    "duration" : "April 2024 - September 2025",
    "projects" : ["EMIS Kementrian Agama", "Telkomsel B2B Odoo Data warehouse","Telkomsel B2B Executive Dashboard"],
    "Description": """
    - Main data engineer for EMIS Kementrian Agama project Higher education module, responsible for designing and implementing data pipelines using Talend Studio to integrate data and synchronize from Dikti and EMIS 
    - Build Telkomsel B2B Project Tracker Data warehouse from scratch, using Python with only built-in libraries due to security restrictions
    - Assisting in building Telkomsel B2B Executive Dashboard, a dashboard to monitor the performance of Telkomsel's B2B division, using tableau
    - Developing revenue outlook for each Account Manager and team in B2B Division, predicting the revenue with smallest granularity of each Account Manager
""" 
},{
    "company" : "XL Axiata (IDstar Vendor)",
    "position" : "Data Engineer",
    "duration" : "July 2021 - April 2024",
    "projects" : ["Reenginering Analytics Pipelines", "Cloudera To GCP Migration", "One Day Closing (Automated accounting closing)"],
    "Description" : """
    - Lead Developer for One Day Closing project, automating the accounting closing process and reducing closing time from 5 days to 4 hours
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



st.title("My Experiences")

with st.container():
    for i in experiences:
        st.header(f"{i['position']} at {i['company']}")
        st.subheader(i['duration'])
        st.markdown(i['Description'])
        st.markdown("**Projects:**")
        for project in i['projects']:
            st.markdown(f"- {project}")
        st.divider()
    