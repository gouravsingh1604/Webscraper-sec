from scraper import scrape_website
from security_checks import check_ssl_certificate, check_security_headers, port_scan
from report_generator import generate_report
import socket

def main():
    url = input("Enter website URL (with http/https): ")
    hostname = url.replace("http://", "").replace("https://", "").split("/")[0]

    print("\n[+] Scraping website...")
    scraped_data = scrape_website(url)

    print("[+] Checking SSL certificate...")
    ssl_data = check_ssl_certificate(hostname)

    print("[+] Checking security headers...")
    header_data = check_security_headers(url)

    print("[+] Running port scan...")
    port_data = port_scan(hostname)

    final_data = {
        "Scraped Data": scraped_data,
        "SSL Certificate": ssl_data,
        "Security Headers": header_data,
        "Port Scan": port_data
    }

    print("[+] Generating report...")
    generate_report("security_report.pdf", url, final_data)

    print("[✔] Security analysis completed. Report saved as security_report.pdf")

if __name__ == "__main__":
    main()
