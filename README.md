# 🚀 Smart Lead & Job Scraper

This project is a submission for **Caprae Capital’s AI-Readiness Pre-Screening Challenge**, built to demonstrate how practical AI solutions can transform businesses post-acquisition. It is a lightweight, deployable web scraping tool that extracts **contact information** and **job listings** from public company websites — enabling business teams to detect growth signals and engage leads intelligently.

---

## 🔗 Live Demo

🟢 Try it here:  
👉 [https://smart-lead-job-scraper-3anx2cnboucyzcbkh9h5lc.streamlit.app/]

---

## 🎯 Project Purpose

Caprae Capital’s mission to create post-acquisition value through AI-driven operations inspired this tool. It aims to support lead generation by identifying growing companies (via job postings) and surfacing their contact information — all with zero setup and within a 5-hour development constraint. The result is a fast, focused tool built for real-world impact.

---

## ✨ Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 📞 Contact Info Scraper     | Extracts emails, phone numbers, and the source URLs                         |
| 💼 Job Listings Extractor   | Finds job titles and descriptions based on custom keywords                  |
| 📤 CSV Export               | One-click download of leads and job data in CSV format                      |
| ⚙️ Keyword Customization    | Easily configure job role focus (e.g., "developer", "manager")              |
| 🧑‍💼 Clean UI for Business   | Built with Streamlit — simple, fast, and intuitive for non-tech users       |

---

## 🧠 Design & Technical Approach

- 🛠 **Built With**: Python, Streamlit, Requests, BeautifulSoup, Pandas
- 🧠 **Smart Extraction**: Regex-based parsing for emails & phone numbers
- ⚙️ **Dynamic Filtering**: User-defined job-role keywords
- 🧾 **Output**: Structured Pandas DataFrames with export options
- 🚀 **Deployable**: App hosted on Streamlit Community Cloud

---

## 🛠 Setup Instructions

### 1. Clone this Repo


git clone https://github.com/vishwa-prajapati/Smart-Lead-Job-Scraper.git
cd smart-leadgen-scraper


## 2. Install Dependencies
pip install -r requirements.txt


## 3. Run the App
streamlit run app.py

---


## 📁 Folder Structure
smart-leadgen-scraper/ <br>
├── app.py               # Streamlit UI<br>
├── scraper.py           # Scraping logic<br>
├── utils.py             # Regex-based extractors & download function<br>
├── requirements.txt     # Dependency list<br>
├── README.md            # You’re reading it!<br>


---


## **🧩 Criteria	✅ How It’s Met**
Business Use Case	Surfaces high-value leads via hiring signals & contact discovery
UX/UI	Clean, intuitive layout with expandable sections and CSV export
Technical Execution	BeautifulSoup-based scraping, regex parsing, user-agent spoofing
Design Aesthetic	Minimalist, professional, mobile-friendly interface
Creative Value-Add	Custom role filters, CSV download, CRM-ready outputs

---


## **📑 Report Summary**
This solution was built within 5 hours as a lightweight leadgen scraper. It scrapes live job postings and contact details from company websites, guided by user-defined keywords. The output is presented via a Streamlit UI with instant CSV export. It’s designed to signal growth-ready companies and unlock outreach opportunities for sales or M&A teams. The tool is flexible, fast, and aligns with Caprae Capital’s goal of enabling post-acquisition value through AI.


---


## **🔮 Future Enhancements**
To align with real-world lead qualification and sales workflows, the following features are planned: <br>

✅ Email Verification APIs – Integrate services like NeverBounce or ZeroBounce for validated contact lists <br>
🌐 LinkedIn/Glassdoor Add-ons – Augment with external hiring signals and company insights<br>
🧠 AI Chat Agent – Let users ask questions like “Which companies are hiring backend engineers in SaaS?”<br>


---


##  **👨‍💻 About the Developer**
Vishwa Prajapati <br>
📍 Mehsana, Gujarat <br>
📫 vishwaprajapati317@gmail.com <br>


---


##  **📄 License**
This project is licensed under the MIT License.


---


## **🌟 Acknowledgments**
Special thanks to Caprae Capital for the challenge and inspiration, and to the SaaSquatch Leads concept for the business problem reference.

---

## **Additional Options**:
- If you want a **PDF export**, I can guide you to copy this markdown into a tool like VS Code or Obsidian, then use a markdown-to-PDF converter (e.g., Pandoc or a browser extension).
- For a downloadable `README.md`, you can copy the above code into a file named `README.md` and save it in your project directory.
- If you need help with a **video walkthrough script** or **Loom outline**, let me know, a
