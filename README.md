# LinkedHeadhunter 👀

**LinkedHeadhunter** is a Python-based growth hacking tool that automates LinkedIn profile views using a city + keyword search strategy. Inspired by the idea that "If you view it, they will come", this tool emulates human browsing behavior to help generate inbound interest and discover leads.

---

## ⚙️ Features

* ✅ Login with LinkedIn credentials (manual 2FA handling supported)
* 🔎 Search by **keywords** + **cities**
* 🌍 Localized and language-filtered search support
* 📄 Saves viewed users and completed queries to logs
* 🔄 Avoids repeated queries and revisits
* 🧠 Uses headless `selenium` automation with robust waiting
* 📁 Maintains daily JSON logs + master log history

---

## 📁 Project Structure

```
.
├── headhunter.py           # Main script
├── template.json           # Template for daily logs
├── cities.txt              # List of LinkedIn city URNs (with city names)
├── keywords.txt            # List of search keywords
├── logs/                   # Stores daily logs and user/query history
├── img/                    # (Optional) For screenshots or documentation
├── README.md               # You're reading it
└── RUN.md                  # Optional run instructions
```

---

## 🧪 Requirements

* Python 3.7+
* Google Chrome
* ChromeDriver (matching your Chrome version): [Download here](https://chromedriver.chromium.org/downloads)

Install dependencies:

```bash
pip install selenium tqdm
```

---

## 🏃‍♂️ Usage

```bash
python3 headhunter.py <linkedin_email> <linkedin_password> <delay_seconds> <page_depth>
```

**Example:**

```bash
python3 headhunter.py john.doe@gmail.com myPassword123 5 10
```

| Parameter           | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| `linkedin_email`    | Your LinkedIn login email                                     |
| `linkedin_password` | Your password (no 2FA support built-in, but waits for manual) |
| `delay_seconds`     | Wait time between actions to mimic human behavior             |
| `page_depth`        | Max pages to visit per search query                           |

---

## 📌 Important Notes

* This script **requires manual 2FA** handling (60-second timeout built-in).
* For ethical use only — respect LinkedIn’s terms of service.
* Save your logs! They contain all collected data and avoid reprocessing the same users/queries.

---

## 📜 Disclaimer

This tool is for educational and research purposes only. The author does not encourage or support any misuse of this script, including scraping data against LinkedIn’s terms.

---

## 💡 Future Improvements (PRs welcome)

* Proxy + CAPTCHA handling
* Headless mode support
* Email finding integration
* GUI interface

---

## 🧑‍💻 Author

* Built by [sohel22z](https://github.com/sohel22z)
* LinkedIn: [LinkedIn/sohelansarii](https://linkedin.com/in/sohelansarii)

---
