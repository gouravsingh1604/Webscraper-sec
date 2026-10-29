# Web Scraper Security Analysis

A Python tool that takes a website URL, scrapes it, runs basic security checks, and saves the findings as a PDF report.

## Features

- **Web scraping:** pulls the page title, all links and all forms using `requests` and `BeautifulSoup`.
- **SSL/TLS check:** connects on port 443 and reports whether the certificate is valid, plus its issuer and subject.
- **HTTP security header check:** reports whether these headers are present or missing:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
- **Port scan:** uses Nmap to scan ports 1–1024 on the target host.
- **PDF report:** writes all results to `security_report.pdf` using ReportLab.

## Project structure

```
Webscraper-sec/
├── main.py              # Entry point: runs every step in order
├── scraper.py           # Fetches the page, extracts title, links, forms
├── security_checks.py   # SSL certificate, security headers, port scan
├── report_generator.py  # Builds the PDF report
└── security_report.pdf  # Sample generated report
```

## Requirements

- Python 3.8+
- [Nmap](https://nmap.org/download.html) installed on your system and available in your PATH
- Python packages: `requests`, `beautifulsoup4`, `python-nmap`, `reportlab`

## Installation

```bash
git clone https://github.com/gouravsingh1604/Webscraper-sec.git
cd Webscraper-sec

python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install requests beautifulsoup4 python-nmap reportlab
```

## Usage

```bash
python main.py
```

Enter a URL when prompted (include `http://` or `https://`):

```
Enter website URL (with http/https): https://example.com
```

The tool then runs each step and saves `security_report.pdf` in the project folder:

```
[+] Scraping website...
[+] Checking SSL certificate...
[+] Checking security headers...
[+] Running port scan...
[+] Generating report...
[✔] Security analysis completed. Report saved as security_report.pdf
```

## How it works

1. `main.py` reads the URL and extracts the hostname.
2. `scraper.py` fetches the page and collects the title, links and forms.
3. `security_checks.py` validates the SSL certificate, checks the headers and scans ports 1–1024.
4. `report_generator.py` writes everything into a PDF.

## Legal and ethical use

Only scan websites and servers that you own or have written permission to test. Port scanning systems without authorization may be illegal. This project is for learning and authorized security auditing only.

## Possible improvements

- Add a `requirements.txt` file
- Wrap long values and add pagination to the PDF report
- Add severity ratings for missing headers
- Support command-line arguments and custom port ranges
- Check cookie flags and TLS version

## Author

**Gourav Kumar Singh**
[GitHub](https://github.com/gouravsingh1604) · [LinkedIn](https://www.linkedin.com/in/gouravsingh16)
