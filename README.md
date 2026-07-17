<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
[![Stars](https://img.shields.io/github/stars/SudhanFromGithub/gst_automation?style=flat-square)](https://github.com/SudhanFromGithub/gst_automation/stargazers)
![Last Commit](https://img.shields.io/github/last-commit/SudhanFromGithub/gst_automation)
![Issues](https://img.shields.io/github/issues/SudhanFromGithub/gst_automation)
![Forks](https://img.shields.io/github/forks/SudhanFromGithub/gst_automation)

</div>
---

# 🚀 GST GSTR-1 Summary Automation

Automate GST GSTR-1 summary PDF downloads using **Python + Playwright**.

GST GSTR-1 Summary Automation is a browser automation tool that logs into the GST portal, navigates through the return dashboard, selects financial periods, opens GSTR-1 summaries, and downloads monthly PDF reports automatically.

Built with **Python**, **Playwright**, and **Rich**, this project provides a simple and interactive terminal-based automation experience.

---

## ✨ Features

- ✅ Automated GST portal login
- ✅ Headless and headed browser support
- ✅ CAPTCHA automation support
- ✅ Automatic GST Return Dashboard navigation
- ✅ Financial year selection
- ✅ Quarter and month-wise processing
- ✅ Automatic GSTR-1 summary PDF download
- ✅ Live progress tracking in terminal
- ✅ Automatic retry for incorrect CAPTCHA
- ✅ Organized output file naming

---

## 🖥️ Demo Workflow

```
Start Automation
        │
        ▼
GST Login
        │
        ▼
CAPTCHA Verification
        │
        ▼
Return Dashboard
        │
        ▼
Select Financial Year
        │
        ▼
Process Months
        │
        ▼
Open GSTR-1 Summary
        │
        ▼
Download PDF Reports
```

---

# 📂 Project Structure

```
gst_automation/
│
├── main.py                  # Main automation script
│
├── gst_captcha.py           # CAPTCHA solving module
│
├── requirements.txt         # Python dependencies
│
├── README.md                # Documentation
│
└── captcha.png              # Temporary CAPTCHA image
```

---

# 🛠️ Installation

## Clone Repository

```bash
git clone https://github.com/SudhanFromGithub/gst_automation.git

cd gst_automation
```

---

## Create Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install chromium
```

---

# 📦 Dependencies

| Package | Purpose |
|---|---|
| Playwright | Browser automation |
| Rich | Terminal UI and progress display |
| pathlib | File path management |

---

# ▶️ Usage

Run the automation:

```bash
python main.py
```

The program will ask:

```
Whether you want to run it windowless(yes/no)? :
```

Choose:

```
yes → Run browser in background mode

no → Open browser window
```

---

Enter GST credentials:

```
Enter GST Username:
Enter GST Password:
```

Enter financial year:

```
Enter FY Year of Returns:
```

Example:

```
2024-25
```

---

Example:

```
1.GSTR1_Summary_April.pdf
2.GSTR1_Summary_May.pdf
3.GSTR1_Summary_June.pdf
```

---

# 🐛 Troubleshooting

## Playwright Browser Missing

Run:

```bash
playwright install
```

---

# 🚧 Future Improvements

- [ ] GSTR-1 Nil Return Support 
- [ ] Choose file location and better file naming

---

# ⚠️ Disclaimer

This project is intended for automation and productivity purposes.

Users are responsible for:

- Protecting their credentials
- Following GST portal policies
- Ensuring compliance with applicable regulations

Use automation responsibly.

---
---

# 📜 License

Distributed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

# 👨‍💻 Author

**SudhanFromGithub**

Built with ❤️ using:

- Python
- Playwright
- Rich
