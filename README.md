# LinkedHeadhunter 👀

**LinkedHeadhunter** is a Python-based growth hacking tool that automates LinkedIn profile views using a city + keyword search strategy. Inspired by the idea that "If you view it, they will come", this tool emulates human browsing behavior to help generate inbound interest and discover leads.

---

## ⚙️ Features

- ✅ Login with LinkedIn credentials (manual 2FA handling supported)
- 🔎 Search by **keywords** + **cities**
- 🌍 Localized and language-filtered search support
- 📄 Saves viewed users and completed queries to logs
- 🔄 Avoids repeated queries and revisits
- 🧠 Uses headless `selenium` automation with robust waiting
- 📁 Maintains daily JSON logs + master log history

---

## 📁 Project Structure

.
├── headhunter.py # Main script
├── template.json # Template for daily logs
├── cities.txt # List of LinkedIn city URNs (with city names)
├── keywords.txt # List of search keywords
├── logs/ # Stores daily logs and user/query history
├── img/ # (Optional) For screenshots or documentation
├── README.md # You're reading it
└── RUN.md # Optional run instructions

---

## 🧪 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (matching your Chrome version): [Download here](https://chromedriver.chromium.org/downloads)

Install dependencies:
```bash
pip install selenium tqdm
