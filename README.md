# 🧾 Log Analyzer Project

This Python script analyzes Apache-style access logs and generates a CSV report showing:

- Top 5 IP addresses making requests
- Top 5 requested endpoints
- All response status codes and their counts

## 📁 Files

- `access_log`: Sample log file (or use `/var/log/httpd/access_log`)
- `analyzer.py`: Python log parser and CSV report generator
- `report.csv`: Output report generated
- `.gitignore`: Ignores temporary files

## ▶️ Usage

python3 analyzer.py
