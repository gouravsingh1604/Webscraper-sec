import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Failed to fetch {url}: {str(e)}"}

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Collect links and forms
    links = [a["href"] for a in soup.find_all("a", href=True)]
    forms = soup.find_all("form")

    return {
        "title": soup.title.string if soup.title else "No Title",
        "links": links,
        "forms": forms
    }
