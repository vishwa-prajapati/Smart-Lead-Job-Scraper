import re
import base64

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return list(set(re.findall(email_pattern, text, re.I)))

def extract_phones(text):
    
    pattern = r'\+\d[\d\s\-().]{7,20}'
    matches = re.findall(pattern, text)

    cleaned = []
    for match in matches:
        digits_only = re.sub(r'\D', '', match) 
        if 10 <= len(digits_only) <= 13:
            cleaned.append(match.strip())

    return list(set(cleaned))

def download_link(content, filename, link_text):
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}">{link_text}</a>'