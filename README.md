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
git clone https://github.com/<username>/gst_automation.git

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
playwright install
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

# 📅 Automated Processing

The script processes all months:

```
Quarter 1
 ├── April
 ├── May
 └── June

Quarter 2
 ├── July
 ├── August
 └── September

Quarter 3
 ├── October
 ├── November
 └── December

Quarter 4
 ├── January
 ├── February
 └── March
```

For every month the automation:

1. Selects financial year
2. Selects quarter
3. Selects month
4. Opens GSTR-1 return
5. Opens summary page
6. Generates PDF
7. Saves the report

---

# 📄 Output

Downloaded files are saved automatically:

```
~/Desktop/
```

Example:

```
1.GSTR1_Summary_April.pdf
2.GSTR1_Summary_May.pdf
3.GSTR1_Summary_June.pdf
```

---

# 🔐 Security Recommendations

⚠️ Never store GST credentials directly inside the source code.

Recommended:

- Environment variables
- Password managers
- Secret management systems

Example:

```
GST_USERNAME=username
GST_PASSWORD=password
```

---

# 🧩 CAPTCHA Handling

The project uses a separate CAPTCHA module:

```python
from gst_captcha import solve_captcha
```

The login flow:

1. Captures CAPTCHA image
2. Solves CAPTCHA
3. Submits login
4. Retries automatically if validation fails

---

# 🐛 Troubleshooting

## Playwright Browser Missing

Run:

```bash
playwright install
```

---

## Login Failure

Check:

- GST username/password
- Internet connection
- CAPTCHA solver
- GST portal availability

---

## PDF Download Failure

Verify:

- Financial year exists
- Return period is available
- Browser session is active

---

# 🚧 Future Improvements

- [ ] Multiple GST account support
- [ ] Secure credential storage
- [ ] Excel report generation
- [ ] Automatic monthly scheduling
- [ ] GUI application
- [ ] Better logging system
- [ ] Cloud execution support

---

# 🤝 Contributing

Contributions are welcome.

## Steps

Create a branch:

```bash
git checkout -b feature/new-feature
```

Commit changes:

```bash
git commit -m "Add new feature"
```

Push:

```bash
git push origin feature/new-feature
```

Create a Pull Request.

---

# ⚠️ Disclaimer

This project is intended for automation and productivity purposes.

Users are responsible for:

- Protecting their credentials
- Following GST portal policies
- Ensuring compliance with applicable regulations

Use automation responsibly.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**SudhanFromGithub**

Built with ❤️ using:

- Python
- Playwright
- Rich
