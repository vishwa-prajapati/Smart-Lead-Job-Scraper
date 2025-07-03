import streamlit as st
import pandas as pd
from scraper import full_scrape
from utils import download_link

st.set_page_config(page_title="🚀 Smart Lead & Job Scraper", layout="wide")
st.title("🌐 Smart Lead & Job Scraper")


url = st.text_input("Enter base company website", placeholder="https://example.com")

job_role_keywords = st.text_input(
    "Enter keywords for job roles (comma-separated, e.g., engineer,developer,data scientist)",
    value="engineer,developer,manager,intern,analyst,specialist"
)


if st.button("Scrape Website"):
    with st.spinner("Scraping contact details and job openings..."):
       
        job_role_keywords_list = [k.strip() for k in job_role_keywords.split(",") if k.strip()]
        
       
        leads_df, jobs_df = full_scrape(
            url,
            job_role_keywords=job_role_keywords_list
        )

    if not leads_df.empty:
        st.subheader("📞 Extracted Contact Information")
        st.dataframe(leads_df)
        leads_csv = leads_df.to_csv(index=False)
        st.markdown(download_link(leads_csv, "leads.csv", "📥 Download Leads CSV"), unsafe_allow_html=True)
    else:
        st.warning("No contact info found.")

    
    if not jobs_df.empty:
        st.subheader("💼 Extracted Job Openings")
        st.dataframe(jobs_df)
        jobs_csv = jobs_df.to_csv(index=False)
        st.markdown(download_link(jobs_csv, "job_openings.csv", "📥 Download Job Openings CSV"), unsafe_allow_html=True)
    else:
        st.warning("No job openings found.")