import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pandas as pd
from fake_useragent import UserAgent
from collections import defaultdict
from utils import extract_emails, extract_phones

def find_links(base_url, html, keywords):
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for tag in soup.find_all("a", href=True):
        href = tag["href"].lower()
        if any(k in href for k in keywords):
            full_url = urljoin(base_url, href)
            links.add(full_url)
    return list(links)

def scrape_contacts(base_url, contact_keywords):
    headers = {"User-Agent": UserAgent().random}
    visited, queue = set(), [base_url]
    results = defaultdict(lambda: {"emails": set(), "phones": set(), "urls": set()})

    try:
        while queue and len(visited) < 5:
            current = queue.pop(0)
            if current in visited:
                continue

            res = requests.get(current, headers=headers, timeout=10)
            if not res.ok:
                continue

            html = res.text
            visited.add(current)

            emails = set(extract_emails(html))
            phones = set(extract_phones(html))

            for email in emails:
                results[email]["emails"].add(email)
                results[email]["urls"].add(current)

            for phone in phones:
                results[phone]["phones"].add(phone)
                results[phone]["urls"].add(current)

            if current == base_url:
                queue += find_links(base_url, html, contact_keywords)

    except Exception as e:
        print("Contact scrape error:", e)
        return pd.DataFrame()

    final = []
    for _, v in results.items():
        final.append({
            "emails": ", ".join(v["emails"]),
            "phones": ", ".join(v["phones"]),
            "sources": ", ".join(v["urls"]),
           
        })

    return pd.DataFrame(final)

def extract_jobs(html, job_role_keywords):
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    for tag in soup.find_all(['li', 'div', 'tr']):
        text = tag.get_text(separator=" ").strip()
        if any(word in text.lower() for word in job_role_keywords):
            jobs.append(text)

    structured = []
    for raw in set(jobs):
        structured.append({
            "job_title": extract_job_title(raw, job_role_keywords),
            "job_description": raw,
           
        })

    return pd.DataFrame(structured)

def extract_job_title(text, job_role_keywords):
    for line in text.split('\n'):
        for word in job_role_keywords:
            if word in line.lower():
                return line.strip()
    return text.split('\n')[0][:60]

def extract_experience(text):
    import re
    match = re.search(r"(\d+)[\+]? ?(years|yrs)", text.lower())
    return match.group(0) if match else "Not specified"

def extract_tech_stack(text):
    stack = ["python", "java", "react", "node", "aws", "sql", "docker", "c++", "html", "css"]
    found = [tech for tech in stack if tech in text.lower()]
    return ", ".join(found) if found else "N/A"

def scrape_jobs(base_url, job_keywords, job_role_keywords):
    headers = {"User-Agent": UserAgent().random}
    try:
        res = requests.get(base_url, headers=headers, timeout=10)
        if not res.ok:
            return pd.DataFrame()

        html = res.text
        links = find_links(base_url, html, job_keywords)

        all_jobs = []
        for url in links:
            try:
                res2 = requests.get(url, headers=headers, timeout=10)
                if res2.ok:
                    job_df = extract_jobs(res2.text, job_role_keywords)
                    job_df["source"] = url
                    all_jobs.append(job_df)
            except:
                continue

        return pd.concat(all_jobs, ignore_index=True) if all_jobs else pd.DataFrame()

    except Exception as e:
        print("Job scrape error:", e)
        return pd.DataFrame()

def full_scrape(url, contact_keywords=None, job_keywords=None, job_role_keywords=None):
    contact_keywords = contact_keywords or ["contact", "about", "team", "support"]
    job_keywords = job_keywords or ["careers", "jobs", "join-us", "work-with-us"]
    job_role_keywords = job_role_keywords or ["engineer", "developer", "manager", "intern", "analyst", "specialist"]
    
    contacts = scrape_contacts(url, contact_keywords)
    jobs = scrape_jobs(url, job_keywords, job_role_keywords)
    if not jobs.empty:
        if not contacts.empty:
            jobs["email"] = contacts["emails"].iloc[0] if not contacts["emails"].isnull().all() else ""
            
        else:
            jobs["email"] = ""
            
    return contacts, jobs